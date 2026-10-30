---
id: agent-report-outcome-first
title: 에이전트 작업 보고는 결과 1~2문장으로 시작하고 요약을 반복하지 않는다
type: pattern
scope: agent-task
tags: [format, agent, report]
source_note: research/2026-10-30_답변-포맷/report.md
source_url: "https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1"
author: Anthropic (claude.ai 시스템 프롬프트), OpenAI (Codex CLI), Google (Gemini CLI)
tier: T1
source_date: 2026-09-01
valid_as_of: 2026-10-30
model_context: Claude Fable 5.1, Claude Code v2.1
half_life: medium
review_by: 2027-10-30
status: active
superseded_by:
---
## 원칙

Claude 는 도구 호출을 끝낸 뒤 사용자가 물은 답을 1~2문장으로 쓴다. "완료했습니다." 만 쓰는 것은 답이 아니다. 보고는 작업을 보지 않은 독자가 읽는다. 그래서 완전한 문장으로 쓴다. 메타 서술은 뺀다. 예: "이제 설명하겠습니다", "요약하면". 이미 쓴 내용을 끝에서 다시 요약하지 않는다. 다음 단계 제안은 실제 다음 단계가 있을 때만 쓴다. 오류, 테스트 실패, 보안 경고는 줄이지 않고 전체를 쓴다.

## 언제 쓰나

- 파일 수정, 명령 실행, 조사 같은 도구 작업 뒤 보고할 때 쓴다.
- 보고가 "Done." 이나 "완료" 로 끝날 때 쓴다. 결과 문장을 더한다.
- 보고 끝에 본문과 같은 내용의 요약이 붙을 때 쓴다. 요약을 지운다.
- 보고가 "더 도와드릴까요?" 로 끝날 때 쓴다. 실제 다음 단계가 없으면 지운다.
- 하네스 시스템 프롬프트나 output style 을 설계할 때 쓴다.

## 프롬프트 문장

```text
작업을 끝내면 첫 문장에 결과를 써 줘. 무엇이 바뀌었고 검증은 어떻게 했는지 1~2문장이다.
작업 과정을 보지 않은 사람이 읽는다. 완전한 문장으로 써 줘.
본문을 끝에서 다시 요약하지 말아 줘. 다음 단계는 실제로 있을 때만 1개 제안해 줘.
오류와 테스트 실패는 줄이지 말고 출력 그대로 보여 줘.
```

## 근거

- Anthropic 의 Fable 5.1 claude.ai 시스템 프롬프트는 "After its last tool call in a turn, Claude states the answer the person asked for in one or two sentences; a sign-off alone, such as "Done.", is not a reply." 를 둔다. [Claude Fable 5.1 system prompts](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1)
- Anthropic 의 Fable 5 가이드는 최종 요약을 작업을 보지 않은 독자를 위해 완전한 문장으로 다시 쓰라고 권한다. [Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5#readability-when-communicating-with-the-user)
- Claude Code 의 Concise output style 은 첫 문장에 결과를 쓰고, 단순 질문은 1~3문장으로 답한다. 오류, 테스트 실패, 보안 경고는 전체 길이를 유지한다. [Output styles](https://code.claude.com/docs/en/output-styles)
- OpenAI 의 Codex CLI 시스템 프롬프트는 단순 작업에서 결과로 시작하고 "Do not start this explanation with "summary"" 를 둔다. 다음 단계는 자연스러운 다음 단계가 있을 때만 제안한다. [Codex CLI prompt](https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/gpt-5.1-codex-max_prompt.md)
- Google 의 Gemini CLI 는 "After completing a code modification or file operation *do not* provide summaries unless asked" 와 "Aim for fewer than 3 lines of text output" 를 둔다. [Gemini CLI snippets.ts](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/packages/core/src/prompts/snippets.ts)
- GOV.UK 글쓰기 지침은 본문을 다시 요약하는 중복을 금지한다. [GOV.UK Create a clear structure](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-structure/)
- 충돌: 대화형 답변에서는 Fable 5.1 시스템 프롬프트가 더 할 말이 있다고 알리는 것을 허용한다. 에이전트 작업 보고에서는 CLI 하네스 3개가 모두 마무리 제안을 제한한다. 이 카드의 scope 는 agent-task 다.
- 주의: Claude Code 의 실제 시스템 프롬프트 중 최종 메시지 규칙은 공개 문서에 없다. 공개된 output style 설명으로 대신했다.
- 관련 카드: `lead-with-outcome`, `readability-over-brevity`, `markdown-only-when-rendered`.
