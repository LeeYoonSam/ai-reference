# AI 레퍼런스 라이브러리 설계

| 항목 | 내용 |
|---|---|
| 문서 상태 | 확정안 v1 |
| 작성일 | 2026-10-29 |
| 다음 검토일 | 2027-01-29 |
| 근거 자료 | `research/2026-10-29_지식베이스-설계/report.md`, `research/2026-10-29_지식베이스-설계/notes/` |

## 0. 한눈에 보기

이 프로젝트는 유통기한이 붙은 원칙 카드 라이브러리다. 사용자는 업무 중에 `/ref` 로 카드를 찾는다. Claude 는 요청을 받으면 카드를 근거로 프롬프트를 추천한다. Claude 는 추천 프롬프트와 카드 없는 기본 프롬프트를 함께 낸다.

새 자료는 `/aside <링크>` 로 시작한다. Claude 가 프로젝트 형식을 지키는 Aside 요청 프롬프트를 만든다. git 에는 텍스트만 넣는다. PDF·HTML·이미지·자막 같은 원천 파일은 git 밖의 로컬 폴더에 둔다. 사용자는 원천 HTML 이나 PDF 를 브라우저로 직접 연다. 라이브러리 전체는 Obsidian 이나 로컬 웹페이지로 본다.

## 1. 목적

1. 사용자가 실무 작업에 맞는 레퍼런스를 1분 안에 찾는다.
2. Claude 가 레퍼런스를 근거로 작업 프롬프트를 추천한다.
3. 라이브러리가 새 자료를 계속 받아들인다.
4. 라이브러리가 낡은 조언을 스스로 찾아낸다.

현재 중심 주제는 "클로드에게 일을 맡기는 법" 이다. HR 자동화 사례는 두 번째 주제다.

## 2. 용어

이 문서는 한 개념에 한 용어만 쓴다.

| 용어 | 뜻 |
|---|---|
| 원천 | Aside 가 만든 PDF, HTML, docx, 자막 원문이다. 아무도 수정하지 않는다. |
| 원천 폴더 | 원천을 두는 `raw/` 폴더다. git 에 넣지 않는다. |
| 요약 노트 | 원천 1개당 1개 만드는 markdown 파일이다. `notes/` 에 둔다. |
| 카드 | 원칙, 패턴, 프롬프트, 사례 중 1개를 담은 markdown 파일이다. `cards/` 에 둔다. |
| index | 모든 카드를 한 줄씩 나열한 `index.md` 다. Claude 가 가장 먼저 읽는다. |
| 기본 프롬프트 | 카드와 skill 을 쓰지 않은 짧은 프롬프트다. 영어로는 plain prompt 다. |
| 반감기 | 조언이 유효성을 잃는 데 걸리는 기간이다. 카드의 `half_life` 필드에 적는다. |
| T1, T2, T3 | 소스 신뢰 등급이다. T1 은 AI 플랫폼을 직접 만드는 사람과 공식 채널이다. T2 는 실험 결과를 공개하는 독립 실무자다. T3 는 요약·해설 채널이다. |
| frontmatter | markdown 파일 맨 위의 YAML 메타데이터 블록이다. |
| 피드 | 사이트의 새 글 목록을 기계가 읽는 형식이다. RSS 와 Atom 이 있다. |

## 3. 설계 원칙

1. **원천을 지킨다.** 요약은 다시 만들 수 있다. 원천과 원문 링크를 잃으면 요약을 다시 만들 수 없고 검증도 할 수 없다.
2. **카드는 작게 만든다.** 카드 1장에 원칙 1개만 쓴다. Claude 가 필요한 카드만 읽게 하기 위해서다.
3. **모든 카드에 유통기한을 붙인다.** Boris Cherny 는 2026-01 에 plan mode 로 시작하라고 권했다. 같은 Boris 는 2026-06 에 새 모델에는 계획 단계가 거의 필요 없다고 말했다.
4. **카드를 모델에게 강요하지 않는다.** 추천 프롬프트에는 카드 원문을 붙이지 않는다. 낡은 지시가 새 모델의 판단을 방해하기 때문이다.
5. **기본 프롬프트와 항상 비교한다.** 기본 프롬프트가 같거나 나으면, 그 카드를 재검토한다.
6. **필요할 때만 기능을 더한다.** 검색 서버, plugin, 자동화는 문제가 실제로 생길 때 더한다. Claude Code 공식 문서도 같은 순서를 권한다.

## 4. 스킬과 펠릭스의 경고

### 4.1 펠릭스가 실제로 한 말

AgentOS 정리 영상 자막에는 두 발언이 따로 있다.

- **15:29~15:36, 에이전트 역할에 대한 발언:** "등장인물들을 미리 정해 놓는 것처럼 접근하면 오히려 인공지능 활용에 제약을 두는 것 같다." 이 발언의 대상은 에이전트에게 정체성을 미리 정해 주는 방식이다. 펠릭스는 모델을 뛰어난 제너럴리스트로 본다.
- **17:45~18:26, 스킬에 대한 발언:** 펠릭스는 스킬을 "여전히 많이 사용한다". 다만 이전 세대 모델에 맞춘 지시가 들어가므로 좋은 스킬의 유효 기간이 짧다고 말했다. 때로는 스킬을 완전히 빼면 결과가 더 좋다. 그래서 "그냥 프롬프트만 보내 보라" 고 권했다.
- **16:39~16:52, 도구에 대한 발언:** 데이터가 많으면 도구를 준다. 각 도구가 어떤 데이터를 가져오는지 명확하게 설명한다.

