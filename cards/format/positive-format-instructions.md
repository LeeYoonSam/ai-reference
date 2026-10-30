---
id: positive-format-instructions
title: 포맷 지시는 금지형이 아니라 원하는 형태로 쓴다
type: pattern
scope: both
tags: [format, prompt, instruction]
source_note: research/2026-10-30_답변-포맷/report.md
source_url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#control-the-format-of-responses"
author: Anthropic (Developer Platform 문서)
tier: T1
source_date: 2026-09-01
valid_as_of: 2026-10-30
model_context: Claude Fable 5.1, Claude Opus 5
half_life: long
review_by: 2027-10-30
status: active
superseded_by:
---
## 원칙

사용자는 포맷을 지시할 때 원하는 결과의 모습을 쓴다. 금지 목록을 쓰지 않는다. "마크다운을 쓰지 마" 는 Claude 에게 대안을 알려 주지 않는다. "자연스럽게 이어지는 산문 단락으로 써" 는 알려 준다. 예시 1개가 금지 목록보다 잘 지켜진다. 예시에는 사용자 요청, 올바른 응답, 그 응답이 옳은 이유 1문장을 함께 넣는다. 사용자 지침의 "금지 규칙에 이유 1문장" 규칙은 이 패턴과 같은 방향이다.

## 언제 쓰나

- 프롬프트나 CLAUDE.md 에 "~하지 마" 포맷 규칙이 쌓일 때 쓴다. 각 규칙을 원하는 모습으로 바꾼다.
- 금지 규칙이 지켜지지 않을 때 쓴다. 예시 1개로 바꾼다.
- 톤이나 포맷 선호를 긴 시스템 프롬프트에 둘 때 쓴다. 말미에 짧은 리마인더를 둔다.

## 프롬프트 문장

```text
답변은 이어지는 산문 단락으로 써 줘. 각 단락은 주장 1개와 근거를 담는다.

<example>
<user>이 두 접근 방식의 차이를 설명해 줘.</user>
<response>A 는 ... 반면 B 는 ... 그래서 ... 상황에서는 A 가 맞다.</response>
<rationale>비교와 이유를 한 흐름으로 읽을 수 있어서 산문이 맞다.</rationale>
</example>
```

## 근거

- Anthropic 의 프롬프트 모범 사례는 포맷 제어 4원칙 중 첫째로 "Tell Claude what to do instead of what not to do" 를 둔다. 예시는 "Do not use markdown in your response" 대신 "Your response should be composed of smoothly flowing prose paragraphs." 다. [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#control-the-format-of-responses)
- 같은 문서의 나머지 3원칙은 XML 포맷 태그 사용, 프롬프트 스타일과 출력 스타일 일치, 상세 지시다. [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#control-the-format-of-responses)
- Opus 5 가이드는 "Positive examples of the communication style you want tend to be more effective than instructions about what not to do" 라고 쓴다. [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5#user-facing-progress-updates)
- Fable 5.1 가이드는 예시 1개로 가르치는 방법을 든다. 사용자 요청, 올바른 응답, 그 응답이 옳은 이유 1문장을 함께 넣는다. [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1#quoting-retrieved-sources)
- Fable 5.1 가이드는 anti-formatting 규칙을 지우고 "a rule that says when specific formatting is appropriate" 로 바꾸라고 권한다. 금지 규칙은 필요한 구조까지 억누른다. [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1#formatting-in-chat)
- claude.ai 시스템 프롬프트는 말미에 `<tone_preference>` 같은 짧은 리마인더를 둔다. 긴 프롬프트에서 포맷 선호를 유지하는 방법이다. [Claude Fable 5.1 system prompts](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1)
- 관련 카드: `fewer-format-rules`, `check-model-default-before-format-rules`.

## 지난 방식

- 2025년 이전: 응답 첫머리를 prefill 로 고정해 포맷을 강제했다. Claude 4.6 부터 prefill 은 400 오류를 낸다. 대체 수단은 structured outputs, XML 태그, "Respond directly without preamble" 지시다. [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
