# 레퍼런스를 카드로 쪼개고 유통기한을 붙여라

이 프로젝트는 PDF 보관함으로 설계하지 않는다. 유통기한이 붙은 원칙 카드 라이브러리로 설계한다. 구조는 수정하지 않는 원천 폴더, 원칙 1개당 markdown 카드 1장, Claude 가 먼저 읽는 `index.md` 1개다. 프롬프트 추천은 `/recommend-prompt` skill 1개로 시작한다. 이 skill 은 카드 3–5장을 읽는다. 그리고 카드를 적용한 프롬프트와 카드 없는 plain prompt 를 함께 낸다.

plain prompt 를 함께 내는 이유는 위임 조언의 반감기가 실제로 짧기 때문이다. Boris Cherny 는 2026-01 에 "plan mode 부터 시작한다" 를 권했다. 같은 Boris 는 2026-06 에 새 모델은 planning step 이 거의 필요 없다고 말했다. PDF 형식 문제는 변환 도구로 풀지 않는다. 원천 단계에서 푼다. 두 PDF 의 원본 HTML 은 지금 Aside 세션 폴더에 남아 있다. 사용자는 오늘 이 파일을 복사하고, 카드를 만들고, skill 1개를 만든다. 피드 자동 추적과 Aside 표준 요약 skill 은 그다음 단계다.

## 용어

이 보고서는 아래 용어를 한 가지 뜻으로만 쓴다.

| 용어 | 뜻 |
|---|---|
| 원천 | Aside 가 만든 PDF·HTML·자막 원문이다. 사용자도 Claude 도 수정하지 않는다. |
| 요약 노트 | 원천 1개당 1개 만드는 markdown 파일이다. 표준 형식을 따른다. |
| 카드 | 원칙·패턴·프롬프트·사례 1개를 담은 markdown 파일이다. |
| `index.md` | 모든 카드를 한 줄씩 나열한 목록이다. Claude 가 가장 먼저 읽는다. |
| skill | Claude Code 나 Aside 가 필요할 때 읽는 절차 문서다. `SKILL.md` 파일 1개로 시작한다. |
| frontmatter | markdown 파일 맨 위의 YAML 메타데이터 블록이다. |
| 반감기 | 조언이 유효성을 잃는 데 걸리는 기간이다. 카드의 `half_life` 필드에 적는다. |
| 피드 | 사이트의 새 글 목록을 기계가 읽는 형식이다. RSS 와 Atom 이 있다. |
| T1·T2·T3 | 소스 신뢰 등급이다. T1 은 플랫폼 빌더와 공식 채널, T2 는 1차 실험을 공개하는 독립 실무자, T3 는 요약·해설 채널이다. |
| LLM | 대형 언어 모델이다. Claude 가 여기에 든다. |

## 위임 조언은 9개월 사이에 뒤집혔다

