# /// script
# requires-python = ">=3.11"
# dependencies = ["beautifulsoup4>=4.12", "markdownify>=0.13"]
# ///
"""Aside 원본 HTML 을 요약 노트 초안(markdown)과 이미지 파일로 바꾼다.

사용법:
    uv run scripts/html2md.py <원본 HTML> <출력 md> <이미지 폴더>

예:
    uv run scripts/html2md.py \
        raw/2026-10-26_agentos_delegate-to-claude/original.html \
        notes/2026-10-26_agentos_delegate-to-claude.md \
        raw/2026-10-26_agentos_delegate-to-claude/img

- HTML 안의 base64 이미지를 이미지 폴더에 001.jpg 형식으로 저장한다.
- md 의 이미지 경로는 md 파일 위치 기준 상대 경로로 바꾼다.
- 마지막 줄에 링크 수, 이미지 수, 표 행 수, 머리글 수를 출력한다.
  사용자는 이 수를 원천과 비교한다.
"""

import base64
import os
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify


def main() -> None:
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    src, out, img_dir = (Path(a) for a in sys.argv[1:])
    img_dir.mkdir(parents=True, exist_ok=True)
    out.parent.mkdir(parents=True, exist_ok=True)

    soup = BeautifulSoup(src.read_text(encoding="utf-8"), "html.parser")
    for tag in soup(["style", "script"]):
        tag.decompose()

    rel_img_dir = Path(os.path.relpath(img_dir, out.parent))
    count = 0
    for img in soup.find_all("img"):
        m = re.match(r"data:image/(\w+);base64,(.*)", img.get("src", ""), re.S)
        if not m:
            continue
        count += 1
        ext = m.group(1).replace("jpeg", "jpg")
        name = f"{count:03d}.{ext}"
        (img_dir / name).write_bytes(base64.b64decode(m.group(2)))
        img["src"] = (rel_img_dir / name).as_posix()

    md = markdownify(str(soup), heading_style="ATX", bullets="-")
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
    out.write_text(md, encoding="utf-8")

    links = len(re.findall(r"\]\(https?://", md))
    images = md.count("![")
    rows = len(re.findall(r"^\|", md, re.M))
    heads = len(re.findall(r"^#", md, re.M))
    print(f"{out} links={links} images={images} table_rows={rows} headings={heads}")


if __name__ == "__main__":
    main()