따라서 "지식을 제한한다" 는 경고의 중심 대상은 역할 부여다. 스킬에 대한 경고의 중심은 낡은 지시다.

### 4.2 `/ref` 가 경고에 해당하는 범위

`/ref` 는 두 가지 일을 한다. 두 일은 경고에 해당하는 정도가 다르다.

| 기능 | 하는 일 | 경고 해당 여부 | 이유 |
|---|---|---|---|
| 찾기 | 사용자에게 카드와 원문 링크를 보여 준다. | 해당하지 않는다. | 독자가 사람이다. 작업 모델의 컨텍스트에 들어가지 않는다. 펠릭스가 권한 "데이터를 가져오는 도구" 와 같다. |
| 추천 | 카드를 근거로 작업 프롬프트를 쓴다. | 일부 해당한다. | 추천 프롬프트는 작업 모델에게 간다. 카드가 낡으면, 낡은 지시가 작업 모델에게 전달된다. |

추천 기능에는 아래 4가지 규칙을 둔다.

1. Claude 는 추천 프롬프트에 역할 문장을 넣지 않는다. 역할 문장이 모델의 활용 범위를 좁히기 때문이다.
2. Claude 는 추천 프롬프트에 목표, 이유, 원천 데이터 위치, 검증 방법만 넣는다.
3. Claude 는 기본 프롬프트를 항상 함께 낸다.
4. 사용자는 두 프롬프트를 새 세션에 붙여 넣는다. 카드 본문이 작업 세션의 컨텍스트를 차지하지 않게 하기 위해서다.

## 5. 저장 정책

### 5.1 git 에 넣는 것과 넣지 않는 것

| 대상 | git | 이유 |
|---|---|---|
| 요약 노트, 카드, index, log | 넣는다. | 텍스트다. 2개 문서의 요약 노트를 합쳐도 약 60 KB 다. |
| 스크립트, skill, 설계 문서 | 넣는다. | 다시 만들 수 없는 작업물이다. |
| PDF, HTML, docx | 넣지 않는다. | 2개 문서만으로 약 25 MB 다. git 이력에서 지우기 어렵다. |
| 이미지 | 넣지 않는다. | 원천 HTML 에서 스크립트로 다시 뽑을 수 있다. 2개 문서의 이미지는 약 7 MB 다. |
| 자막 원문 | 넣지 않는다. | 원천의 일부다. 영상마다 약 70 KB 이고 수가 계속 는다. |
| 로컬 웹페이지 `site/` | 넣지 않는다. | 스크립트로 다시 만든다. |

현재 저장소에는 커밋이 없다. 따라서 PDF 를 git 이력에서 지우는 작업은 필요 없다.

### 5.2 원천의 안전장치

원천 폴더는 git 밖에 있다. 그래서 디스크를 잃으면 원천도 잃는다. 아래 2가지로 이 위험을 줄인다.

1. 요약 노트의 frontmatter 에 원천 파일 이름, SHA-256 해시, 원본 영상 URL 을 적는다. 원천을 잃으면, 사용자는 원본 영상 URL 로 Aside 요약을 다시 만든다.
2. 사용자는 원천 폴더의 백업 방법을 1가지 정한다. 기본안은 Time Machine 이다. 다른 Mac 에서도 원천이 필요하면, 사용자는 원천 폴더를 Google Drive 나 iCloud Drive 로 옮기고 symlink 로 연결한다.

Git LFS 는 쓰지 않는다. 저장 용량 한도와 설정 관리 부담이 1인 운영에 맞지 않기 때문이다.

## 6. 폴더 구조

```text
ai-reference/
├── README.md           # 프로젝트 안내서. 영어. AUTO 블록은 자동 생성된다.
├── README.ko.md        # 프로젝트 안내서. 한국어 번역.
├── DESIGN.md           # 이 문서
├── CLAUDE.md           # 폴더 규칙과 작업 절차. 100줄 이내.
├── index.md            # 카드마다 1줄. Claude 가 가장 먼저 읽는다.
├── log.md              # 작업 기록. 줄을 추가만 한다.
├── .gitignore          # raw/, site/, .DS_Store 를 제외한다.
├── .githooks/pre-commit  # 커밋 전에 README 를 다시 만들고 검사한다.
├── .github/workflows/docs-check.yml  # GitHub 에서 같은 검사를 실행한다.
├── raw/                # 원천 폴더. git 제외.
│   └── 2026-10-26_agentos_delegate-to-claude/
│       ├── original.html
│       ├── original.pdf
│       ├── original.docx
│       ├── transcript.ko.txt
│       └── img/001.jpg
├── notes/              # 요약 노트. 원천 1개당 1개.
│   └── 2026-10-26_agentos_delegate-to-claude.md
├── cards/
│   ├── delegation/     # 맡기는 방식
│   ├── verification/   # 검증과 리뷰
│   ├── context/        # 컨텍스트, skill, CLAUDE.md
│   └── hr-automation/  # HR 업무 자동화 사례
├── prompts/            # 실제로 써서 효과를 확인한 프롬프트
├── sources/
│   └── feeds.md        # 추적할 사람과 피드 목록
├── inbox/              # 새로 발견한 자료. 분류 전 상태.
├── research/           # 딥리서치 노트와 보고서
├── scripts/
│   ├── html2md.py      # 원천 HTML 을 요약 노트 초안과 이미지로 바꾼다.
│   ├── update_docs.py  # README 의 AUTO 블록을 만들고 정합성을 검사한다.
│   ├── build_site.py   # 노트와 카드로 로컬 웹페이지를 만든다.
│   └── freshness.py    # review_by 가 지난 카드를 나열한다.
├── templates/
│   ├── aside-youtube.md  # YouTube 링크용 Aside 요청 템플릿
│   └── aside-article.md  # 글 링크용 Aside 요청 템플릿
├── site/               # 로컬 웹페이지. git 제외.
└── .claude/skills/
    ├── ref/SKILL.md    # 찾기와 추천
    └── aside/SKILL.md  # Aside 요청 프롬프트 생성
```

