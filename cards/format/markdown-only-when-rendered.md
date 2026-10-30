---
id: markdown-only-when-rendered
title: 마크다운은 렌더링되는 채널에서만 쓴다
type: principle
scope: both
tags: [format, markdown, channel]
source_note: research/2026-10-30_답변-포맷/report.md
source_url: "https://www.anthropic.com/constitution"
author: Anthropic (Claude 헌법), OpenAI, Google, xAI
tier: T1
source_date: 2026-01-21
valid_as_of: 2026-10-30
model_context: Claude Fable 5.1, Claude Code v2.1
half_life: long
review_by: 2027-10-30
status: active
superseded_by:
---
## 원칙

Claude 는 출력 채널이 마크다운을 렌더링할 때만 마크다운을 쓴다. 채팅 웹 UI 는 렌더링한다. 터미널, 음성, SNS 답글, API 응답 본문, 로그는 렌더링하지 않는다. 렌더링되지 않는 채널에서 마크다운은 기호 잡음이다. 사용자는 프롬프트에 채널을 밝힌다. 그러면 Claude 가 포맷을 채널에 맞춘다. 마크다운 기본값을 둘러싼 벤더 간 차이는 충돌이 아니다. 채널 차이다.

## 언제 쓰나

- API 로 받은 답을 다른 시스템에 그대로 넣을 때 쓴다. 평문을 요청한다.
- 터미널 도구의 최종 메시지를 설계할 때 쓴다. 경로와 명령만 백틱으로 감싼다.
- 음성 인터페이스나 SMS 로 답을 보낼 때 쓴다. 포맷 기호를 모두 뺀다.
- 채팅 UI 에서 답할 때 쓴다. 이때는 마크다운이 맞다. 다만 `lists-only-when-multifaceted` 카드의 기준을 따른다.

## 프롬프트 문장

```text
이 답은 [터미널 / 음성 / Slack 평문 / API 본문] 으로 전달된다. 마크다운이 렌더링되지 않는다.
헤더, 볼드, 불릿 기호 없이 문장으로 써 줘. 파일 경로와 명령만 백틱으로 감싸 줘.
```

## 근거

- Claude 의 헌법은 기본값으로 "using Markdown only if Markdown is likely to be rendered" 를 둔다. 이 규칙은 사용자 지시와 운영자 지시가 없을 때 적용된다. [Claude's constitution](https://www.anthropic.com/constitution)
- OpenAI 의 GPT-5 가이드는 "By default, GPT-5 in the API does not format its final answers in Markdown" 이라고 쓴다. 채팅 제품과 API 의 기본값이 다르다. [GPT-5 prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide)
- OpenAI 의 Codex CLI 시스템 프롬프트는 "You are producing plain text that will later be styled by the CLI" 라고 선언한다. [Codex CLI prompt](https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/gpt-5.1-codex-max_prompt.md)
- Google 의 Gemini CLI 는 GitHub Flavored Markdown 을 허용하지만 monospace 렌더링을 경고하고 출력을 3줄 미만으로 둔다. [Gemini CLI snippets.ts](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/packages/core/src/prompts/snippets.ts)
- xAI 의 X 답글용 공개 프롬프트는 "Do not use markdown formatting" 과 "under 550 characters" 를 둔다. [xai-org/grok-prompts](https://github.com/xai-org/grok-prompts/blob/main/ask_grok_system_prompt.j2)
- OpenAI Model Spec 2025-02-12 판은 대화형 기본값을 Markdown 으로 뒀다. 2026-10-29 판은 이를 지우고 "If parts of the response are in a specific format (e.g., Markdown, code, JSON, LaTeX), GPT should adhere to the specifications of that format" 로 일반화했다. [Model Spec 2026-10-29](https://model-spec.openai.com/2026-10-29.html)
- 주의: 헌법의 공개일 2026-01-21 은 2차 보도로 확인했다. 헌법 페이지에 날짜가 없다.
- 관련 카드: `lists-only-when-multifaceted`, `agent-report-outcome-first`.
