---
id: lead-with-outcome
title: 결론을 첫 문장에 쓴다
type: principle
scope: both
tags: [format, structure, readability]
source_note: research/2026-10-30_답변-포맷/report.md
source_url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5#strong-instruction-following"
author: Anthropic (Developer Platform 문서), Nielsen Norman Group, GOV.UK
tier: T1
source_date: 2026-09-01
valid_as_of: 2026-10-30
model_context: Claude Fable 5.1, Claude Code v2.1
half_life: long
review_by: 2027-10-30
status: active
superseded_by:
---
## 원칙

Claude 는 답변의 첫 문장에 결론을 쓴다. 결론은 "무엇이 일어났나" 또는 "무엇을 찾았나" 에 대한 답이다. 독자는 첫 문장만 읽어도 핵심을 얻는다. 근거, 과정, 조건은 그 뒤에 쓴다. 이 규칙은 Anthropic 문서, 웹 가독성 연구, 공공 문서 표준, 군사 문서 규정, 컨설팅 글쓰기가 모두 같은 형태로 둔다. 그래서 모델 세대가 바뀌어도 유지된다.

## 언제 쓰나

- 질문에 답할 때 쓴다. 첫 문장이 답이다.
- 작업 결과를 보고할 때 쓴다. 첫 문장이 결과다. `agent-report-outcome-first` 카드가 보고 형식을 더 자세히 다룬다.
- 조사 보고서를 쓸 때 쓴다. 첫 단락이 결론과 핵심 근거를 담는다.
- 사용자가 답변을 끝까지 읽지 않을 때 쓴다. 웹 독자는 단어의 20~28% 만 읽는다.

## 프롬프트 문장

```text
첫 문장에 결론을 써 줘. "무엇이 일어났나" 또는 "무엇을 찾았나" 에 바로 답해 줘.
근거와 과정은 그 뒤에 써 줘. 작업 과정을 설명하는 서두는 쓰지 말아 줘.
```

## 근거

- Anthropic 의 Fable 5 가이드는 지시 예시로 "Lead with the outcome. Your first sentence after finishing should answer "what happened" or "what did you find"" 를 든다. [Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5#strong-instruction-following)
- Claude Code 의 Concise output style 은 "the first sentence of a response states what happened or what the answer is" 로 설명된다. [Output styles](https://code.claude.com/docs/en/output-styles)
- Nielsen Norman Group 의 역피라미드 글은 "The story should start with the main point" 라고 쓴다. [NN/g Inverted Pyramid](https://www.nngroup.com/articles/inverted-pyramid/)
- Nielsen Norman Group 은 웹 독자가 페이지 단어의 20~28% 만 읽는다고 보고했다. [NN/g How Little Do Users Read?](https://www.nngroup.com/articles/how-little-do-users-read/)
- GOV.UK 글쓰기 지침은 "Put the most important information first" 를 둔다. [GOV.UK Create a clear structure](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-structure/)
- Microsoft 스타일 가이드는 "Get to the point." "Then stop." 을 둔다. [Microsoft Scannable content](https://learn.microsoft.com/en-us/style-guide/scannable-content/)
- 미 육군 규정 AR 25-50 의 BLUF 와 Minto 피라미드의 Answer-first 가 같은 규칙이다. [Wikipedia BLUF](https://en.wikipedia.org/wiki/BLUF_(communication))
- OpenAI 의 Codex CLI 시스템 프롬프트는 단순 작업에서 결과로 시작하고 "Do not start this explanation with "summary"" 를 둔다. [Codex CLI prompt](https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/gpt-5.1-codex-max_prompt.md)
- 관련 카드: `agent-report-outcome-first`, `readability-over-brevity`.