파일 이름 규칙은 `YYYY-MM-DD_<채널>_<주제>` 다. 날짜는 원본 영상의 게시일이다. 카테고리 폴더는 4개로 시작한다. 한 폴더의 카드가 10장을 넘으면, 그 폴더만 나눈다.

현재 파일은 아래와 같이 옮긴다.

| 현재 위치 | 새 위치 |
|---|---|
| `references/클로드에게_일을_맡기는_법_실무레퍼런스.pdf` | `raw/2026-10-26_agentos_delegate-to-claude/original.pdf` |
| `references/HR_AI_에이전트_실무_레퍼런스_왓츠인마이AI_ep03.pdf` | `raw/2026-10-28_wanted_hr-ai-agent-ep03/original.pdf` |
| `research_notes/`, `reports/` | `research/2026-10-29_지식베이스-설계/` |

## 7. 처리 흐름

새 영상 1개를 라이브러리에 넣는 절차는 다음과 같다.

1. 사용자가 Claude Code 에 `/aside <링크>` 를 입력한다. Claude 가 Aside 요청 프롬프트를 만든다. 11절을 따른다.
2. 사용자가 그 프롬프트를 Aside 에 붙여 넣고 요약을 받는다.
3. 사용자가 Claude 에게 "가져와줘" 라고 요청한다. Claude 가 Aside 결과물을 `raw/<slug>/` 에 복사한다. 7.1절을 따른다.
4. Claude 가 `scripts/html2md.py` 로 HTML 을 요약 노트 초안과 이미지로 바꾼다.
5. Claude 가 요약 노트 초안을 표준 형식으로 정리한다.
6. Claude 가 요약 노트에서 카드를 만든다.
7. Claude 가 `index.md` 에 카드를 1줄씩 더한다.
8. Claude 가 `log.md` 에 작업 기록 1줄을 더한다.
9. 사용자가 링크 수와 이미지 수를 원천과 비교한다.

Aside 작업을 지우면, Aside 세션 폴더의 원천도 함께 지워진다. 따라서 사용자는 3단계를 요약 직후에 한다.

### 7.1 Aside 에서 가져올 파일

Aside 는 작업마다 `~/.aside/u/0/sessions/<날짜>_<id>/` 폴더를 만든다. 파일 이름은 작업마다 다르다. 아래 표는 2026-10-29 의 세션 2개에서 확인한 이름이다.

| 가져올 것 | 세션 안 위치 | 프로젝트 안 위치 | 필요도 | 이유 |
|---|---|---|---|---|
| 원본 HTML | `tmp/reference.html`, `tmp/doc.html` | `raw/<slug>/original.html` | 필수 | 변환의 입력이다. 링크와 스크린샷을 모두 담는다. |
| 자막 원문 | `tmp/ko.txt`, `tmp/transcript_ko.txt`, `tmp/transcript.txt` | `raw/<slug>/transcript.ko.txt`, `transcript.en.txt` | 필수 | 요약을 다시 만들거나 발언을 검증할 때 쓴다. |
| 영상 메타데이터 | `tmp/repl-result-*.txt` 중 `"videoId"` 가 있는 파일 | `raw/<slug>/metadata.json` | 권장 | 영상 ID, 제목, 채널, 길이가 들어 있다. |
| PDF | `artifacts/*.pdf` | `raw/<slug>/original.pdf` | 보존 | 사람이 원본 모양을 볼 때 쓴다. |
| docx | `artifacts/*.docx` | `raw/<slug>/original.docx` | 선택 | HTML 이 있으면 다시 쓸 일이 거의 없다. |

아래 파일은 가져오지 않는다.

- `tmp/frames/`, `tmp/hi/`, `tmp/repl-display-*`: 스크린샷 중간 파일이다. 같은 이미지가 원본 HTML 안에 들어 있다.
- `tmp/pdfprev*`, `tmp/pdfpages`, `tmp/*sheet*.jpg`: PDF 미리보기 파일이다.
- `messages.jsonl`: Aside 대화 기록이다. 약 8 MB 이고 카드에 쓸 정보가 없다.

위 표는 `/aside` 를 쓰기 전에 만든 세션의 이름이다. `/aside` 가 만든 프롬프트를 쓰면, Aside 는 `artifacts/` 에 문서 ID 로 시작하는 고정 이름을 쓴다. 이름 규칙은 11.3절에 있다.

Claude 는 아래 순서로 세션 폴더를 찾는다.

