---
id: check-model-default-before-format-rules
title: 포맷 규칙을 더하기 전에 모델의 기본값을 먼저 확인한다
type: pattern
scope: both
tags: [format, model-upgrade, verbosity]
source_note: research/2026-10-30_답변-포맷/report.md
source_url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#communication-style-and-verbosity"
author: Anthropic (Developer Platform 문서)
tier: T1
source_date: 2026-09-01
valid_as_of: 2026-10-30
model_context: Claude Fable 5.1, Claude Opus 5
half_life: short
review_by: 2027-01-30
status: active
superseded_by:
---
## 원칙

사용자는 포맷 규칙을 쓰기 전에 모델의 기본 출력을 본다. 그다음 기본값에서 벗어나게 하는 규칙만 쓴다. 장황함과 포맷 기본값은 모델 세대마다 반대 방향으로 움직인다. Opus 5 는 이전 모델보다 길게 답한다. Fable 5.1 은 볼드, 헤더, 목록을 덜 쓴다. 그래서 한 세대에 맞춘 "간결하게", "불릿 금지" 규칙은 다음 세대에서 필요한 구조까지 억누른다. 모델을 바꾸면 포맷 규칙을 다시 검사한다.

## 언제 쓰나

- 새 모델로 바꿀 때 쓴다. CLAUDE.md 와 시스템 프롬프트의 포맷 규칙을 하나씩 다시 검사한다.
- 답변이 너무 짧거나 구조가 사라졌을 때 쓴다. 억제 규칙이 원인인지 본다.
- "간결하게" 규칙을 더하려 할 때 쓴다. 먼저 규칙 없는 출력의 길이를 잰다.
- `skill-half-life-try-plain-prompt` 카드와 함께 쓴다. 스킬뿐 아니라 포맷 규칙도 낡는다.

## 프롬프트 문장

```text
같은 요청을 2번 처리해 줘. 1번은 지금 CLAUDE.md 의 포맷 규칙을 모두 적용한다.
2번은 포맷 규칙을 모두 뺀다. 두 답의 길이, 목록 수, 헤더 수를 표로 비교해 줘.
어느 쪽이 나은지는 내가 판단한다.
```

## 근거

- Anthropic 의 프롬프트 모범 사례는 Opus 5 를 "its default user-facing responses run longer than prior models'" 로, Fable 5.1 을 "it uses bold less and is less likely to reach for headers, lists, or quotation marks" 로 설명한다. [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#communication-style-and-verbosity)
- Opus 5 가이드는 "Keep responses focused, brief, and concise" 같은 명시 지시를 더하라고 권한다. [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5#response-length-and-verbosity)
- Fable 5.1 가이드는 반대 방향이다. "If your prompt contains anti-formatting language, remove it or replace it with a rule that says when specific formatting is appropriate" 라고 쓴다. [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1#formatting-in-chat)
- 같은 가이드는 Fable 5.1 에서 진행 보고가 줄었으므로 필요하면 요청하라고 권한다. [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1#ask-for-user-facing-progress-updates)
- claude.ai 공개 시스템 프롬프트의 포맷 규칙은 2024-09 부터 2026-09 까지 5번 바뀌었다. 2024-10 은 불릿 전면 금지, 2026-09 는 다면적일 때 허용이다. [Claude Sonnet 3.5 system prompts](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-sonnet-3-5), [Claude Fable 5.1 system prompts](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1)
- 보조 근거: 커뮤니티 벤치마크는 "간결" 규칙의 토큰 감소가 haiku 4%, sonnet 12%, opus 7% 에 그쳤다고 보고했다. 기본값이 이미 "0% preamble, sycophancy" 라서 서두 금지 규칙은 입력 토큰만 늘린다고 적었다. 이 벤치마크는 N=5 의 커뮤니티 리포지토리다. [drona23/claude-token-efficient](https://github.com/drona23/claude-token-efficient)
- 주의: 이 카드의 모델별 기본값 설명은 Fable 5.1 과 Opus 5 기준이다. 다음 모델에서 뒤집힐 수 있다. 그래서 half_life 는 short 다. 패턴 자체는 유지된다.
- 관련 카드: `skill-half-life-try-plain-prompt`, `fewer-format-rules`, `positive-format-instructions`.