Boris Cherny 의 조언 변화가 반감기의 가장 선명한 증거다. Boris 는 Claude Code 를 만든 사람이다. 2026-01-02 스레드에서 Boris 는 plan mode 로 시작하고, Claude 가 틀릴 때마다 CLAUDE.md 에 규칙을 더하라고 했다 ([Boris X 2026-01-02](https://x.com/bcherny/status/2007179832300581177)). 2026-06-08 회고에서 Boris 는 auto mode 가 plan mode 를 대체한다고 말했다. 2차 요약 사이트는 이 발언을 "don't actually need a planning step" 으로 전한다 ([Boris X 2026-06-08](https://x.com/bcherny/status/2064034799711588805), [howborisusesclaudecode.com](https://howborisusesclaudecode.com/)). 2026-07-08 에 Boris 의 `/checkup` 은 Boris 자신의 설정에서 **미사용 project skill 38개**와 **매 세션 로드되는 약 10k 토큰의 CLAUDE.md** 를 찾았다 ([Boris X 2026-07-08](https://x.com/bcherny/status/2074997571563479143)).

Anthropic 의 공식 입장도 같은 방향으로 움직였다. Thariq Shihipar 는 Claude 5 세대 모델용 Claude Code 시스템 프롬프트에서 **80% 이상을 지웠고 코딩 평가 손실이 없었다**고 썼다 ([Thariq 블로그 2026-07-24](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/)). Fable 5 공식 문서는 "Skills developed for prior models are often too prescriptive for Claude Fable 5 and can degrade output quality" 라고 쓴다 ([Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)). 사용자의 Felix PDF 도 같은 경고를 담는다. 196행은 "좋은 스킬의 반감기는 짧다" 이고, 근거 타임스탬프는 ▶ 19:43 이다 ([로컬 PDF](file:///Users/leeyoonsam/Documents/ai-reference/references/클로드에게_일을_맡기는_법_실무레퍼런스.pdf)).

이 주장의 출처에는 주의가 필요하다. Felix 블로그 원문은 skill 반감기를 다루지 않는다. 블로그 원문은 능력이 "every couple of weeks" 바뀐다고만 말한다 ([Felix 블로그 2026-10-13](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)). 따라서 반감기 주장은 인터뷰 발언에서 나왔을 가능성이 높다. 카드는 이 주장의 출처로 인터뷰 영상의 타임스탬프를 적는다. 블로그를 출처로 적지 않는다.

모든 시기에 바뀌지 않은 원칙도 있다. 그 원칙은 **Claude 가 스스로 검증할 수단을 준다** 이다. Boris 는 이 원칙이 품질을 "2-3x" 올린다고 했다 ([InfoQ](https://infoq.com/news/2026/01/claude-code-creator-workflow/)). Fable 5 문서는 "Separate, fresh-context verifier subagents tend to outperform self-critique" 라고 쓴다 ([Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)). Karpathy 는 LLM 이 "automate what you can verify" 한다고 정리했다 ([Karpathy Sequoia Ascent 2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/)). Felix 는 "Do _not_ ask the model to judge itself" 라고 썼다 ([Felix 블로그](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)).

여러 출처를 합치면 실무 공식 1개가 나온다. 공식은 "목표와 이유는 넓게 준다. 지시는 짧게 준다. 맥락은 원천 그대로 준다. 종료 조건과 검증은 세션 밖에 둔다." 이다. 아래 표는 이 공식을 반감기별로 나눈다. 기간 값은 실증 데이터가 없는 제안값이다. 사용자는 운영하면서 기간을 조정한다.

| 반감기 | 원칙 예 | 근거 |
|---|---|---|
| long | 검증 수단을 준다. 만든 세션이 채점하지 않게 한다. | [Boris](https://x.com/bcherny/status/2007179832300581177), [Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5), [Felix](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) |
| long | 요청만 주지 않고 이유를 준다. | [Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) |
| medium | CLAUDE.md 는 짧게 쓰고 함정만 적는다. | [Thariq](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/) |
| medium | 코딩 전에 모호한 점을 한 번에 하나씩 묻게 한다. | [Thariq X 2026-07-03](https://x.com/trq212/status/2073100352921215386) |
| short | plan mode 로 먼저 시작한다. | [Boris 2026-01](https://x.com/bcherny/status/2007179832300581177) 에서 권장, [Boris 2026-06](https://x.com/bcherny/status/2064034799711588805) 에서 약화 |
| short | `/goal`, `/checkup`, "use a workflow" 같은 명령·트리거 이름 | [Boris X 2026-05](https://x.com/bcherny/status/2053982327123132846), [howborisusesclaudecode.com](https://howborisusesclaudecode.com/) |
| 폐기 | prefill, `budget_tokens`, 추론을 본문에 쓰라는 지시 | [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), [Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) |

일부 원칙은 출처끼리 충돌한다. 공식 문서는 출력 형식을 맞출 때 예시 3–5개와 한 줄 역할 부여를 여전히 권한다 ([Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). Thariq 는 예시가 에이전트의 탐색 공간을 좁힌다고 쓴다 ([Thariq](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/)). Felix 는 역할극을 피하고 전문가가 "하는 일" 을 시키라고 쓴다 ([Felix](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)). 두 입장은 적용 층위가 다르다. 그러므로 카드에 `scope` 필드를 두고 `api-output` 과 `agent-task` 를 구분한다.

## 원천·카드·index 3층이면 원천 100개까지 검색 인프라가 필요 없다

라이브러리 구조는 Karpathy 의 LLM wiki 패턴을 따른다. 이 패턴은 수정하지 않는 원천, LLM 이 유지하는 markdown 페이지, 구조 규칙을 적은 CLAUDE.md 의 3층으로 이루어진다 ([Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)). 작업은 3가지다. Ingest 는 새 원천을 페이지로 통합한다. Query 는 index 를 먼저 읽고 관련 페이지만 연다. Lint 는 모순과 낡은 주장을 정기 점검한다. Karpathy 는 원천 약 100개, 페이지 수백 개 규모에서 index 파일만으로 "surprisingly well" 동작한다고 썼다. 사용자의 규모는 이 범위 안에 있으므로 vector DB 와 검색 서버는 지금 필요 없다.

Claude Code 의 로딩 방식도 이 구조를 지지한다. CLAUDE.md 는 매 요청에 전체가 들어간다. skill 은 설명만 상시 로드되고 본문은 사용할 때 로드된다 ([Extend Claude Code](https://code.claude.com/docs/en/features-overview)). 공식 문서는 **CLAUDE.md 를 200줄 미만**으로 유지하라고 권한다. `@import` 는 비용을 줄이지 않는다. 문서 원문은 "imported files load together with the CLAUDE.md that imports them" 이다 ([Memory](https://code.claude.com/docs/en/memory)). 따라서 카드를 CLAUDE.md 에 import 하지 않는다. 카드가 늘수록 매 요청 비용이 커지기 때문이다.

Anthropic 의 context engineering 글은 파일 경로를 "lightweight identifiers" 로 들고 있다가 필요할 때 읽으라고 권한다. 같은 글은 폴더 계층, 이름 규칙, 날짜를 Claude 가 읽는 신호로 본다 ([Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). 그래서 파일 이름에 날짜를 앞에 붙인다. 카드는 Claude 가 열기 전까지 컨텍스트 비용이 0이다. 아래는 시작용 폴더 구조다.

```text
ai-reference/
├── CLAUDE.md          # 폴더 규칙, 카드 형식, ingest·query·lint 절차. 100줄 이내.
├── index.md           # 카드마다 1줄. Claude 가 가장 먼저 읽는다.
├── log.md             # 작업 기록. 줄을 추가만 한다. 예: "2026-10-29 ingest | felix"
├── references/        # 원천. 수정하지 않는다.
│   ├── 2026-10-26_agentos_delegate-to-claude/
│   │   ├── original.pdf
│   │   ├── reference.html
│   │   └── transcript.ko.txt
│   └── 2026-10-28_wanted_hr-ai-agent/
│       ├── original.pdf
│       └── doc.html
├── notes/             # 요약 노트. 원천 1개당 1개. 표준 형식.
│   ├── 2026-10-26_agentos_delegate-to-claude.md
│   └── assets/2026-10-26_agentos_delegate-to-claude/001.jpg
├── cards/
│   ├── delegation/
│   ├── verification/
│   ├── context-and-skills/
│   └── hr-automation/
├── prompts/           # 실제로 써서 효과를 확인한 프롬프트
├── scripts/           # html2md.py, freshness.py
└── .claude/skills/
    └── recommend-prompt/SKILL.md
```

사용자는 처음에 카테고리 폴더를 4개만 만든다. 한 폴더의 카드가 10장을 넘으면, 그 폴더만 나눈다. 아래는 카드 frontmatter 형식이다. `model_context` 와 `review_by` 가 이 형식의 핵심 필드다. 새 모델이 나오면 Claude 가 `model_context` 로 영향받는 카드를 grep 한다. Claude 는 `review_by` 로 만료된 카드를 찾는다.

```yaml
---
id: skill-half-life-try-plain-prompt
title: 스킬은 금방 낡는다. 스킬 없는 프롬프트와 비교한다
type: principle          # principle | pattern | prompt | case | anti-pattern
scope: agent-task        # agent-task | api-output | both
tags: [skills, model-upgrade]
source_note: notes/2026-10-26_agentos_delegate-to-claude.md
source_url: "https://www.youtube.com/watch?v=<원 인터뷰 id>&t=<초>s"
author: Felix Rieseberg (Anthropic)
tier: T1                 # 발언자 기준. 전달 채널 기준이 아니다.
source_date: 2026-10-20
valid_as_of: 2026-10-29
model_context: Claude Opus 5.5 / Claude Code v2.1.x
half_life: short         # short=3개월 | medium=12개월 | long=원칙급
review_by: 2027-01-29
status: active           # active | needs-review | deprecated
superseded_by:
---
## 원칙
## 언제 쓰나
## 프롬프트 문장
## 근거
## Old patterns
```

본문의 `Old patterns` 섹션은 Anthropic skill 작성 지침에서 가져왔다. 이 지침은 낡은 방식을 지우지 않고, 폐기 날짜를 붙여 별도 섹션에 접으라고 권한다 ([Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)). `index.md` 의 한 줄 형식은 llms.txt 규칙을 빌린다 ([llmstxt.org](https://llmstxt.org/)). 형식은 `- [제목](cards/…/id.md): 한 줄 요약 · tags · review_by` 다. Claude 는 `index.md` 만 읽어도 만료 여부를 안다.

| 선택지 | 장점 | 단점 | 판단 |
|---|---|---|---|
| CLAUDE.md 에 카드 전부 `@import` | 설정이 가장 쉽다. | 매 요청에 전체 비용이 든다. | 쓰지 않는다. |
| 카드 파일 + `index.md` + skill 1개 | 읽기 전 비용이 0이다. git 과 Obsidian 이 둘 다 읽는다. | 사용자가 ingest 습관을 유지해야 한다. | **시작점** |
| 위 구성 + 개인 skill | 다른 업무 저장소에서도 쓴다. | skill 이 절대 경로에 의존한다. | 2주 안에 전환 |
| Plugin 배포 | 여러 기기와 팀이 공유한다. | 1인에게 관리 비용이 크다. | 팀 공유가 필요할 때 |
| MCP 검색 서버 또는 RAG | 수천 페이지 규모에서 검색 품질이 좋다. | 인프라를 유지해야 한다. | 카드가 수백 장을 넘을 때 |
| Notion 또는 Obsidian 을 원본으로 | 기존 도구를 쓴다. | grep 과 git 이력에서 분리된다. | git 을 원본으로 두고 Obsidian 은 뷰어로 쓴다. |

MCP 는 Model Context Protocol 이다. RAG 는 검색 결과를 LLM 입력에 붙이는 방식이다. Karpathy 도 Obsidian 을 뷰어로, Dataview 를 frontmatter 쿼리 도구로 언급한다 ([Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)). 사용자는 저장소 폴더를 Obsidian vault 로 열 수 있다.

## /recommend-prompt 는 카드를 번역하고 plain prompt 와 겨루게 한다

추천 skill 은 짧은 절차형 문서로 시작한다. Claude 는 작업 설명과 skill 설명을 대조해 skill 을 고른다. 공식 문서는 설명이 모호하거나 겹치면 Claude 가 skill 을 잘못 고른다고 경고한다 ([Extend Claude Code](https://code.claude.com/docs/en/features-overview)). 그래서 설명에 무엇을 하는지와 언제 쓰는지를 함께 쓴다. 가장 가까운 공개 사례는 `severity1/claude-code-prompt-improver` 다. 이 도구는 hook 으로 모호한 프롬프트를 감지하고, skill 로 질문 1–6개를 묻는다. 저자는 이 분리로 토큰이 31% 줄었다고 보고한다 ([newreleases.io v0.4.0](https://newreleases.io/project/github/severity1/claude-code-prompt-improver/release/v0.4.0)).

이번 조사는 카드 라이브러리를 기반으로 프롬프트를 추천하는 공개 사례를 찾지 못했다. 따라서 아래 초안은 공식 지침과 Karpathy 패턴에서 추론한 설계다. 매 프롬프트에 hook 을 거는 방식은 시작 단계에 과하다. 사용자가 `/recommend-prompt` 를 직접 부르는 방식으로 시작한다.

```markdown
---
name: recommend-prompt
description: ai-reference 카드 라이브러리를 근거로 업무 작업에 맞는 Claude 프롬프트를 추천한다. 사용자가 작업을 설명하고 "프롬프트 추천", "이 일 어떻게 시키지", "클로드에게 맡기는 법" 을 물을 때 쓴다.
argument-hint: [작업 설명]
---

1. /Users/leeyoonsam/Documents/ai-reference/index.md 를 Read 한다.
2. $ARGUMENTS 에 맞는 카드 3–5장을 고른다. 고른 카드만 Read 한다.
3. 카드의 review_by 가 오늘 이전이면, 그 카드에 "재검증 필요" 를 표시한다.
4. 카드 원칙을 프롬프트 문장으로 바꿔 추천 프롬프트 1개를 쓴다. 카드 본문을 그대로 붙이지 않는다.
5. 추천 프롬프트 아래에 적용한 카드 id 를 나열한다.
6. 카드와 skill 을 쓰지 않은 plain prompt 1개를 쓴다.
7. 둘 중 먼저 시도할 것과 이유를 1문장으로 쓴다.
```

4단계가 카드 본문을 붙이지 않는 이유가 있다. Thariq 는 Claude Code 가 시스템 프롬프트와 skill 로 Claude 를 "overconstraining" 했다고 썼다 ([Thariq](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/)). 카드를 통째로 붙이면 같은 과잉 지시가 생긴다. 6단계의 plain prompt 는 Felix PDF 의 체크리스트 항목을 절차에 넣은 장치다. 그 항목은 "오래된 스킬/지시문이 새 모델을 방해하고 있지 않나? (스킬 없이 프롬프트만으로도 비교해 보기)" 다 ([로컬 PDF 508행](file:///Users/leeyoonsam/Documents/ai-reference/references/클로드에게_일을_맡기는_법_실무레퍼런스.pdf)). 공식 skill 지침도 skill 없는 baseline 을 먼저 재라고 권한다 ([Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)).

Felix 레퍼런스에서 바로 만들 수 있는 첫 카드는 아래와 같다. 각 카드의 `source_url` 은 원 인터뷰나 Felix 블로그를 가리킨다. 한국어 정리 영상은 T3 전달 채널이다. 따라서 정리 영상 URL 은 `source_note` 에만 남긴다.

| 카드 id | 원칙 | 근거 |
|---|---|---|
| raise-altitude | 작업 단위가 아니라 결정 단위로 맡긴다. 예: `Tell me what changed this quarter, why, and what we should do about it.` | [Felix 블로그](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) |
| deeper-not-bigger | `I want a deeper version of this task, not a bigger one.` 으로 최고 전문가의 방법과 검증 기준을 먼저 묻는다. | [Felix 블로그](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) |
| reproduce-from-raw-data | 가설을 주고 원천 데이터에서 재현하게 한다. 예: `Try to reproduce that from the raw data.` | [Felix 블로그](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) |
| do-what-expert-does | 전문가처럼 "쓰게" 하지 않는다. 전문가가 "하는 일" 을 하게 한다. | [Felix 블로그](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) |
| grade-outside-session | 만든 세션이 채점하지 않는다. PDF 의 구조는 "공격 클로드 ×5 → 판사 클로드 → 만든 클로드" 다. | [Felix 블로그](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/), [로컬 변환 md 187행](file:///private/tmp/claude-501/-Users-leeyoonsam-Documents-ai-reference/99ff6306-dff2-4a3e-827d-62a155338d2a/scratchpad/pdftest/html/A.md) |
| skill-half-life-try-plain-prompt | 모델이 바뀌면 skill 없이도 시도한다. | [로컬 PDF 196행, ▶ 19:43](file:///Users/leeyoonsam/Documents/ai-reference/references/클로드에게_일을_맡기는_법_실무레퍼런스.pdf) |
| run-new-process-alongside | 새 프로세스를 기존 프로세스 옆에서 한 분기 동안 함께 돌린다. | [Felix 블로그](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) |

다른 1차 출처의 프롬프트 원문도 `prompts/` 의 시작 재료로 쓴다. 아래 원문은 모두 영어 그대로 둔다. 번역하면 원문 검증이 어려워지기 때문이다.

| 용도 | 원문 | 출처 |
|---|---|---|
| 목표와 이유 전달 | `I'm working on [the larger task] for [who it's for]. They need [what the output enables]. With that in mind: [request].` | [Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) |
| 미지수 줄이기 | `Interview me one question at a time about anything ambiguous.` | [Thariq X](https://x.com/trq212/status/2073100352921215386) |
| 검증 요구 | `Prove to me this works.` | [Boris X 2026-01-31](https://x.com/bcherny/status/2017742741636321619) |
| 다시 만들기 | `Knowing everything you know now, scrap this and implement the elegant solution.` | [Boris X 2026-01-31](https://x.com/bcherny/status/2017742741636321619) |
| 꾸민 보고 막기 | `Before reporting progress, audit each claim against a tool result from this session.` | [Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) |
| 범위 제한 | `Don't add features, refactor, or introduce abstractions beyond what the task requires.` | [Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) |
| 판단만 원할 때 | `When the user is describing a problem ... the deliverable is your assessment. Report your findings and stop.` | [Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) |

예를 들어 사용자가 "신규 입사자 3개월 내 퇴사 원인을 분석해서 피플팀 회의 자료를 만들고 싶다" 고 입력한다. 그러면 skill 은 `raise-altitude`, `reproduce-from-raw-data`, `grade-outside-session` 카드와 목표 전달 템플릿을 고른다. 아래 프롬프트는 이 조합으로 만든 예시다.

```text
피플팀 다음 주 회의용으로 신규 입사자 3개월 내 퇴사 원인을 분석한다.
팀은 이 자료로 온보딩 개선 항목 3개를 정해야 한다.
우리는 원인이 온보딩이라고 믿는다. 첨부한 원천 데이터에서 그 가설을 재현해 보고, 재현이 안 되면 그렇다고 말해 줘.
무엇이 바뀌었고, 왜 바뀌었고, 우리가 무엇을 해야 하는지로 정리해 줘.
시작 전에 모호한 점을 한 번에 하나씩 물어봐 줘.
결론마다 근거가 된 데이터 위치를 적어 줘. 검증은 내가 별도 세션에서 한다.
```

같은 skill 은 plain prompt 로 "첨부 데이터로 신규 입사자 3개월 내 퇴사 원인을 분석해 줘. 다음 주 피플팀 회의 자료다." 를 함께 낸다. 사용자는 두 결과를 비교한다. plain prompt 결과가 같거나 나으면, 해당 카드의 `status` 를 `needs-review` 로 바꾼다. 효과를 확인한 프롬프트는 `prompts/` 에 저장한다. 이 루프는 Karpathy 의 "좋은 답변을 wiki 에 다시 넣는다" 와 같다 ([Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)).

## PDF 를 고치지 말고 Aside 세션에 남은 원본 HTML 을 살린다

두 PDF 의 형식 차이는 변환 단계가 아니라 생성 단계에서 생겼다. 실측 결과 A PDF 에는 링크 annotation 이 36개 있다. B PDF 에는 링크가 0개다. A 는 타임스탬프를 `▶ mm:ss` 링크로 썼다. B 는 `[mm:ss]` 평문으로 썼다. 같은 Aside 가 두 문서를 만들었지만 지시가 달랐다. 따라서 변환 도구만 바꿔서는 형식이 통일되지 않는다.

두 PDF 의 원본 HTML 은 지금 Aside 세션 폴더에 있다. A 세션에는 `reference.html` 2.3 MB 와 한국어 자막 원문 `ko.txt` 71 KB 가 있다 ([A 세션 tmp](file:///Users/leeyoonsam/.aside/u/0/sessions/2026-10-29_xdB7AcOPjBgbupPS/tmp/)). B 세션에는 `doc.html` 7.7 MB 가 있고 자막 파일은 없다 ([B 세션 tmp](file:///Users/leeyoonsam/.aside/u/0/sessions/2026-10-29_mv5Ybyf4W44B89rA/tmp/)). Aside 문서는 생성 파일이 사용자가 task 나 폴더를 지울 때까지 남는다고 쓴다 ([Aside Tasks](https://docs.aside.com/help/tasks)). 자동 정리 여부는 확인하지 못했다. 그러므로 사용자는 이 파일을 오늘 `references/` 로 복사한다.

원본 HTML 을 markdown 으로 바꾸면 손실이 거의 없다. 연구자는 BeautifulSoup 과 markdownify 로 20줄 스크립트를 만들었다. 이 스크립트는 HTML 안의 base64 이미지를 파일로 풀고 상대 경로로 바꾼다. A 의 결과는 **링크 36/36, 이미지 33/33** 이다 ([html2md.py](file:///private/tmp/claude-501/-Users-leeyoonsam-Documents-ai-reference/99ff6306-dff2-4a3e-827d-62a155338d2a/scratchpad/pdftest/html2md.py)). 이 스크립트는 세션 임시 폴더에 있으므로, 사용자는 스크립트를 저장소 `scripts/` 로 옮긴다. 남는 결함은 3가지다. B 표 셀의 `|` 문자가 열을 깬다. 프롬프트 템플릿이 코드 블록이 아니다. B 에는 원본에도 링크가 없다.

| 방법 | 한국어 띄어쓰기 | 표 | 링크 | 이미지 | 판단 |
|---|---|---|---|---|---|
| 원본 HTML + markdownify | 정상 | 정상 | 36/36 | 33/33 | **최선** |
| pymupdf4llm layout 모드 | 캡션 일부 손실 | 대체로 정상 | 0 | 34 | PDF 만 남았을 때 |
| markitdown 0.1.9 | 정상 | 여러 줄 셀이 깨진다 | 0 | 0 | 텍스트 확인용 |
| `pdftotext -layout` | 정상 | 공백 정렬 텍스트 | 0 | 0 | LLM 파싱에 약하다 |

위 표는 이번 조사의 로컬 실측이다. 출력 파일은 [pdftest 폴더](file:///private/tmp/claude-501/-Users-leeyoonsam-Documents-ai-reference/99ff6306-dff2-4a3e-827d-62a155338d2a/scratchpad/pdftest/) 에 있다. Marker 와 Docling 은 시험하지 않았다. 두 PDF 는 텍스트 레이어가 있는 Chrome 인쇄 PDF 다. 따라서 OCR 과 GPU 를 쓰는 도구의 강점이 거의 필요 없다. 2026년 비교 글들도 단일 승자가 없다고 본다 ([The Menon Lab](https://themenonlab.blog/blog/best-open-source-pdf-to-markdown-tools-2026)).

PDF 만 남은 경우에는 `pymupdf4llm` 을 쓰고, 링크는 PyMuPDF 의 `page.get_links()` 로 따로 뽑아 붙인다. 2026-10 기준 `pymupdf4llm` 2.0 패키지는 빈 껍데기다. 사용자는 `pip install pymupdf` 로 설치한다. Claude 에게 PDF 를 직접 주는 방식은 요약에는 좋다. 그러나 Claude PDF 문서는 링크 처리를 언급하지 않는다. 같은 문서는 텍스트 비용을 **페이지당 1,500–3,000 토큰**으로 적는다 ([Claude PDF support](https://platform.claude.com/docs/en/build-with-claude/pdf-support)). A 문서 24쪽은 약 36K–72K 토큰이다. 같은 내용의 변환 md 는 18 KB 다. 그러므로 라이브러리에는 md 를 저장하고, PDF 는 보존용으로만 둔다.

앞으로의 형식 통일은 Aside 쪽에서 푼다. Aside 는 Chromium 기반의 로컬 우선 AI 브라우저다 ([docs.aside.com](https://docs.aside.com)). 공식 문서는 템플릿이나 커스텀 지시 기능을 설명하지 않는다. 그러나 로컬 내장 `skill-creator` 는 사용자 skill 경로를 `~/.aside/u/0/skills/user/<name>/SKILL.md` 로 정한다 ([로컬 skill-creator](file:///Users/leeyoonsam/.aside/u/0/skills/builtin/skill-creator/SKILL.md)). 내장 `youtube` skill 은 `getMetadata()` 와 `getTranscript()` 를 제공한다 ([로컬 youtube skill](file:///Users/leeyoonsam/.aside/u/0/skills/builtin/youtube/SKILL.md)). 현재 `skills/` 폴더에는 `builtin` 만 있다. Aside 가 사용자 skill 을 자동으로 고르는지는 실행해서 확인하지 않았다.

Aside 의 역할은 요약 노트에서 끝난다. Claude 가 요약 노트에서 카드를 만든다. 두 단계를 나누면 Aside 의 요약 품질이 바뀌어도 카드 형식은 흔들리지 않는다. 아래는 Aside 사용자 skill 초안이다. frontmatter 는 Aside 규칙대로 `name` 과 `description` 만 큰따옴표로 쓴다.

````markdown
---
name: "youtube-reference-md"
description: "사용자가 YouTube 영상을 요약, 정리, 실무 레퍼런스로 만들라고 할 때 쓴다. YAML frontmatter, 고정 섹션, 타임스탬프 링크를 갖춘 한국어 markdown 파일 1개를 만든다."
---

1. youtube.getMetadata() 로 제목·채널·게시일·길이를 가져온다. 추측하지 않는다.
2. youtube.getTranscript() 로 한국어 자막을 가져온다. 한국어 자막이 없으면, 원어 자막을 가져온다.
3. 자막 원문을 <slug>.transcript.txt 로 저장한다. 형식은 [mm:ss] 텍스트 다.
4. 아래 형식 규칙으로 <slug>.md 를 쓴다.
5. 화면 캡처는 assets/<slug>/NNN.jpg 로 저장한다. base64 로 넣지 않는다.
6. 사용자가 요청할 때만, 완성한 md 로 PDF 나 docx 를 만든다.
7. 저장한 파일 경로를 보고한다.

## 형식 규칙
- 파일 이름: YYYY-MM-DD_<channel-slug>_<topic-slug>.md. 날짜는 게시일이다.
- frontmatter 키 순서: title, doc_type(video-reference), source_url, video_id, channel, speakers, published, duration, related_sources, summarized, summarizer("Aside"), summarizer_model, transcript, language(ko), tags, valid_as_of, review_by.
- related_sources 에는 영상이 소개한 원 인터뷰·원문 글의 URL 을 적는다.
- 섹션 순서: 한 줄 요약 → TL;DR → 핵심 원칙 → 사례·수치 → 프롬프트 템플릿 → 체크리스트 → 타임스탬프 색인 → 주의·한계 → 출처.
- 내용이 없는 섹션은 머리글까지 지운다. 빈 머리글이 있으면 LLM 이 내용을 지어낼 수 있다.
- 타임스탬프는 항상 [▶ mm:ss](https://www.youtube.com/watch?v=<id>&t=<초>s) 로 쓴다.
- 이미지 캡션은 이미지 바로 아래 한 줄로 쓴다: *장면 설명* [▶ mm:ss](링크)
- 프롬프트 템플릿 원문은 항상 ```text 코드 블록에 넣는다.
- 표 셀 안에 | 를 쓰지 않는다. 필요하면 / 로 바꾼다.
- 영상에 없는 수치·인용을 만들지 않는다. 불확실한 내용은 주의·한계에 적는다.
````

Aside 가 사용자 skill 을 고르지 않으면, 사용자는 위 "형식 규칙" 을 매 요청에 붙여 넣는다. `related_sources` 규칙이 특히 중요하다. 이 필드가 있어야 Claude 가 카드의 `source_url` 을 T3 정리 영상이 아니라 원문으로 채운다. 이미지는 md 밖 `assets/` 에 둔다. A 의 이미지 33장은 1.7 MB 이고 md 텍스트는 18 KB 다. base64 로 넣으면 md 를 LLM 에 넣을 때 쓸모없는 토큰이 대량으로 들어간다.

## 빌더 추적은 피드가 있는 T1·T2 만 자동화하고 X 는 손으로 훑는다

가장 신뢰할 빌더의 주 채널이 가장 추적하기 어렵다. Boris Cherny, Cat Wu, Thariq Shihipar 는 주로 X 에 짧게 쓴다. X 의 무료 RSS 경로는 2026-09 에 사라졌다. Nitter 저장소는 2026-09-11 에 보관 처리됐다. XCancel 은 2026-09-14 에 무기한 중단됐다 ([TechCrunch 2026-09-15](https://techcrunch.com/2026/09/15/nitter-and-xcancel-are-dead-again-after-xs-latest-legal-actions)). YouTube 채널 RSS 도 연구 환경에서 5개 채널 모두 404 였다. 2025-12 이후 간헐적 404 보고가 있다 ([Google AI 개발자 포럼](https://discuss.ai.google.dev/t/youtube-rss-feed-endpoint-returns-404-errors/113379)). 사용자는 자기 Mac 에서 다시 시험해야 한다.

빌더의 X 글은 결국 공식 채널로 옮겨진다. Boris 의 기능 발표는 Claude Code 변경 이력에 들어간다. Thariq 의 원칙은 Claude 블로그와 공식 문서에 들어간다. 따라서 공식 변경 이력 피드가 X 를 대체하는 현실적 경로다. 아래 표는 2026-10-29 에 연구자가 직접 요청해 살아 있음을 확인한 시작 피드다.

| 등급 | 소스 | 피드 | 비고 |
|---|---|---|---|
| T1 | Claude Code 변경 이력 | [changelog/rss.xml](https://code.claude.com/docs/en/changelog/rss.xml) | 카드가 낡았는지 판정하는 가장 직접적 신호 |
| T1 | Claude Code GitHub 릴리스 | [releases.atom](https://github.com/anthropics/claude-code/releases.atom) | |
| T1 | Claude Platform 릴리스 노트 | [feed.xml](https://platform.claude.com/docs/en/release-notes/feed.xml) | 모델 출시와 폐기 기능 |
| T1 | Anthropic Engineering 블로그 | [Olshansk 대체 피드](https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_engineering.xml) | 공식 RSS 가 없다. 제3자 스크레이퍼다. |
| T1 | Claude 블로그 | [Olshansk 대체 피드](https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_claude.xml) | 위와 같다. |
| T1 | anthropics/skills | [commits/main.atom](https://github.com/anthropics/skills/commits/main.atom) | |
| T1 | Felix Rieseberg | [felixrieseberg.com/rss](https://www.felixrieseberg.com/rss) | |
| T2 | Simon Willison, claude-code 태그 | [claude-code.atom](https://simonwillison.net/tags/claude-code.atom) | 하루 여러 건 |
| T2 | Hamel Husain | [hamel.dev/index.xml](https://hamel.dev/index.xml) | 평가 설계 |
| T2 | Latent Space | [latent.space/feed](https://www.latent.space/feed) | 빌더 인터뷰 |
| T2 | Ethan Mollick | [oneusefulthing.org/feed](https://www.oneusefulthing.org/feed) | 비개발자 업무 위임 |
| T2 | Karpathy | [bearblog 피드](https://karpathy.bearblog.dev/feed/) | 빈도가 낮고 신호가 크다. |
| 2차 색인 | Boris 스레드 모음 | [howborisusesclaudecode.com](https://howborisusesclaudecode.com/) | 피드가 아니다. 주 1회 사용자가 확인한다. |
| T3 | AgentOS, 원티드 왓츠인마이AI | YouTube | 발견용으로만 쓴다. |

Boris 개인 소속과 직함은 2026 상반기 학습 지식 기준이다. 연구자는 10월 현재 소속을 확인하지 못했다. 피드 목록에서 Olshansk 피드는 사이트 구조가 바뀌면 조용히 멈출 수 있다. 수집 스크립트는 제3자 피드의 최신 날짜가 7일 넘게 멈추면 경고한다.

신뢰 등급은 산출물로 판정한다. 1차 빌더는 코드, 공식 문서, 제품 결정, 재현 가능한 수치를 남긴다. 재포장 콘텐츠는 원문 링크 없이 개수를 붙인 팁 목록을 만든다. 실제로 Boris 의 같은 스레드를 다룬 2차 글들은 팁 개수를 10·13·22·53개로 다르게 센다 ([VentureBeat](https://venturebeat.com/technology/the-creator-of-claude-code-just-revealed-his-workflow-and-developers-are), [Medium](https://medium.com/@joe.njenga/boris-cherny-claude-code-creator-shares-these-22-tips-youre-probably-using-it-wrong-1b570aedefbe)). 그러므로 2차 소스는 발견에만 쓴다. 라이브러리에는 2차 소스가 가리킨 원문만 저장한다. 사용자의 두 PDF 도 이 규칙의 대상이다. Felix PDF 는 Felix 인터뷰를 AgentOS 가 정리한 영상을 다시 Aside 가 요약한 문서다.

자동화는 수집과 판정을 나눈다. GitHub Actions 가 매일 피드를 받는다. 스크립트는 이전 상태 파일과 비교해 새 항목만 `feeds/inbox/` 에 쓴다. Claude Code 클라우드 예약 작업은 inbox 항목을 라이브러리와 대조해 판정한다. 나누는 이유는 2가지다. 클라우드 기본 환경은 허용 목록 밖 호스트를 `403 host_not_allowed` 로 막는다 ([Claude Code scheduled tasks](https://code.claude.com/docs/en/routines)). 결정적인 diff 는 LLM 이 아닌 스크립트가 맡아야 재현된다.

예약 작업은 Pro 이상 요금제에서 쓸 수 있다. 최소 주기는 1시간이다. 정각 실행은 몇 분 늦을 수 있으므로 09:07 같은 시각을 쓴다 ([Claude Code scheduled tasks](https://code.claude.com/docs/en/routines)). Claude 는 `claude/` 접두사 브랜치에 판정 결과를 커밋한다. 사용자는 주 1회 결과를 보고 머지한다. 아래는 판정 라벨이다.

| 라벨 | 뜻 | Claude 의 행동 |
|---|---|---|
| `NEW` | 라이브러리에 없는 개념이다. | 카드 초안을 만든다. |
| `UPDATE` | 기존 카드의 사실을 바꾼다. | 영향받는 카드 경로와 근거 1문장을 쓴다. |
| `STALE?` | 변경 이력이 카드의 기능 이름을 언급한다. | 카드 `status` 를 `needs-review` 로 바꾼다. |
| `DUP` | 기존 카드와 같은 내용이다. | 원문이 더 1차적이면 출처만 바꾼다. |
| `SKIP` | 마케팅, 채용, 무관한 주제다. | 아무것도 하지 않는다. |

`UPDATE` 의 실제 사례가 이미 있다. 2026 문서는 "scheduled tasks, formerly routines" 라고 쓴다 ([Claude Code scheduled tasks](https://code.claude.com/docs/en/routines)). "routines" 라는 이름으로 쓴 카드는 이 변경으로 갱신 대상이 된다.

## 1일차, 2주, 분기 단위로 키운다

공식 문서는 기능을 한꺼번에 만들지 말고 트리거가 생길 때 하나씩 더하라고 권한다. 예를 들어 같은 프롬프트를 반복 입력하면 skill 을 만든다. 매번 자동으로 일어나야 하면 hook 을 만든다. 두 번째 저장소가 같은 설정을 쓰면 plugin 을 만든다 ([Extend Claude Code](https://code.claude.com/docs/en/features-overview)). 아래 단계는 이 원칙을 따른다.

**1일차: 오늘 시작한다**

1. 사용자가 A 세션의 `reference.html`, `ko.txt`, `.docx` 를 `references/2026-10-26_agentos_delegate-to-claude/` 로 복사한다.
2. 사용자가 B 세션의 `doc.html`, `.docx` 를 `references/2026-10-28_wanted_hr-ai-agent/` 로 복사한다.
3. 사용자가 기존 PDF 2개를 각 폴더의 `original.pdf` 로 옮긴다.
4. Claude 가 `html2md.py` 를 저장소 `scripts/` 로 복사한다.
5. Claude 가 `html2md.py` 로 HTML 2개를 `notes/` 의 md 와 `assets/` 이미지로 바꾼다.
6. Claude 가 두 md 를 표준 형식으로 재구성한다.
7. Claude 가 B 의 `[mm:ss]` 평문을 영상 ID `IrK71LslbFQ` 기반 링크로 바꾼다.
8. 사용자가 링크와 이미지 수를 확인한다. 기대값은 A 링크 36개·이미지 33장, B 이미지 43장이다.
9. Claude 가 A 요약 노트에서 원칙 카드 7–12장을 만든다.
10. Claude 가 B 요약 노트에서 `type: case` 카드 3–5장을 만든다.
11. Claude 가 `CLAUDE.md`, `index.md`, `log.md` 를 만든다.
12. Claude 가 `.claude/skills/recommend-prompt/SKILL.md` 를 만든다.
13. 사용자가 실제 업무 작업 1개로 `/recommend-prompt` 를 시험한다.

**2주차까지: 실사용으로 다듬는다**

1. 사용자가 실무 작업마다 `/recommend-prompt` 를 쓴다.
2. 사용자가 효과를 본 프롬프트를 `prompts/` 에 저장한다.
3. 사용자가 Aside 에게 skill-creator 로 `youtube-reference-md` 를 등록하라고 요청한다.
4. 사용자가 새 영상 1개로 Aside 출력이 표준 형식인지 확인한다.
5. 사용자가 다른 업무 저장소에서도 skill 이 필요하면, skill 을 `~/.claude/skills/` 로 옮긴다.
6. Claude 가 `scripts/freshness.py` 를 만든다. 이 스크립트는 `review_by` 가 지난 카드를 나열한다.
7. 사용자가 위 피드 표의 T1 피드 5개를 피드 리더에 넣고 주 1회 훑는다.

symlink 로 skill 을 연결하는 방식은 이번 조사에서 동작을 확인하지 않았다. 사용자가 symlink 를 쓰면, Claude Code 의 skill 목록에 skill 이 보이는지 먼저 확인한다.

**1–3개월: 자동화를 더한다**

1. Claude 가 GitHub Actions 피드 수집 workflow 를 만든다.
2. 사용자가 `/schedule` 로 매일 09:07 KST 트리아지 예약 작업을 만든다.
3. Claude 가 `ingest-reference` skill 을 만든다. 이 skill 은 요약 노트 1개를 카드 N장, `index.md` 갱신, `log.md` 1줄로 바꾼다.
4. 새 모델이 출시되면, Claude 가 `half_life: short` 카드를 카드 적용 프롬프트와 plain prompt 로 각각 실행한다.
5. 사용자가 두 결과를 비교한다. plain prompt 가 같거나 나으면, 사용자가 그 카드를 `deprecated` 로 바꾼다.
6. 사용자가 분기마다 `/doctor prompt-audit` 로 CLAUDE.md 와 skill 의 낡은 지시를 찾는다.

`/doctor prompt-audit` 는 Claude Code v2.1.283 이상이 필요하다 ([Memory](https://code.claude.com/docs/en/memory)). 다음 확장은 조건이 생길 때만 한다. 카드가 수백 장을 넘으면, 사용자는 MCP 검색 서버를 검토한다. 피플팀 동료와 공유해야 하면, 사용자는 plugin 배포를 검토한다. 원티드 사례처럼 팀이 함께 쓰는 단계가 오면 이 조건이 생긴다.

## 결론

이 라이브러리의 가장 큰 위험은 라이브러리 자신이 "새 모델을 방해하는 낡은 skill" 이 되는 것이다. Boris 의 미사용 skill 38개와 10k 토큰 CLAUDE.md 가 그 위험의 실제 모습이다. 그러므로 라이브러리의 성공 지표는 카드 수가 아니다. 성공 지표는 재검증된 카드 비율과 폐기된 카드 수다. 모든 추천에 plain prompt 를 붙이는 설계가 이 지표를 자동으로 만든다. 사용자는 매번 카드가 아직 값을 하는지 확인하게 된다.

가장 오래 가치를 지키는 자산은 요약이 아니라 원천과 원문 링크다. 사용자의 두 PDF 는 T1 발언을 T3 채널이 정리하고 Aside 가 다시 요약한 문서다. 요약은 모델이 바뀌면 다시 만들 수 있다. 그러나 `ko.txt` 자막과 원 인터뷰 URL 을 잃으면, 사용자는 요약을 다시 만들 수 없고 검증할 수도 없다. 남은 불확실성은 3가지다. 반감기 기간 값은 실증 근거가 없다. Aside 사용자 skill 의 자동 선택은 검증하지 않았다. YouTube RSS 가 사용자 Mac 에서 동작하는지 확인하지 않았다. 세 가지 모두 2주차 실사용에서 사용자가 확인할 수 있다.
