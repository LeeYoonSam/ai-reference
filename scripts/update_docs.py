"""Regenerate the AUTO blocks in README.md and README.ko.md, and check docs and library integrity.
README.md 와 README.ko.md 의 AUTO 블록을 다시 만들고, 문서와 라이브러리의 정합성을 검사한다.

Usage:
    python3 scripts/update_docs.py           # rewrite AUTO blocks in place
    python3 scripts/update_docs.py --check   # exit 1 if anything is stale or broken

The script uses only the Python standard library, so git hooks and CI can run it
without installing packages.

AUTO blocks look like this in both READMEs:
    <!-- AUTO:cards -->
    ...generated content...
    <!-- /AUTO:cards -->

Do not edit text between the markers by hand. The next run overwrites it.

Checks in --check mode:
  1. Every AUTO block matches what the generator would write now.
  2. README.md and README.ko.md have the same heading structure (translation parity).
  3. Every top-level folder or file has a description in LAYOUT below.
  4. Every card file is listed in index.md, and every index.md link points to a file.
  5. Every script in scripts/ has a two-line docstring (English line, Korean line).
"""

from __future__ import annotations

import ast
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
READMES = {"en": ROOT / "README.md", "ko": ROOT / "README.ko.md"}

# Top-level entries and their descriptions. Add a line here when you add a top-level entry.
# --check fails on any entry missing from this table, so the README layout cannot drift.
LAYOUT = {
    "README.md": ("Project guide (English). AUTO blocks are generated.", "프로젝트 안내서(영어). AUTO 블록은 자동 생성된다."),
    "README.ko.md": ("Project guide (Korean).", "프로젝트 안내서(한국어)."),
    "DESIGN.md": ("Design document. The source of truth for all rules.", "설계 문서. 모든 규칙의 원본이다."),
    "CLAUDE.md": ("Rules Claude follows in every session in this repository.", "Claude 가 이 저장소의 모든 세션에서 따르는 규칙."),
    "index.md": ("One line per card. Claude reads this first.", "카드마다 1줄. Claude 가 가장 먼저 읽는다."),
    "log.md": ("Append-only work log (requested, ingested, compare).", "추가만 하는 작업 기록(requested, ingested, compare)."),
    "notes": ("Normalized notes. One per source.", "표준 형식 요약 노트. 원천 1개당 1개."),
    "cards": ("Cards. One principle, pattern, prompt, or case per file.", "카드. 파일 1개에 원칙, 패턴, 프롬프트, 사례 중 1개."),
    "templates": ("Aside request templates used by /aside.", "/aside 가 쓰는 Aside 요청 템플릿."),
    "scripts": ("Conversion and documentation scripts.", "변환 스크립트와 문서 자동화 스크립트."),
    "research": ("Deep-research notes and reports behind the design.", "설계의 근거가 된 딥리서치 노트와 보고서."),
    ".claude": ("Claude Code project skills (/ref, /aside).", "Claude Code 프로젝트 skill(/ref, /aside)."),
    ".githooks": ("Git hooks. pre-commit regenerates and checks the docs.", "git hook. pre-commit 이 문서를 다시 만들고 검사한다."),
    ".github": ("CI workflow that runs the docs check on GitHub.", "GitHub 에서 문서 검사를 실행하는 CI workflow."),
    ".gitignore": ("Keeps raw/ and site/ out of git.", "raw/ 와 site/ 를 git 에서 제외한다."),
    "prompts": ("Prompts that proved useful in real work.", "실무에서 효과를 확인한 프롬프트."),
    "inbox": ("New items found by feed tracking, before triage.", "피드 추적으로 찾은 새 자료. 분류 전 상태."),
    "sources": ("List of people and feeds to track.", "추적할 사람과 피드 목록."),
    "raw": ("Local only. Original PDF, HTML, transcripts, images. Not in git.", "로컬 전용. 원본 PDF, HTML, 자막, 이미지. git 에 없다."),
    "site": ("Local only. Generated web pages (planned). Not in git.", "로컬 전용. 생성된 웹페이지(계획). git 에 없다."),
}
SKIP_ENTRIES = {".git", ".DS_Store", "__pycache__", ".venv"}
LOCAL_ONLY = {"raw", "site"}

CATEGORY = {
    "delegation": ("Delegation", "맡기는 방식"),
    "verification": ("Verification and review", "검증과 리뷰"),
    "context": ("Context, skills, handoff", "컨텍스트, skill, 작업 이어 가기"),
    "hr-automation": ("HR automation cases", "HR 업무 자동화 사례"),
    "format": ("Answer format", "답변 포맷"),
}

