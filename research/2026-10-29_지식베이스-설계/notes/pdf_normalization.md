# AI 생성 한국어 PDF 요약의 정규화와 Aside 출력 표준화 (2026-10-29 기준)

용어 정의
- **A 문서**: `references/클로드에게_일을_맡기는_법_실무레퍼런스.pdf`. 24 페이지다.
- **B 문서**: `references/HR_AI_에이전트_실무_레퍼런스_왓츠인마이AI_ep03.pdf`. 15 페이지다.
- **원본 HTML**: Aside 가 PDF 를 인쇄하기 전에 만든 HTML 파일이다.
- **실측**: 이 연구자가 scratchpad 의 사본으로 직접 돌려 본 결과다. 실측 출력은 `/private/tmp/claude-501/-Users-leeyoonsam-Documents-ai-reference/99ff6306-dff2-4a3e-827d-62a155338d2a/scratchpad/pdftest/` 아래에 있다.
- `references/` 의 원본 파일은 수정하거나 옮기지 않았다.

## 1. "Aside" 는 무엇인가. 커스텀 프롬프트·템플릿·내보내기를 지원하는가

### Takeaway
Aside 는 Aside Computer 가 만든 Chromium 기반 로컬 우선 AI 브라우저다. 이 회사는 YC Fall 2025 배치 출신이다. 공식 문서는 템플릿이나 커스텀 지시 기능을 설명하지 않는다. 그러나 로컬 설치본에는 사용자 스킬 기능(`skills/user/<name>/SKILL.md`)이 있다. 이 스킬이 미래 요약을 원천에서 표준화하는 가장 확실한 수단이다.