1. Claude 가 `log.md` 에서 `requested` 상태인 문서 ID 를 읽는다.
2. Claude 가 `artifacts/<문서 ID>.*` 파일이 있는 세션 폴더를 찾는다.
3. 그 파일이 없으면, Claude 가 가장 최근 세션 폴더에서 위 표의 파일을 찾는다.
4. Claude 가 찾은 파일 목록을 사용자에게 보여 주고 복사한다.

이 동작은 2단계에서 `scripts/import_aside.py` 와 `ingest-reference` skill 로 고정한다.

PDF 만 남은 경우에는 3단계에서 `pymupdf` 를 쓴다. 이 방법은 링크를 잃는다. 그래서 Claude 는 PDF 의 링크를 따로 뽑아 붙인다. 원천 HTML 변환은 첫 번째 문서에서 링크 36개와 이미지 33장을 모두 살렸다.

스크립트는 `uv run` 으로 실행한다. 스크립트 안에 필요한 패키지를 적는다. 이렇게 하면 시스템 Python 에 패키지를 설치하지 않는다.

## 8. 로컬에서 보기

| 보려는 것 | 방법 | 준비 |
|---|---|---|
| Aside 원본 모양 그대로 | `open raw/<slug>/original.html` 또는 `original.pdf` | 없음. 원천 HTML 은 이미지를 안에 담은 단일 파일이다. |
| 라이브러리 전체 | Obsidian 에서 저장소 폴더를 vault 로 연다. | 없음. Obsidian 이 이미 설치되어 있다. |
| 웹페이지 | `uv run scripts/build_site.py` 를 실행하고 `open site/index.html` 을 실행한다. | 2단계에서 스크립트를 만든다. |
| 새 PDF | Chrome headless 로 `site/` 의 HTML 을 PDF 로 인쇄한다. | 2단계에서 `build_site.py` 에 옵션으로 넣는다. |

요약 노트의 이미지 링크는 `../raw/<slug>/img/001.jpg` 형식의 상대 경로다. 따라서 Obsidian 과 로컬 웹페이지에서는 이미지가 보인다. GitHub 웹에서는 이미지가 보이지 않는다. 텍스트와 타임스탬프 링크는 GitHub 웹에서도 그대로 읽힌다.

## 9. 파일 형식

### 9.1 요약 노트

```yaml
---
title: 클로드에게 일을 맡기는 법
doc_id: yt-gV0CtvIX5zk
doc_type: video-reference
source_url: https://www.youtube.com/watch?v=<id>
video_id: <id>
channel: AgentOS
speakers: [Felix Rieseberg]
published: 2026-10-26
duration: "43:36"
related_sources:            # 영상이 소개한 원 인터뷰와 원문 글
  - https://www.youtube.com/watch?v=<원 인터뷰 id>
  - https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/
summarized: 2026-10-29
summarizer: Aside
raw:
  dir: raw/2026-10-26_agentos_delegate-to-claude/
  html_sha256: <해시>
tags: [delegation, verification]
valid_as_of: 2026-10-29
---
```

섹션 순서는 다음과 같다: 한 줄 요약, TL;DR, 핵심 원칙, 사례·수치, 프롬프트 템플릿, 체크리스트, 타임스탬프 색인, 주의·한계, 출처.

형식 규칙은 다음과 같다.

- 타임스탬프는 항상 `[▶ mm:ss](https://www.youtube.com/watch?v=<id>&t=<초>s)` 로 쓴다.
- 프롬프트 템플릿은 항상 ```` ```text ```` 코드 블록에 넣는다.
- 내용이 없는 섹션은 머리글까지 지운다. 빈 머리글이 있으면 LLM 이 내용을 지어낼 수 있기 때문이다.
- 표 셀 안에 `|` 를 쓰지 않는다. `|` 가 표의 열을 깨기 때문이다.

### 9.2 카드

```yaml
---
id: grade-outside-session
title: 만든 세션이 아니라 바깥에서 채점한다
type: principle          # principle, pattern, prompt, case, anti-pattern 중 1개
scope: agent-task        # agent-task, api-output, both 중 1개
tags: [verification, review]
source_note: notes/2026-10-26_agentos_delegate-to-claude.md
source_url: "https://www.youtube.com/watch?v=<원 인터뷰 id>&t=<초>s"
author: Felix Rieseberg (Anthropic)
tier: T1                 # 발언자 기준으로 정한다.
source_date: 2026-10-20
valid_as_of: 2026-10-29
model_context: Claude Opus 5.5, Claude Code v2.1
half_life: long          # short 는 3개월, medium 은 12개월, long 은 원칙급
review_by: 2027-10-29
status: active           # active, needs-review, deprecated 중 1개
superseded_by:
---
## 원칙
## 언제 쓰나
## 프롬프트 문장
## 근거
## 지난 방식
```

- `source_url` 에는 원 발언의 위치를 적는다. 한국어 정리 영상은 T3 전달 채널이므로 `source_note` 로만 연결한다.
- `지난 방식` 섹션에는 폐기된 방식을 날짜와 함께 옮긴다. 지우지 않는다. 같은 실수를 반복하지 않기 위해서다.
- 카드에서도 내용이 없는 섹션은 머리글까지 지운다. 빈 머리글이 있으면 LLM 이 내용을 지어낼 수 있기 때문이다.
- 원 인터뷰의 시점을 아직 찾지 않았으면, `source_url` 에 원 인터뷰 URL 을 시점 없이 적는다. 근거 섹션에는 정리 영상의 타임스탬프를 달고, 그 사실을 주의 줄로 적는다.
- `half_life` 기간 값은 실증 근거가 없는 시작값이다. 사용자는 운영하면서 기간을 조정한다.

### 9.3 index 한 줄

```text
- [만든 세션이 아니라 바깥에서 채점한다](cards/verification/grade-outside-session.md): 적대적 리뷰어와 판사 세션으로 검증한다 · verification · review_by 2027-10-29
```

Claude 는 index 만 읽고도 카드의 주제와 만료 여부를 판단한다. 카드를 CLAUDE.md 에 `@import` 하지 않는다. import 한 파일은 매 요청에 함께 로드되어 컨텍스트 비용이 커지기 때문이다.

## 10. `/ref` skill

### 10.1 동작

| 입력 예 | 모드 | 결과 |
|---|---|---|
| `/ref 검증` | 찾기 | 맞는 카드 최대 5장의 제목, 요약, 원문 링크 |
| `/ref 추천 신규 입사자 퇴사 원인 분석 회의 자료` | 추천 | 추천 프롬프트 1개, 기본 프롬프트 1개, 적용 카드 목록 |

### 10.2 SKILL.md 초안

```markdown
---
name: ref
description: ai-reference 라이브러리에서 업무에 맞는 카드를 찾아 보여 주고, 요청하면 카드를 근거로 Claude 프롬프트를 추천한다. 사용자가 "레퍼런스 찾아줘", "이 일 어떻게 맡기지", "프롬프트 추천" 이라고 하거나 /ref 를 부를 때 쓴다.
argument-hint: "[찾을 말] 또는 [추천 작업 설명]"
---