T = {
    "en": {
        "sources": "Sources", "cards": "Cards", "skills": "Skills", "last": "Last ingest",
        "path": "Path", "desc": "Description", "local": "local only",
        "title": "Title", "type": "Type", "half": "Half-life", "review": "Review by",
        "pub": "Published", "channel": "Channel", "docid": "Doc ID", "ncards": "Cards",
        "skill": "Skill", "usage": "Usage", "file": "File", "purpose": "Purpose",
        "none": "None yet.",
    },
    "ko": {
        "sources": "원천", "cards": "카드", "skills": "skill", "last": "마지막 가져오기",
        "path": "경로", "desc": "설명", "local": "로컬 전용",
        "title": "제목", "type": "유형", "half": "반감기", "review": "재검토일",
        "pub": "게시일", "channel": "채널", "docid": "문서 ID", "ncards": "카드 수",
        "skill": "skill", "usage": "사용법", "file": "파일", "purpose": "용도",
        "none": "아직 없다.",
    },
}


# ---------- reading the repository ----------

def frontmatter(path: Path) -> dict[str, str]:
    """Read top-level scalar keys from YAML frontmatter. Nested blocks are skipped."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    out: dict[str, str] = {}
    for line in m.group(1).splitlines():
        km = re.match(r"([A-Za-z_][\w-]*):\s*(.*)$", line)
        if not km:
            continue
        value = re.sub(r"\s+#.*$", "", km.group(2)).strip().strip('"').strip("'")
        out[km.group(1)] = value
    return out


def cards() -> list[dict[str, str]]:
    items = []
    for p in sorted((ROOT / "cards").glob("*/*.md")):
        fm = frontmatter(p)
        fm["_path"] = p.relative_to(ROOT).as_posix()
        fm["_category"] = p.parent.name
        items.append(fm)
    return items


def notes() -> list[dict[str, str]]:
    items = []
    for p in sorted((ROOT / "notes").glob("*.md")):
        fm = frontmatter(p)
        fm["_path"] = p.relative_to(ROOT).as_posix()
        items.append(fm)
    return items


def skills() -> list[dict[str, str]]:
    items = []
    for p in sorted((ROOT / ".claude" / "skills").glob("*/SKILL.md")):
        fm = frontmatter(p)
        fm["_path"] = p.relative_to(ROOT).as_posix()
        items.append(fm)
    return items


def script_docs() -> list[tuple[str, str, str]]:
    out = []
    for p in sorted((ROOT / "scripts").glob("*.py")):
        doc = ast.get_docstring(ast.parse(p.read_text(encoding="utf-8"))) or ""
        lines = [line.strip() for line in doc.splitlines()]
        en = lines[0] if lines else ""
        ko = lines[1] if len(lines) > 1 else ""
        out.append((p.relative_to(ROOT).as_posix(), en, ko))
    return out


def last_ingest() -> str:
    log = ROOT / "log.md"
    if not log.exists():
        return "-"
    dates = re.findall(r"^(\d{4}-\d{2}-\d{2}) ingested", log.read_text(encoding="utf-8"), re.M)
    return max(dates) if dates else "-"


def top_entries() -> list[str]:
    # Local-only folders are always listed, so the output is the same on this Mac and in CI.
    names = {n for n in os.listdir(ROOT) if n not in SKIP_ENTRIES} | LOCAL_ONLY
    order = list(LAYOUT)
    return sorted(names, key=lambda n: (order.index(n) if n in order else len(order), n))


# ---------- rendering AUTO blocks ----------

def cell(text: str) -> str:
    return text.replace("|", "/").replace("\n", " ")


def render_stats(lang: str) -> str:
    t = T[lang]
    cs = cards()
    by_cat: dict[str, int] = {}
    order = list(CATEGORY)
    for c in sorted(cs, key=lambda c: order.index(c["_category"]) if c["_category"] in order else len(order)):
        by_cat[c["_category"]] = by_cat.get(c["_category"], 0) + 1
    i = 0 if lang == "en" else 1
    parts = ", ".join(f"{CATEGORY.get(k, (k, k))[i]} {v}" for k, v in by_cat.items())
    return "\n".join([
        f"| {t['sources']} | {t['cards']} | {t['skills']} | {t['last']} |",
        "|---|---|---|---|",
        f"| {len(notes())} | {len(cs)} ({parts}) | {len(skills())} | {last_ingest()} |",
    ])


def render_layout(lang: str) -> str:
    t = T[lang]
    i = 0 if lang == "en" else 1
    rows = [f"| {t['path']} | {t['desc']} |", "|---|---|"]
    for name in top_entries():
        is_dir = (ROOT / name).is_dir() or name in LOCAL_ONLY
        label = f"`{name}/`" if is_dir else f"`{name}`"
        desc = LAYOUT.get(name, ("UNDOCUMENTED. Add it to LAYOUT in scripts/update_docs.py.",) * 2)[i]
        rows.append(f"| {label} | {cell(desc)} |")
    return "\n".join(rows)


def render_sources(lang: str) -> str:
    t = T[lang]
    cs = cards()
    rows = [f"| {t['pub']} | {t['channel']} | {t['title']} | {t['docid']} | {t['ncards']} |", "|---|---|---|---|---|"]
    for n in notes():
        count = sum(1 for c in cs if c.get("source_note") == n["_path"])
        title = f"[{cell(n.get('title', n['_path']))}]({n['_path']})"
        rows.append(f"| {n.get('published', '-')} | {cell(n.get('channel', '-'))} | {title} | `{n.get('doc_id', '-')}` | {count} |")
    return "\n".join(rows) if len(rows) > 2 else t["none"]


def render_cards(lang: str) -> str:
    t = T[lang]
    i = 0 if lang == "en" else 1
    cs = cards()
    if not cs:
        return t["none"]
    out = []
    cats = list(dict.fromkeys(c["_category"] for c in cs))
    order = list(CATEGORY)
    cats.sort(key=lambda k: order.index(k) if k in order else len(order))
    for cat in cats:
        out.append(f"**{CATEGORY.get(cat, (cat, cat))[i]}**")
        out.append("")
        out.append(f"| {t['title']} | {t['type']} | {t['half']} | {t['review']} |")
        out.append("|---|---|---|---|")
        for c in (c for c in cs if c["_category"] == cat):
            out.append(f"| [{cell(c.get('title', c['_path']))}]({c['_path']}) | {c.get('type', '-')} | {c.get('half_life', '-')} | {c.get('review_by', '-')} |")
        out.append("")
    return "\n".join(out).rstrip()


def render_skills(lang: str) -> str:
    t = T[lang]
    rows = [f"| {t['skill']} | {t['usage']} | {t['file']} |", "|---|---|---|"]
    for s in skills():
        usage = f"`/{s.get('name', '?')} {s.get('argument-hint', '')}`".replace(" `", "`")
        rows.append(f"| `/{s.get('name', '?')}` | {cell(usage)} | [{s['_path']}]({s['_path']}) |")
    return "\n".join(rows) if len(rows) > 2 else t["none"]


def render_scripts(lang: str) -> str:
    t = T[lang]
    rows = [f"| {t['file']} | {t['purpose']} |", "|---|---|"]
    for path, en, ko in script_docs():
        rows.append(f"| [`{path}`]({path}) | {cell(en if lang == 'en' else ko)} |")
    return "\n".join(rows)


BLOCKS = {
    "stats": render_stats,
    "layout": render_layout,
    "sources": render_sources,
    "cards": render_cards,
    "skills": render_skills,
    "scripts": render_scripts,
}
MARKER = re.compile(r"(<!-- AUTO:(\w+) -->\n)(.*?)(<!-- /AUTO:\2 -->)", re.S)


def regenerate(text: str, lang: str) -> str:
    def repl(m: re.Match) -> str:
        name = m.group(2)
        if name not in BLOCKS:
            return m.group(0)
        return f"{m.group(1)}{BLOCKS[name](lang)}\n{m.group(4)}"
    return MARKER.sub(repl, text)


# ---------- checks ----------

def headings(text: str) -> list[int]:
    levels, fence = [], False
    for line in text.splitlines():
        if line.startswith("```"):
            fence = not fence
        elif not fence and re.match(r"#{1,6} ", line):
            levels.append(len(line) - len(line.lstrip("#")))
    return levels


def check(texts: dict[str, str]) -> list[str]:
    problems = []
    for lang, path in READMES.items():
        if not path.exists():
            problems.append(f"{path.name} is missing.")
            continue
        current = path.read_text(encoding="utf-8")
        if regenerate(current, lang) != current:
            problems.append(f"{path.name}: AUTO blocks are stale. Run python3 scripts/update_docs.py.")
        missing = set(BLOCKS) - set(n for _, n, _, _ in MARKER.findall(current))
        if missing:
            problems.append(f"{path.name}: missing AUTO blocks: {', '.join(sorted(missing))}.")
    if all(p.exists() for p in READMES.values()):
        en, ko = (headings(READMES[k].read_text(encoding="utf-8")) for k in ("en", "ko"))
        if en != ko:
            problems.append(f"README.md and README.ko.md heading structure differs ({len(en)} vs {len(ko)} headings). Update the translation.")
    for name in top_entries():
        if name not in LAYOUT:
            problems.append(f"Top-level entry '{name}' has no description in LAYOUT (scripts/update_docs.py).")
    index = (ROOT / "index.md").read_text(encoding="utf-8") if (ROOT / "index.md").exists() else ""
    linked = set(re.findall(r"\]\((cards/[^)]+\.md)\)", index))
    on_disk = {c["_path"] for c in cards()}
    for p in sorted(on_disk - linked):
        problems.append(f"index.md does not list {p}.")
    for p in sorted(linked - on_disk):
        problems.append(f"index.md links to a missing file: {p}.")
    for path, en, ko in script_docs():
        if not en or not ko or not re.search(r"[가-힣]", ko):
            problems.append(f"{path}: docstring needs an English first line and a Korean second line.")
    return problems


def main() -> int:
    check_only = "--check" in sys.argv[1:]
    texts = {}
    for lang, path in READMES.items():
        if not path.exists():
            continue
        current = path.read_text(encoding="utf-8")
        texts[lang] = current
        if not check_only:
            new = regenerate(current, lang)
            if new != current:
                path.write_text(new, encoding="utf-8")
                print(f"updated {path.name}")
    if not check_only:
        return 0
    problems = check(texts)
    for p in problems:
        print(f"docs check: {p}", file=sys.stderr)
    if not problems:
        print("docs check: ok")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