### Cited Findings
- Aside 는 크로미움 기반 AI 브라우저다. AI 가 로그인된 사이트에서 페이지를 읽고, 클릭하고, 입력한다. 도움말 주소는 `docs.aside.com` 이다. — [디지털마케터: 에이사이드 브라우저란](https://www.digitalmarketer.co.kr/class/coding-agents-basics/what-is-aside-browser)
- 이용약관상 제작사는 샌프란시스코의 Aside Computer 다. 한국인 3명이 창업했고 YC Fall 2025 배치다. 출시일은 2026-06-23 으로 소개된다. 이 정보는 검색 결과 요약에서 나왔고, 원문 약관은 직접 확인하지 않았다. — [디지털마케터: Aside 리뷰](https://www.digitalmarketer.co.kr/insights/aside-browser-review); [moge.ai](https://moge.ai/ko/product/aside)
- Aside 는 공개 가격표가 없다. 사용자가 자기 AI 구독이나 API 키를 연결하는 bring-your-own-model 방식이다. 메모리는 기기에 저장된 일반 markdown 파일이다. 사용자가 이 파일을 열어 고칠 수 있다. 이 리뷰는 커스텀 프롬프트·템플릿·Notion/Obsidian 연동·YouTube 요약을 언급하지 않는다. — [eesel.ai: Aside AI browser review (2026)](https://eesel.ai/blog/aside-ai-browser-review)
- 공식 문서 목차: Get started, Tasks, Side panel, Ultrabrowse, Automation(루틴), Memory, Password Manager, AI 설정, Privacy, Security, Developers(CLI·MCP·REPL), Changelog. 공식 문서는 skills, custom instructions, templates, markdown/HTML/PDF 내보내기를 언급하지 않는다. — [docs.aside.com](https://docs.aside.com)
- Task 상세 화면은 task 가 만들거나 바꾼 파일을 보여 준다. 이미지·PDF·HTML·텍스트 파일을 미리 볼 수 있다. 생성 파일은 사용자가 task 나 그 폴더를 지울 때까지 남는다. 각 task 는 작업 폴더를 가진다. — [docs.aside.com/help/tasks](https://docs.aside.com/help/tasks)
- 메모리는 `Settings > Memory` 에서 보고 고친다. 에피소드 메모리 보존 기간은 "Never forget", "30 days", "90 days" 중에서 고른다. — [docs.aside.com/help/memory](https://docs.aside.com/help/memory)
- CLI 설치 명령은 `curl -fsSL https://releases.aside.com/install.sh | bash` 다. 프롬프트로 task 를 시작하는 명령은 `aside "<프롬프트>"` 다. `aside mcp` 는 Aside 를 MCP(Model Context Protocol) 서버로 노출한다. 따라서 Claude Code 가 Aside 를 도구로 부를 수 있다. — [docs.aside.com/help/developers](https://docs.aside.com/help/developers)
- 로컬 실측: 계정 루트는 `~/.aside/u/0/` 이다. 그 아래에 `memory/`, `sessions/`, `skills/builtin/`, `agents/`, `backups/` 가 있다. — 로컬 경로 `file:///Users/leeyoonsam/.aside/u/0/`
- 로컬 실측: 내장 스킬 목록에 `youtube`, `pdf`, `docx`, `pptx`, `xlsx`, `notion`, `google-docs`, `skill-creator`, `visualize`, `draft-preview` 가 있다. `youtube` 스킬은 `youtube.getMetadata()`, `youtube.getTranscript()`, `youtube.getComments()` 를 제공한다. — `file:///Users/leeyoonsam/.aside/u/0/skills/builtin/youtube/SKILL.md`
- 로컬 실측: 내장 `skill-creator` 스킬은 사용자 스킬 경로를 `<accountRoot>/skills/user/<skill-name>/SKILL.md` 로 정한다. frontmatter 는 `name` 과 `description` 만 쓴다. 문자열 값은 큰따옴표로 감싼다. 이 스킬의 설명은 "reusable instructions, … templates" 를 계정 스킬로 바꾸는 용도라고 밝힌다. — `file:///Users/leeyoonsam/.aside/u/0/skills/builtin/skill-creator/SKILL.md`
- 로컬 실측: `aside` 내장 스킬은 Projects API(`aside.projects.list()`)와 task 의 `projectId` 를 다룬다. — `file:///Users/leeyoonsam/.aside/u/0/skills/builtin/aside/SKILL.md`

### Inferences
- 사용자가 부르는 "Aside(어사이드)" 는 위 제품이라고 높은 확신으로 판단한다. 근거는 3가지다. 로컬에 `~/.aside` 와 `~/Library/Application Support/Aside` 가 있다. 두 PDF 가 Aside 세션 폴더의 `artifacts/` 에 같은 파일명·같은 바이트 크기로 있다. Aside 는 Chromium 기반이므로 PDF Creator 가 "Chrome/153" 으로 찍힌다.
- PDF 제목이 "about:blank" 인 이유를 추정한다. Aside 에이전트가 HTML 을 빈 탭에 넣고 Chrome 인쇄로 PDF 를 만들었을 가능성이 높다. 원본 HTML 에 `<title>` 태그가 없다는 실측도 이 추정과 맞는다.
- Aside 에는 "모든 요약에 이 형식을 쓴다" 를 강제하는 공식 설정 화면이 없다. 대신 3가지 수단이 있다. 첫째는 사용자 스킬이다. 둘째는 메모리 파일에 선호를 적는 방법이다. 셋째는 매번 붙여 넣는 지시 프롬프트다. 스킬이 가장 재현성이 높다. Aside 는 스킬을 `description` 으로 자동 선택하기 때문이다.
- `notion` 내장 스킬이 있으므로 Aside 가 Notion 에 직접 저장할 수 있을 가능성이 있다. 이 기능은 검증하지 않았다.

### Gaps
- 공식 문서에서 사용자 스킬·Project 지시문(instructions) 기능의 설명을 찾지 못했다. 사용자 스킬 경로는 로컬 내장 스킬 문서로만 확인했다.
- Aside 가 사용자 스킬을 실제로 자동 로드하는지는 실행해서 검증하지 않았다.
- Obsidian 연동은 어떤 출처에도 없다. markdown 파일을 Obsidian vault 폴더에 쓰는 방식은 가능하다고 추정한다. 이 방식은 Aside 의 Guard 권한에서 그 폴더를 승인해야 한다.

## 2. PDF 대신 원본 HTML/markdown 을 얻을 수 있는가

### Takeaway
얻을 수 있다. 그리고 이미 디스크에 있다. 두 PDF 모두 원본 HTML·.docx 가 Aside 세션 폴더에 남아 있다. A 문서는 한국어 자막 원문 `ko.txt` 도 남아 있다. 원본 HTML 을 markdown 으로 바꾸면 링크·표·이미지·굵은 글씨가 거의 손실 없이 보존된다. 세션 폴더를 지우면 이 파일도 사라진다. 따라서 사용자는 이 파일을 빨리 별도 폴더로 복사해야 한다.

### Cited Findings
- 로컬 실측: A 문서 세션은 `~/.aside/u/0/sessions/2026-10-29_xdB7AcOPjBgbupPS/` 다. `artifacts/` 에 같은 이름의 `.pdf`(2,921,923 바이트, references 사본과 같은 크기)와 `.docx` 가 있다. `tmp/` 에 `reference.html`(2.3 MB), `ko.txt`(71 KB, `[mm:ss - mm:ss] 자막` 형식), `frames/`(영상 프레임 캡처)가 있다. — `file:///Users/leeyoonsam/.aside/u/0/sessions/2026-10-29_xdB7AcOPjBgbupPS/`
- 로컬 실측: B 문서 세션은 `~/.aside/u/0/sessions/2026-10-29_mv5Ybyf4W44B89rA/` 다. `artifacts/` 에 `.pdf`(6,631,366 바이트, 사본과 같은 크기)와 `.docx` 가 있다. `tmp/` 에 `doc.html`(7.7 MB), `frames/`, `hi/` 가 있다. 이 세션에는 자막 텍스트 파일이 없다. — `file:///Users/leeyoonsam/.aside/u/0/sessions/2026-10-29_mv5Ybyf4W44B89rA/`
- 로컬 실측: 원본 HTML 의 구성은 아래와 같다. 이미지는 모두 base64 `data:image/jpeg` URI 로 HTML 안에 박혀 있다.
  - A `reference.html`: `<h1>/<h2>` 13개, `<table>` 4개, `<a href>` 36개, `<img>` 33개.
  - B `doc.html`: `<h1>/<h2>` 10개, `<table>` 4개, `<a href>` 0개, `<img>` 43개.
  - 근거 파일: `file:///Users/leeyoonsam/.aside/u/0/sessions/2026-10-29_xdB7AcOPjBgbupPS/tmp/reference.html`, `file:///Users/leeyoonsam/.aside/u/0/sessions/2026-10-29_mv5Ybyf4W44B89rA/tmp/doc.html`
- 생성 파일은 사용자가 task 나 그 폴더를 지울 때까지 남는다. — [docs.aside.com/help/tasks](https://docs.aside.com/help/tasks)
- 로컬 실측: 원본 HTML 을 `BeautifulSoup` + `markdownify` 로 바꾸는 20줄 스크립트를 만들었다. 이 스크립트는 base64 이미지를 파일로 풀고 상대 경로로 바꾼다. A 결과는 링크 36/36, 이미지 33/33, heading 40개, 표 행 24개다. 표는 깨지지 않았다. 캡션은 `*캡션* [▶ 43:19](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=2599s)` 형태로 남는다. — 스크립트 `file:///private/tmp/claude-501/-Users-leeyoonsam-Documents-ai-reference/99ff6306-dff2-4a3e-827d-62a155338d2a/scratchpad/pdftest/html2md.py`, 결과 `…/pdftest/html/A.md`, `…/pdftest/html/B.md`
- 로컬 실측: HTML 변환에도 남는 결함은 3가지다.
  - B 문서 첫 표의 셀에 제목 문자 `|` 가 있다. 이 문자가 escape 되지 않아 표 열이 하나 늘어난다.
  - 프롬프트 템플릿이 코드 블록이 아니다. 굵은 제목 1줄과 `<br>` 줄바꿈 문단으로 나온다. 원본 HTML 에 `<pre>`/`<code>` 가 0개이기 때문이다.
  - B 문서는 원본 HTML 에도 링크가 없다. URL 은 표 안의 평문이고, 타임스탬프는 `[11:00]` 같은 평문 캡션 43개다.
- 로컬 실측: `markitdown` 0.1.9 는 `.docx` 를 빈 출력(0 바이트)으로 바꿨다. `markitdown[docx]` extra 를 설치하지 않았기 때문일 가능성이 높다. .docx 경로는 더 시험하지 않았다. — `…/pdftest/html/A.docx.md`

### Inferences
- 두 문서의 구조 차이는 PDF 변환에서 생긴 것이 아니다. 생성 단계에서 생겼다. A 는 타임스탬프마다 링크를 걸었다. B 는 같은 Aside 로 만들었지만 링크를 하나도 걸지 않았다. 따라서 변환 도구만 바꿔서는 일관성을 얻을 수 없다. 원천 지시(3절의 스킬·프롬프트)가 필요하다.
- 기존 2개 문서의 최선 경로는 "원본 HTML → markdown 변환 → LLM 1회 정규화" 다. LLM 정규화는 frontmatter 추가, 표준 섹션 재배치, 프롬프트 템플릿의 코드 블록화, B 타임스탬프의 링크화를 맡는다. B 의 링크는 영상 ID `IrK71LslbFQ` 와 `[mm:ss]` 를 `&t=<초>s` 로 바꾸면 기계적으로 만들 수 있다.
- `ko.txt` 같은 자막 원문은 요약보다 가치가 오래간다. 요약을 다시 만들거나 검증할 때 원문이 필요하기 때문이다. 사용자는 이 파일을 요약 md 옆에 함께 보관하는 것이 좋다.

### Gaps
- Aside 가 세션 폴더를 자동 정리하는지, 정리 주기가 있는지 확인하지 못했다.
- B 세션에 자막 원문 파일이 없는 이유를 확인하지 못했다. Aside 가 메모리 안에서만 자막을 썼을 수 있다.

## 3. 2026년 한국어 PDF → markdown 도구 비교 (표·링크·이미지 보존)

### Takeaway
원본 HTML 이 있으면 PDF 변환 도구는 필요 없다. PDF 만 남은 경우에는 `pymupdf4llm`(PyMuPDF 2.0 내장) layout 모드가 구조를 가장 잘 살린다. 다만 이 모드는 링크를 버리고 일부 한국어 캡션의 띄어쓰기를 지운다. 그래서 링크는 `page.get_links()` 로 따로 뽑아 붙여야 한다. Claude 의 PDF 읽기는 사람이 읽듯 요약·재구성하는 데 좋다. 그러나 링크 URL 을 받는다는 문서 근거는 없다.

### Cited Findings
- 로컬 환경: `pdftotext`, `pdftohtml`, `pdfimages`, `pdfinfo` 가 `/opt/homebrew/bin` 에 있다. Python 3.13.5 와 `uv` 가 있다. `marker`, `docling`, `markitdown`, `pandoc` 는 전역 설치되어 있지 않다. 시험용 패키지는 scratchpad 의 venv 에만 설치했다. — 로컬 `which` 결과
- 로컬 실측: PDF 자체의 링크 상태는 아래와 같다.
  - A PDF 에는 URI link annotation 이 36개 있다. 예: `https://www.youtube.com/watch?v=gV0CtvIX5zk&t=2599s`.
  - B PDF 에는 link annotation 이 0개다.
  - A 는 이미지 34개, B 는 이미지 44개다. 대부분 1280×720 JPEG 다.
  - 근거: `pdfimages -list`, PyMuPDF `page.get_links()` 실측.
- 로컬 실측: `pymupdf4llm` 2.0 은 빈 껍데기 패키지다. 이 패키지의 METADATA 는 "The pymupdf-2.x package now contains the 4llm code" 라고 밝힌다. 그래서 2026-10 기준으로는 `pip install pymupdf` 를 해야 `import pymupdf4llm` 이 동작한다. — venv 의 `pymupdf4llm-2.0.dist-info/METADATA`
- 로컬 실측 비교표 (A 문서 기준, B 는 괄호):

| 방법 | Korean 띄어쓰기 | heading | 표 | 링크 | 이미지 | 비고 |
|---|---|---|---|---|---|---|
| 원본 HTML + markdownify | 정상 | 40 (54) | 정상, 셀 병합 없음 | 36/36 (원본에 0) | 33/33 파일 추출 | 최선. B 표의 `\|` escape 만 필요 |
| `pymupdf4llm` layout 모드(기본값) | 캡션 일부 손실 ("가져갈방향네가지") | 45 (62) | 대체로 정상, 셀 줄바꿈은 `<br>`. 일부 표는 행이 쪼개짐 | 0 | 34 (47) 파일 추출 | 24 페이지 5.1초, CPU. 페이지 꼬리말 "… \| 1 / 24" 가 남음 |
| `pymupdf4llm` legacy 모드 (`use_layout(False)`) | 캡션 일부 손실 | 14 | 첫 표 머리글 깨짐 | 34/36. 1개는 잘못 병합 ("[인터뷰 · 블로그](…D-SVFneJ_Nk)") | 옵션 | 빈 줄 과다 |
| `markitdown` 0.1.9 (pdfminer) | 정상 | 1 (0) | 여러 줄 셀이 조각 표로 깨짐 | 0 | 0 | 텍스트 확인용으로만 적합 |
| `pdftotext -layout` | 정상 | 없음 | 공백 정렬 텍스트 | 0 | 0 | 표는 사람이 읽을 수 있으나 LLM 파싱에 약함 |
| `pdftohtml -s -i` | 정상 | 없음 | 절대 좌표 span | 35 href 보존 | 제외(-i) | 텍스트가 span 단위로 쪼개짐 ("정리 영" + "상") |

  - 근거 출력: `…/pdftest/A.pymupdf.md`, `A.pymupdf_legacy.md`, `A.markitdown.md`, `A.layout.txt`, `A.pdftohtml.html`, `html/A.md`. B 도 같은 이름 규칙이다.
- 로컬 실측: 프롬프트 템플릿 박스는 PDF 계열 도구 어디에서도 코드 블록으로 나오지 않았다. 모두 일반 문단으로 나왔다. — `…/pdftest/A.pymupdf.md` 122행 부근
- 2026년 비교 글들은 단일 승자가 없다고 본다. MarkItDown 은 깨끗한 디지털 PDF, Docling 은 표·수식·다단 학술 문서, Marker 는 GPU 가 있고 정확도가 중요할 때를 권한다. 이 글들은 공통 코퍼스의 재현 가능한 벤치마크를 싣지 않는다. 일부는 변환 서비스 업체의 마케팅 글이다. — [The Menon Lab: Best Open-Source PDF-to-Markdown Tools in 2026](https://themenonlab.blog/blog/best-open-source-pdf-to-markdown-tools-2026); [dev.to: markitdown vs docling vs marker](https://dev.to/dmaxdev/markitdown-vs-docling-vs-marker-pdf-to-markdown-for-llms-571o); [file2markdown: pymupdf4llm vs docling](https://www.file2markdown.ai/blog/pymupdf4llm-vs-docling)
- Docling 은 설치가 무겁고 GPU 없이 느리다는 평가가 있다. Marker 는 `--use_llm` 옵션으로 LLM 보정을 더한다. 이 옵션은 지연과 API 비용을 늘린다. PyMuPDF4LLM 은 빠르고 로컬에서 돌지만 스캔 문서는 처리하지 못한다. — [file2markdown: docling alternatives](https://www.file2markdown.ai/blog/docling-alternatives); [The Menon Lab](https://themenonlab.blog/blog/best-open-source-pdf-to-markdown-tools-2026)
- Claude PDF 지원은 각 페이지를 이미지로 바꾸고, 페이지 텍스트를 추출해 이미지와 함께 준다. 요청당 최대 600 페이지다. context window 가 1M 토큰 미만이면 100 페이지다. 요청 크기 한도는 1st-party API 에서 128 MB 다. 텍스트 비용은 페이지당 보통 1,500–3,000 토큰이다. 이미지 비용은 별도다. — [Claude Docs: PDF support](https://platform.claude.com/docs/en/build-with-claude/pdf-support)
- Claude PDF 지원 문서는 hyperlink 나 link annotation 처리를 언급하지 않는다. — [Claude Docs: PDF support](https://platform.claude.com/docs/en/build-with-claude/pdf-support)

### Inferences
- 이 사용자의 PDF 는 모두 Chrome 인쇄 PDF 다. 즉 텍스트 레이어가 있는 디지털 PDF 다. 따라서 OCR·GPU 를 쓰는 Marker·Docling 의 강점이 거의 필요 없다. 설치 비용(PyTorch, 모델 내려받기)만 크다. 2개 문서를 위해 이 도구를 설치하는 것은 권하지 않는다. 이 판단은 로컬에서 Marker·Docling 을 돌려 보지 않은 추정이다.
- PDF 만 남은 경우의 권장 파이프라인은 아래와 같다.
  1. `pymupdf4llm.to_markdown(path, write_images=True, image_path=…)` 를 layout 모드로 실행한다.
  2. `page.get_links()` 로 URI 와 링크 사각형을 뽑는다.
  3. 각 `▶ mm:ss` 캡션을 같은 URI 의 markdown 링크로 바꾼다. 매칭 키는 `t=<초>s` 와 캡션의 `mm:ss` 다.
  4. 페이지 꼬리말 `<문서명> | n / N` 줄을 정규식으로 지운다.
  5. Claude 에게 결과 md 와 원본 PDF 를 함께 주고, 4절 템플릿으로 재구성하게 한다. Claude 는 PDF 이미지로 띄어쓰기·표 구조를 교차 확인할 수 있다.
- Claude 에 PDF 만 주면 "▶ 43:19" 텍스트는 보이지만 URL 은 잃을 가능성이 높다. 따라서 링크가 필요한 문서는 링크 목록을 텍스트로 함께 줘야 한다.
- 24 페이지 A 문서를 Claude 에 PDF 로 넣으면 텍스트만 약 36K–72K 토큰이 든다. 이 값은 페이지당 1,500–3,000 토큰으로 계산한 추정이다. 같은 내용의 HTML 변환 md 는 18 KB 다. 따라서 지식베이스에는 md 를 저장하고 PDF 는 보존용으로만 두는 것이 비용 면에서 낫다.

### Gaps
- Marker 와 Docling 은 로컬에서 시험하지 않았다. 두 도구의 한국어 띄어쓰기·링크 보존 품질은 확인하지 못했다.
- Marker·Docling·MarkItDown 의 2026-10 최신 버전 번호와 라이선스를 1차 출처(GitHub)에서 확인하지 못했다.
- `pymupdf4llm` layout 모드에 링크를 출력하는 옵션이 있는지 확인하지 못했다. `to_markdown` 시그니처가 `(*args, **kwargs)` 라서 옵션 목록을 볼 수 없었다.
- `pymupdf4llm` 이 RapidOCR 미설치 경고를 냈다. 텍스트 PDF 결과에는 영향이 없었다.

## 4. 표준 요약 템플릿과 Aside 지시 프롬프트

### Takeaway
표준 형식은 "YAML frontmatter + 고정 섹션 순서 + 고정 타임스탬프 링크 문법" 으로 정한다. 사용자는 이 형식을 Aside 사용자 스킬로 등록한다. 등록이 안 되면 매 요청에 지시 프롬프트를 붙인다. 출력 1순위는 `.md` 파일이다. PDF·docx 는 필요할 때만 같은 md 에서 만든다.

### Cited Findings
- Aside 사용자 스킬은 `<accountRoot>/skills/user/<skill-name>/SKILL.md` 에 둔다. 이 사용자의 accountRoot 는 `~/.aside/u/0` 이다. frontmatter 는 `name`·`description` 만 쓰고 값은 큰따옴표로 감싼다. 트리거 정보는 `description` 에 쓴다. 본문은 절차형으로 짧게 쓴다. 검증 명령은 `node <skill-creator-dir>/scripts/validate-frontmatter.mjs <path>/SKILL.md` 다. — `file:///Users/leeyoonsam/.aside/u/0/skills/builtin/skill-creator/SKILL.md`
- Aside `youtube` 스킬은 메타데이터(제목, 채널, 길이, 게시일, 설명)와 자막을 직접 가져온다. 따라서 frontmatter 의 대부분을 Aside 가 사실값으로 채울 수 있다. — `file:///Users/leeyoonsam/.aside/u/0/skills/builtin/youtube/SKILL.md`
- 기존 두 문서는 이미 일부 공통 요소를 가진다. 둘 다 메타 정보 표, TL;DR 또는 "한눈에 보기", 이미지 캡션 + 타임스탬프를 쓴다. 그러나 타임스탬프 문법이 다르다. A 는 `▶ mm:ss` 링크, B 는 `[mm:ss]` 평문이다. — 로컬 실측 `…/pdftest/html/A.md`, `…/pdftest/html/B.md`

### Inferences

#### 4-1. 표준 템플릿 (`<slug>.md`)

파일 이름 규칙 제안: `YYYY-MM-DD_<채널-slug>_<주제-slug>.md`. 날짜는 영상 게시일이다. 이미지는 `assets/<파일 이름과 같은 slug>/NNN.jpg` 에 둔다.

````markdown
---
title: "클로드에게 일을 맡기는 법"
doc_type: video-reference          # 고정값
source_url: "https://www.youtube.com/watch?v=gV0CtvIX5zk"
video_id: "gV0CtvIX5zk"
channel: "AgentOS"
speakers: ["Felix Rieseberg (Anthropic)"]
published: 2026-10-26
duration: "43:36"
related_sources:                   # 원본 인터뷰, 인용 글
  - title: "Claude Engineering Lead: \"Stop Using Claude Like It's 2024\""
    url: "https://www.youtube.com/watch?v=D-SVFneJ_Nk"
summarized: 2026-10-29
summarizer: "Aside"                # 도구 이름
summarizer_model: ""               # Aside 에 연결한 모델. 모르면 빈 값
transcript: auto-generated         # auto-generated | manual | none
language: ko
tags: [claude, prompting, agent]
valid_as_of: 2026-10-26            # 내용이 유효한 기준일. 보통 게시일
review_by: 2027-04-26              # 다시 확인할 날짜. 기본 6개월 뒤
---

# {제목}

> 한 줄 요약: {영상 전체를 한 문장으로}

## TL;DR
- {핵심 3~7개. 한 항목 한 문장}

## 핵심 원칙
### 1. {원칙 이름}
- 주장: {무엇을 하라}
- 근거: {영상 속 근거} [▶ mm:ss](https://www.youtube.com/watch?v={id}&t={초}s)
- 실무 적용: {구체 행동 1개}

## 사례·수치               <!-- 사례가 없으면 섹션 삭제 -->
| 사례 | 문제 | 해법 | 효과 | 시점 |
|---|---|---|---|---|

## 프롬프트 템플릿
### {템플릿 이름}
- 용도: {언제 쓰나}
```text
{그대로 복사해 쓸 프롬프트 원문}
```

## 체크리스트
- [ ] {바로 실행할 행동}

## 타임스탬프 색인
| 시점 | 장면 |
|---|---|
| [▶ 04:21](https://www.youtube.com/watch?v={id}&t=261s) | {장면 설명} |

## 주의·한계
- {자동 자막 오인식 가능성, 화자의 주관적 주장, 유효 기간이 짧은 내용}

## 출처
- 영상: [{제목}]({source_url})
- {관련 글·원본 인터뷰}
````

템플릿 결정 근거
- frontmatter 는 Obsidian·정적 사이트·LLM 검색 필터가 모두 읽는다. 따라서 메타 정보 표 대신 frontmatter 를 쓴다.
- 타임스탬프는 항상 `[▶ mm:ss](…&t=<초>s)` 로 쓴다. 이 문법은 사람에게 클릭 링크이고, 기계에게 정규식 키다.
- 프롬프트 템플릿은 항상 ```` ```text ```` 코드 블록에 둔다. 그래야 변환·복사 중 줄바꿈과 따옴표가 깨지지 않는다.
- 표 셀 안에 `|` 문자를 쓰지 않는다. B 문서에서 이 문자가 표를 깼다.
- 섹션 순서는 고정한다. 내용이 없는 섹션은 지운다. 빈 머리글을 남기면 LLM 이 그 섹션에 내용을 지어낼 수 있다.

#### 4-2. Aside 사용자 스킬 초안

위치: `~/.aside/u/0/skills/user/youtube-reference-md/SKILL.md`. 이 연구자는 이 파일을 만들지 않았다. 사용자가 직접 만들거나 Aside 에게 "skill-creator 로 이 스킬을 등록해 줘" 라고 요청한다.

````markdown
---
name: "youtube-reference-md"
description: "Use when the user asks to summarize, 정리, or make a 실무 레퍼런스 from a YouTube video. Produces one standard Korean markdown file with YAML frontmatter, fixed sections, and timestamp links."
---

# YouTube 실무 레퍼런스 (표준 markdown)

1. `youtube.getMetadata()` 로 제목·채널·게시일·길이를 가져온다. 추측하지 않는다.
2. `youtube.getTranscript()` 로 한국어 자막을 가져온다. 없으면 원어 자막을 가져온다.
3. 자막 원문을 `<slug>.transcript.txt` 로 저장한다. 형식은 `[mm:ss] 텍스트` 다.
4. 아래 "형식 규칙" 에 따라 `<slug>.md` 를 쓴다.
5. 슬라이드·화면 캡처는 `assets/<slug>/NNN.jpg` 파일로 저장한다. base64 로 박지 않는다.
6. 사용자가 PDF 나 docx 를 요청할 때만, 완성한 md 를 렌더링해서 만든다.
7. 마지막에 저장한 파일 경로 목록을 보고한다.

## 형식 규칙
- 파일 이름: `YYYY-MM-DD_<channel-slug>_<topic-slug>.md`. 날짜는 게시일이다.
- frontmatter 키와 순서: title, doc_type(video-reference), source_url, video_id, channel, speakers, published, duration, related_sources, summarized, summarizer("Aside"), summarizer_model, transcript, language(ko), tags, valid_as_of, review_by.
- 섹션 순서: 한 줄 요약 → TL;DR → 핵심 원칙 → 사례·수치 → 프롬프트 템플릿 → 체크리스트 → 타임스탬프 색인 → 주의·한계 → 출처. 내용이 없는 섹션은 머리글까지 지운다.
- 타임스탬프는 항상 `[▶ mm:ss](https://www.youtube.com/watch?v=<id>&t=<초>s)` 로 쓴다.
- 이미지 아래 캡션은 `*<장면 설명>* [▶ mm:ss](…)` 한 줄로 쓴다.
- 프롬프트 템플릿 원문은 항상 ```text 코드 블록에 넣는다.
- 체크리스트는 `- [ ]` 로 쓴다.
- 표 셀 안에서 `|` 를 쓰지 않는다. 필요하면 `/` 로 바꾼다.
- 영상에 없는 수치·인용을 만들지 않는다. 불확실하면 "주의·한계" 에 적는다.
````

#### 4-3. 붙여 넣기용 지시 프롬프트 (스킬을 쓰지 않을 때)

```text
이 YouTube 영상을 한국어 실무 레퍼런스로 정리해 줘. 결과는 markdown 파일 1개로 저장해 줘.

[저장]
- 파일 이름: YYYY-MM-DD_<채널>_<주제>.md (날짜는 영상 게시일)
- 이미지는 assets/<파일이름>/NNN.jpg 파일로 따로 저장하고 md 에서 상대 경로로 링크해. base64 로 넣지 마.
- 자막 원문은 <파일이름>.transcript.txt 로 함께 저장해.
- PDF·docx 는 내가 따로 요청할 때만 만들어.

[frontmatter: 파일 맨 위 YAML]
title, doc_type: video-reference, source_url, video_id, channel, speakers, published, duration, related_sources, summarized(오늘 날짜), summarizer: "Aside", summarizer_model, transcript(auto-generated|manual|none), language: ko, tags, valid_as_of(게시일), review_by(게시일+6개월)
- 메타데이터는 YouTube 에서 직접 가져와. 추측하지 마.

[본문 섹션: 이 순서 고정, 내용이 없으면 머리글까지 삭제]
1. 한 줄 요약 (인용 블록 >)
2. ## TL;DR (3~7개 불릿, 한 항목 한 문장)
3. ## 핵심 원칙 (원칙마다 주장 / 근거+타임스탬프 / 실무 적용)
4. ## 사례·수치 (표: 사례 | 문제 | 해법 | 효과 | 시점)
5. ## 프롬프트 템플릿 (템플릿마다 용도 1줄 + ```text 코드 블록에 원문)
6. ## 체크리스트 (- [ ] 형식)
7. ## 타임스탬프 색인 (표: 시점 | 장면)
8. ## 주의·한계 (자막 오인식, 화자의 주관, 유효 기간)
9. ## 출처

[문법 규칙]
- 타임스탬프는 항상 [▶ mm:ss](https://www.youtube.com/watch?v=<id>&t=<초>s) 형식으로 링크해.
- 이미지 캡션은 이미지 바로 아래 한 줄: *장면 설명* [▶ mm:ss](링크)
- 표 셀 안에 | 문자를 쓰지 마.
- 영상에 없는 수치나 인용을 지어내지 마. 불확실하면 주의·한계에 적어.
```

#### 4-4. 기존 2개 문서의 이관 절차
1. 사용자가 두 세션 폴더의 `tmp/*.html`, `tmp/ko.txt`, `artifacts/*.docx` 를 지식베이스의 원천 보관 폴더로 복사한다.
2. 사용자가 `html2md.py` 로 각 HTML 을 md 와 이미지 폴더로 바꾼다.
3. 사용자가 Claude 에게 변환된 md 와 4-1 템플릿을 주고 재구성을 요청한다.
4. Claude 는 B 의 `[mm:ss]` 평문을 `video_id` 기반 링크로 바꾼다.
5. Claude 는 "프롬프트 템플릿" 문단을 `text` 코드 블록으로 옮긴다.
6. 사용자가 링크 수와 이미지 수를 원본 HTML 과 비교한다. 기대값은 A 링크 36·이미지 33, B 이미지 43 이다.

### Gaps
- 사용자 스킬이 실제로 트리거되는지, Aside 가 md 를 artifacts 폴더에 저장하는지 실행해 보지 않았다.
- Aside 의 Project 기능에 프로젝트 단위 지시문을 넣을 수 있는지 확인하지 못했다. 가능하면 스킬보다 범위를 좁게 적용할 수 있다.

## 5. 이미지(슬라이드 캡처)를 보존할 것인가

### Takeaway
보존하되 md 밖의 파일로 둔다. 캡션과 타임스탬프 링크는 반드시 텍스트로 남긴다. LLM 검색·요약에서는 캡션 텍스트가 정보를 운반한다. 이미지는 사람이 다시 볼 때와 나중에 vision 모델로 재분석할 때를 위한 보조 자료다.

### Cited Findings
- 로컬 실측: 원본 HTML 에서 푼 이미지 용량은 A 33장 1.7 MB, B 43장 5.6 MB 다. 변환된 md 텍스트는 A 18 KB, B 12 KB 다. — `…/pdftest/html/A_img`, `…/pdftest/html/B_img`
- 로컬 실측: `pymupdf4llm` 의 `write_images=True` 도 A 34장, B 47장을 파일로 뽑았다. `pdfimages -list` 는 A 34장(1280×720 JPEG)을 보고했다. — `…/pdftest/img_A`, `…/pdftest/img_B`
- Claude PDF 처리는 각 페이지를 이미지로 넣는다. 그래서 그래픽이 많은 PDF 는 page 한도 전에 context 를 채울 수 있다. 문서는 큰 파일에 대해 embedded image downsampling 을 권한다. — [Claude Docs: PDF support](https://platform.claude.com/docs/en/build-with-claude/pdf-support)
- A 문서의 캡션은 슬라이드 내용을 이미 요약한다. 예: "구조는 세 겹: 공격 클로드 ×5 → 판사 클로드 → 만든 클로드". — 로컬 실측 `…/pdftest/html/A.md` 187행

### Inferences
- 선택지별 판단은 아래와 같다.
  - **선택지 1: base64 로 md 안에 박기.** 권하지 않는다. md 가 MB 단위로 커진다. LLM 에 md 를 넣을 때 쓸모없는 토큰이 대량으로 들어간다.
  - **선택지 2: `assets/<slug>/` 파일 + 상대 경로 링크.** 권장한다. Obsidian·GitHub 미리보기에서 보인다. LLM 수집기는 `![](…)` 줄을 무시하거나 캡션만 읽는다.
  - **선택지 3: 이미지를 버리고 캡션 + 타임스탬프만 남기기.** 저장 공간이 중요할 때의 대안이다. 타임스탬프 링크가 있으면 원 장면을 언제든 다시 볼 수 있다. B 처럼 링크가 없는 문서는 먼저 링크를 만들어야 이 선택지가 안전하다.
- 이미지 추출에는 원본 HTML 의 base64 를 푸는 방법이 가장 정확하다. 캡션과 순서가 1:1 로 맞기 때문이다. PDF 만 있으면 `pymupdf4llm write_images=True` 가 md 내 위치까지 맞춰 준다. `pdfimages -j` 는 위치 정보를 주지 않는다.
- 슬라이드에 캡션보다 많은 정보(표, 코드)가 있으면 캡션을 보강해야 한다. 그 경우 Claude 에게 이미지를 보여 주고 "슬라이드의 텍스트를 캡션 아래 인용 블록으로 옮겨 줘" 라고 요청한다.

### Gaps
- 이미지 저작권·재배포 문제는 조사하지 않았다. 개인 지식베이스 용도라면 문제가 작다고 추정하지만, 공유 저장소에 올리기 전에는 확인이 필요하다.