## 찾기 모드

1. /Users/leeyoonsam/Documents/ai-reference/index.md 를 Read 한다.
2. $ARGUMENTS 와 맞는 카드를 최대 5장 고른다.
3. 카드마다 제목, 한 줄 요약, 원문 링크, review_by 를 보여 준다.
4. review_by 가 오늘보다 이전이면, 그 카드에 "재검증 필요" 를 붙인다.
5. 사용자가 요청할 때만 카드 본문을 Read 해서 보여 준다.

## 추천 모드

$ARGUMENTS 가 "추천" 으로 시작하면 이 모드를 쓴다.

1. 찾기 모드 1~4단계를 한다.
2. 고른 카드의 본문을 Read 한다.
3. 작업 설명에 목표나 데이터 위치가 없으면, 사용자에게 한 번에 1개씩 묻는다. 질문은 3개 이하로 한다.
4. 추천 프롬프트 1개를 쓴다. 프롬프트에는 목표, 이유, 원천 데이터 위치, 검증 방법만 넣는다.
5. 역할 문장을 넣지 않는다. 역할 문장은 모델의 활용 범위를 좁힌다.
6. 카드 원문을 붙이지 않는다. 카드의 원칙을 작업에 맞는 문장으로 바꿔 쓴다.
7. 카드를 쓰지 않은 기본 프롬프트 1개를 쓴다.
8. 적용한 카드 id 를 나열한다.
9. 두 프롬프트를 각각 새 세션에서 실행하라고 안내한다.
```

### 10.3 비교 기록

1. 사용자가 두 프롬프트의 결과를 비교한다.
2. 사용자가 `log.md` 에 결과 1줄을 남긴다. 예: `2026-11-02 compare | grade-outside-session | 추천 승`
3. 기본 프롬프트가 같거나 나으면, Claude 가 해당 카드의 `status` 를 `needs-review` 로 바꾼다.
4. 효과를 확인한 추천 프롬프트는 Claude 가 `prompts/` 에 저장한다.

`/ref` 는 처음에 이 저장소의 project skill 로 만든다. 다른 업무 저장소에서도 필요하면, 사용자는 skill 을 `~/.claude/skills/ref/` 로 옮긴다.

## 11. Aside 요청 프롬프트 생성: `/aside`

### 11.1 필요한 이유

두 PDF 의 형식 차이는 Aside 가 요약을 만드는 단계에서 생겼다. 첫 번째 문서는 링크 36개를 가진다. 두 번째 문서는 링크가 0개이고 타임스탬프가 평문이다. 따라서 변환 도구를 바꿔도 형식은 통일되지 않는다. Aside 에게 주는 요청을 통일해야 한다.

`/aside` 는 링크 1개를 받아 Aside 요청 프롬프트를 만든다. 이 방식은 Aside 사용자 skill 보다 아래 4가지가 낫다.

- **규칙 원본이 1곳이다.** 형식 규칙은 저장소의 `templates/` 에만 있다. Aside 사용자 skill 을 쓰면 같은 규칙을 저장소 밖에서 따로 관리해야 한다.
- **확인되지 않은 기능에 기대지 않는다.** Aside 가 사용자 skill 을 자동으로 고르는지는 확인하지 않았다. 붙여 넣은 프롬프트는 Aside 가 반드시 읽는다.
- **링크별 정보를 넣는다.** Claude 는 링크 종류, 영상 ID, 문서 ID 를 프롬프트에 채운다.
- **가져오기가 정확해진다.** Aside 가 문서 ID 로 파일 이름을 붙인다. 그래서 Claude 가 세션 폴더를 추측하지 않는다.

### 11.2 동작

1. 사용자가 `/aside <링크>` 를 입력한다.
2. Claude 가 링크 종류를 `youtube` 와 `article` 중 하나로 정한다.
3. Claude 가 문서 ID 를 만든다. YouTube 는 `yt-<영상 ID>` 다. 글은 `web-<도메인>-<경로 마지막 부분>` 이다.
4. Claude 가 `log.md` 와 `notes/` 에서 같은 문서 ID 를 찾는다.
5. 같은 문서 ID 가 있으면, Claude 가 "이미 있음" 을 알리고 멈춘다.
6. Claude 가 `templates/aside-<종류>.md` 를 Read 한다.
7. Claude 가 템플릿에 링크와 문서 ID 를 채운다.
8. Claude 가 완성된 프롬프트를 코드 블록 1개로 보여 준다.
9. Claude 가 `pbcopy` 로 프롬프트를 클립보드에 복사한다.
10. Claude 가 `log.md` 에 `requested` 줄을 더한다. 예: `2026-10-30 requested | yt-gV0CtvIX5zk | https://www.youtube.com/watch?v=gV0CtvIX5zk`
11. 사용자가 프롬프트를 Aside 에 붙여 넣는다.

가져오기를 마치면, Claude 는 `log.md` 에 `ingested` 줄을 더한다. 최종 폴더 이름은 `YYYY-MM-DD_<채널>_<주제>` 다. Claude 는 이 이름을 `metadata.json` 의 게시일과 채널로 만든다. 문서 ID 는 요약 노트의 `doc_id` 필드에 남긴다.

### 11.3 YouTube 템플릿 초안

이 템플릿은 프로젝트 원칙을 따른다. 역할 문장을 넣지 않는다. 목표와 이유, 원천, 검증 기준을 준다.

```text
아래 YouTube 영상을 실무 레퍼런스 문서로 정리해 줘.

링크: {{url}}
문서 ID: {{doc_id}}

[목적]
이 문서는 내 레퍼런스 라이브러리의 원천이 된다. 나중에 Claude 가 이 문서에서 원칙 카드를 만든다.
그래서 형식이 일정해야 하고, 모든 주장을 영상의 시점으로 확인할 수 있어야 한다.

[내용]
1. 핵심 내용을 정리하고 중요한 장면의 스크린샷을 넣어 줘.
2. 섹션 순서: 한 줄 요약, TL;DR, 핵심 원칙, 사례와 수치, 프롬프트 템플릿, 체크리스트, 타임스탬프 색인, 주의와 한계, 출처.
3. 내용이 없는 섹션은 머리글까지 빼 줘.
4. 이 영상이 다른 인터뷰나 글을 정리한 영상이면, 원 인터뷰와 원문 글의 링크를 찾아 출처에 적어 줘.

[형식]
- 타임스탬프는 모두 [▶ mm:ss] 링크로 걸어 줘. 주소는 {{url}}&t=<초>s 형식이다.
- 스크린샷 바로 아래에 장면 설명 1줄과 타임스탬프 링크를 달아 줘.
- 프롬프트 템플릿은 원문 그대로 코드 블록에 넣어 줘.
- 표 셀 안에 | 를 쓰지 말아 줘.
- 영상에 없는 수치나 인용을 만들지 말아 줘. 불확실한 내용은 주의와 한계에 적어 줘.

[저장] artifacts 폴더에 아래 이름으로 저장해 줘.
1. {{doc_id}}.pdf : 스크린샷을 포함한 정리 문서
2. {{doc_id}}.html : PDF 를 만든 HTML 원본
3. {{doc_id}}.transcript.ko.txt : 자막 원문 전체. 줄마다 [mm:ss] 를 붙인다.
4. {{doc_id}}.metadata.json : video_id, url, title, channel, published, duration, related_sources

[마지막 보고]
저장한 파일 4개의 이름, 타임스탬프 링크 수, 스크린샷 수를 알려 줘.
```

마지막 보고의 링크 수와 스크린샷 수는 검증 기준이다. Claude 는 가져오기 후 같은 수를 다시 센다. 두 수가 다르면 Claude 가 사용자에게 알린다.

### 11.4 글 링크

글 템플릿 `templates/aside-article.md` 는 YouTube 템플릿과 아래 4가지가 다르다.

- 타임스탬프 대신 원문 문단의 인용과 원문 링크로 근거를 단다.
- 스크린샷 대신 글 속 그림을 넣는다.
- 자막 원문 대신 글 본문 전체를 `{{doc_id}}.source.md` 로 저장한다.
- 메타데이터는 url, title, author, site, published, related_sources 다.

그림이 필요 없는 글은 Aside 를 거치지 않는다. Claude 가 글을 직접 가져와서 `raw/` 에 저장한다. 단계를 줄이기 위해서다.

### 11.5 Aside 사용자 skill

Aside 사용자 skill 은 지금 만들지 않는다. 규칙을 두 곳에서 관리하게 되기 때문이다. `/aside` 프롬프트를 매번 붙여 넣기가 불편해지면, 그때 사용자 skill 을 검토한다. 등록 위치는 `~/.aside/u/0/skills/user/<name>/SKILL.md` 다. skill 초안은 연구 보고서에 있다.

## 12. 흐름 추적

### 12.1 소스 선정 기준

1. 라이브러리에는 T1 과 T2 의 원문만 카드 근거로 쓴다.
2. T3 채널은 새 자료를 발견하는 데만 쓴다. T3 요약은 원문과 다를 수 있다. 같은 Boris 스레드를 다룬 2차 글들은 팁 개수를 10개, 13개, 22개, 53개로 다르게 셌다.
3. 사용자의 두 PDF 도 이 기준을 따른다. 첫 번째 PDF 는 Felix 인터뷰를 AgentOS 가 정리하고, 그 영상을 Aside 가 다시 요약한 문서다.

### 12.2 시작 소스

| 등급 | 소스 | 추적 방법 |
|---|---|---|
| T1 | Claude Code 변경 이력 | 피드 `https://code.claude.com/docs/en/changelog/rss.xml` |
| T1 | Claude Platform 릴리스 노트 | 피드 `https://platform.claude.com/docs/en/release-notes/feed.xml` |
| T1 | Anthropic Engineering 블로그 | 제3자 대체 피드 Olshansk/rss-feeds |
| T1 | Claude 블로그 | 제3자 대체 피드 Olshansk/rss-feeds |
| T1 | Felix Rieseberg | 피드 `https://www.felixrieseberg.com/rss` |
| T1 | Boris Cherny, Cat Wu, Thariq Shihipar | X 를 주 1회 직접 확인한다. |
| T2 | Simon Willison | 피드 `https://simonwillison.net/tags/claude-code.atom` |
| T2 | Ethan Mollick | 피드 `https://www.oneusefulthing.org/feed` |
| T2 | Latent Space | 피드 `https://www.latent.space/feed` |
| T3 | AgentOS, 원티드 왓츠인마이AI | YouTube 구독. 발견용이다. |

X 의 무료 RSS 경로는 2026-09 에 사라졌다. Nitter 와 XCancel 이 모두 중단됐다. 따라서 Boris 같은 X 중심 빌더는 자동으로 추적하지 않는다. 빌더의 기능 발표는 결국 공식 변경 이력에 들어간다. 그래서 변경 이력 피드가 X 를 대신하는 주 신호다. 전체 소스 25명의 목록은 `research/2026-10-29_지식베이스-설계/notes/source_map_and_tracking.md` 에 있다.

### 12.3 분류 라벨

| 라벨 | 뜻 | Claude 의 행동 |
|---|---|---|
| `NEW` | 라이브러리에 없는 개념이다. | 카드 초안을 만든다. |
| `UPDATE` | 기존 카드의 사실을 바꾼다. | 영향받는 카드 경로와 근거 1문장을 쓴다. |
| `STALE?` | 변경 이력이 카드의 기능 이름을 언급한다. | 카드 `status` 를 `needs-review` 로 바꾼다. |
| `DUP` | 기존 카드와 같은 내용이다. | 원문이 더 1차 자료이면 출처만 바꾼다. |
| `SKIP` | 마케팅, 채용, 무관한 주제다. | 아무것도 하지 않는다. |

## 13. 반감기 관리

1. 사용자는 월 1회 `uv run scripts/freshness.py` 를 실행한다. 이 스크립트는 `review_by` 가 지난 카드를 나열한다.
2. 새 모델이 출시되면, Claude 가 `half_life: short` 카드를 추천 프롬프트와 기본 프롬프트로 각각 실행한다.
3. 사용자가 두 결과를 비교한다.
4. 기본 프롬프트가 같거나 나으면, 사용자가 카드 `status` 를 `deprecated` 로 바꾼다.
5. 사용자는 분기마다 `/doctor prompt-audit` 로 CLAUDE.md 와 skill 의 낡은 지시를 찾는다. 이 명령은 Claude Code v2.1.283 이상에서 동작한다.

라이브러리의 성공 지표는 카드 수가 아니다. 성공 지표는 재검증한 카드의 비율과 폐기한 카드의 수다.

## 14. 단계별 계획

### 14.1 1단계: 오늘

1. Claude 가 `.gitignore` 를 만든다.
2. Claude 가 Aside 세션 폴더의 HTML, docx, 자막 원문을 `raw/` 로 복사한다.
3. Claude 가 `references/` 의 PDF 2개를 `raw/` 로 옮긴다.
4. Claude 가 `research_notes/` 와 `reports/` 를 `research/` 로 옮긴다.
5. Claude 가 `scripts/html2md.py` 를 만든다.
6. Claude 가 원천 HTML 2개를 요약 노트 2개로 바꾼다.
7. Claude 가 두 번째 문서의 평문 타임스탬프를 영상 ID `IrK71LslbFQ` 기반 링크로 바꾼다.
8. Claude 가 첫 번째 요약 노트에서 원칙 카드 7~12장을 만든다.
9. Claude 가 두 번째 요약 노트에서 사례 카드 3~5장을 만든다.
10. Claude 가 `CLAUDE.md`, `index.md`, `log.md` 를 만든다.
11. Claude 가 `.claude/skills/ref/SKILL.md` 를 만든다.
12. Claude 가 `templates/aside-youtube.md` 와 `.claude/skills/aside/SKILL.md` 를 만든다.
13. 사용자가 링크 수와 이미지 수를 확인한다.
14. 사용자가 실무 작업 1개로 `/ref 추천` 을 시험한다.
15. 사용자가 새 영상 1개로 `/aside` 를 시험한다.
16. 사용자가 첫 커밋을 승인한다.

### 14.2 2단계: 2주 안

1. 사용자가 실무 작업마다 `/ref` 를 쓴다.
2. 사용자가 비교 결과를 `log.md` 에 남긴다.
3. 사용자가 `/aside` 로 받은 Aside 결과가 표준 형식인지 확인한다.
4. Claude 가 결과를 보고 `templates/aside-youtube.md` 를 고친다. 그리고 `templates/aside-article.md` 를 만든다.
5. Claude 가 `scripts/import_aside.py`, `scripts/build_site.py`, `scripts/freshness.py` 를 만든다.
6. Claude 가 `sources/feeds.md` 를 만든다.
7. 사용자가 T1 피드를 피드 리더에 넣고 주 1회 확인한다.

### 14.3 3단계: 1~3개월

1. Claude 가 피드 수집 스크립트를 만든다. 이 스크립트는 새 항목만 `inbox/` 에 쓴다.
2. 사용자가 주 1회 Claude 에게 `inbox/` 분류를 요청한다.
3. 수집이 안정되면, Claude 가 GitHub Actions 일일 수집을 만든다.
4. 사용자가 Claude Code 예약 작업으로 일일 분류를 만든다. 예약 작업은 허용 목록 밖 사이트를 막는다. 그래서 수집은 GitHub Actions 가 맡고, 분류만 예약 작업이 맡는다.
5. Claude 가 `ingest-reference` skill 을 만든다. 이 skill 은 7절의 3~7단계를 한 번에 한다.

### 14.4 조건이 생길 때만 하는 확장

- 카드가 수백 장을 넘으면, 사용자는 검색 서버를 검토한다.
- 피플팀 동료와 함께 써야 하면, 사용자는 plugin 배포를 검토한다.
- 다른 기기에서 원천이 필요하면, 사용자는 원천 폴더를 클라우드 드라이브로 옮긴다.

## 15. 확인하지 않은 사항

- `half_life` 기간 값은 실증 근거가 없다.
- Aside 가 사용자 skill 을 자동으로 고르는지 확인하지 않았다.
- YouTube 채널 RSS 가 사용자 Mac 에서 동작하는지 확인하지 않았다. 연구 환경에서는 404 를 반환했다.
- skill 을 symlink 로 연결하는 방식은 동작을 확인하지 않았다.
- Boris Cherny 의 2026-10 현재 소속은 확인하지 않았다.
- 펠릭스 발언의 타임스탬프는 AgentOS 정리 영상 기준이다. 원 인터뷰의 타임스탬프는 아직 찾지 않았다.

## 16. 문서 자동화

README 는 `README.md` 와 `README.ko.md` 2개다. 영어가 원본이고 한국어가 번역이다.

1. `scripts/update_docs.py` 가 두 README 의 AUTO 블록 6개를 저장소 내용으로 다시 쓴다. 블록은 stats, layout, sources, cards, skills, scripts 다.
2. `.githooks/pre-commit` 이 커밋마다 1번을 실행하고 README 를 stage 한다.
3. 같은 hook 이 `update_docs.py --check` 를 실행한다. 검사가 실패하면 커밋이 멈춘다.
4. GitHub Actions `docs-check` 가 push 와 pull request 마다 같은 검사를 실행한다.

검사 항목은 5개다. AUTO 블록의 최신 여부, 두 README 의 머리글 구조, 최상위 항목의 설명 유무, 카드와 `index.md` 의 일치, 스크립트 docstring 의 영어·한국어 줄이다. 서술 부분은 자동으로 만들지 않는다. 설계나 구현 파일만 바뀐 커밋에서 hook 이 확인 알림을 출력한다.

## 17. 결정 기록

| 날짜 | 결정 | 이유 |
|---|---|---|
| 2026-10-29 | 원천 파일을 git 에 넣지 않는다. | 용량이 크고 git 이력에서 지우기 어렵다. |
| 2026-10-29 | 원천 HTML 을 변환의 1순위 입력으로 쓴다. | PDF 변환은 링크를 잃는다. HTML 변환은 링크와 이미지를 모두 살린다. |
| 2026-10-29 | skill 은 `/ref` 와 `/aside` 2개로 시작한다. | `/ref` 는 찾기와 추천을 한 명령으로 쓴다. `/aside` 는 입력 형식을 통일한다. 공식 문서도 기능을 하나씩 더하라고 권한다. |
| 2026-10-29 | 추천에는 기본 프롬프트를 항상 붙인다. | 펠릭스와 Anthropic 문서가 모두 낡은 skill 의 위험을 경고한다. |
| 2026-10-29 | 검색 서버와 RAG 는 쓰지 않는다. | 원천 100개 규모까지는 index 파일로 충분하다. |
| 2026-10-29 | Aside 형식은 `/aside` 가 만드는 요청 프롬프트로 통일한다. Aside 사용자 skill 은 보류한다. | 규칙 원본을 저장소 1곳에 둔다. Aside 의 skill 자동 선택은 확인되지 않았다. |
| 2026-10-29 | README 는 영어 원본과 한국어 번역 2개로 둔다. 숫자, 표, 목록은 `update_docs.py` 가 만든다. pre-commit hook 과 GitHub Actions 가 같은 검사를 실행한다. | 사람이 문서 갱신을 잊어도 구현과 문서가 어긋나지 않게 한다. 머리글 구조 비교로 번역 누락을 잡는다. |
