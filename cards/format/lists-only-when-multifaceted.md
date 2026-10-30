---
id: lists-only-when-multifaceted
title: 목록은 내용이 다면적일 때만 쓴다. 관계와 논증은 산문으로 쓴다
type: principle
scope: both
tags: [format, lists, markdown]
source_note: research/2026-10-30_답변-포맷/report.md
source_url: "https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1"
author: Anthropic (claude.ai 시스템 프롬프트), Microsoft, Google
tier: T1
source_date: 2026-09-01
valid_as_of: 2026-10-30
model_context: Claude Fable 5.1
half_life: medium
review_by: 2027-10-30
status: active
superseded_by:
---
## 원칙

Claude 는 병렬 항목과 절차를 목록으로 쓴다. 관계, 비교, 논증은 산문으로 쓴다. 목록은 항목 사이의 관계를 지운다. 그래서 "왜" 를 설명하는 글에 목록을 쓰면 논리가 사라진다. 목록을 쓸 때 항목은 2개 이상 7개 이하다. 항목 1개는 목록이 아니다. 친밀한 대화, 감정적 대화, 거절에서는 포맷을 쓰지 않는다. 포맷은 글을 격식 있고 사무적으로 만들기 때문이다.

## 언제 쓰나

- 답변에 불릿이 먼저 떠오를 때 쓴다. 항목이 서로 독립적인지 먼저 묻는다.
- 비교나 추론을 설명할 때 쓴다. 이때는 산문이 맞다.
- 단계가 있는 절차를 쓸 때 쓴다. 이때는 번호 목록이 맞다.
- 목록 항목이 8개를 넘을 때 쓴다. 항목을 묶거나 표로 바꾼다.
- 사용자가 힘든 일을 말할 때 쓴다. 불릿 없이 문장으로 답한다.

## 프롬프트 문장

```text
목록은 항목이 서로 독립적일 때만 써 줘. 예: 파일 목록, 선택지, 절차 단계.
관계, 비교, 이유를 설명할 때는 문장으로 이어 써 줘.
목록 1개는 2개 이상 7개 이하 항목으로 써 줘.
```

## 근거

- Anthropic 의 Fable 5.1 claude.ai 시스템 프롬프트는 "Claude uses lists and bullet points when asked to or when the content is multifaceted enough that they help with clarity" 라고 쓴다. 같은 판은 "Claude uses the minimum formatting needed for clarity" 를 둔다. [Claude Fable 5.1 system prompts](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1)
- 같은 프롬프트는 감정적 대화에서 포맷을 쓰지 않는다. 이유는 "any kind of formatting lends a more formal and professional tone to the conversation" 이다. [Claude Fable 5.1 system prompts](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1)
- Microsoft 스타일 가이드는 "A list should have at least two items but (if possible) no more than seven items" 를 둔다. [Microsoft Lists](https://learn.microsoft.com/en-us/style-guide/scannable-content/lists)
- Google 개발자 문서 가이드는 "Don't use a list to show only one item" 을 둔다. [Google Lists](https://developers.google.com/style/lists)
- GOV.UK 는 도입문 필수와 불릿 1개당 1문장을 둔다. [GOV.UK A to Z style guide](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/style-guides/a-to-z-style-guide/)
- Edward Tufte 는 불릿 목록이 "a misleading façade of objectivity and neutrality" 를 만든다고 비판했다. Jeff Bezos 는 "We don't do PowerPoint" 라고 쓰고 서사 메모를 요구했다. 두 비판은 논증 문서를 말한다. [Wikipedia The Cognitive Style of PowerPoint](https://en.wikipedia.org/wiki/The_Cognitive_Style_of_PowerPoint), [2017 Letter to Shareholders](https://www.aboutamazon.com/news/company-news/2017-letter-to-shareholders)
- Nielsen Norman Group 은 웹 조회용 글에서 스캔 가능한 레이아웃이 사용성을 높인다고 보고했다. 두 진영의 차이는 문서 목적이다. 조회와 절차는 목록, 논증과 비교는 산문이 맞다. [NN/g How Users Read on the Web](https://www.nngroup.com/articles/how-users-read-on-the-web/)
- 보조 근거: 2026년 연구는 사람이 마크다운을 약 57% 만 선호하고 LLM 판정자는 73~97% 선호한다고 보고했다. 모델의 불릿 과용은 판정자 편향에서 온다. 이 논문은 단독 저자 preprint 이고 사람 실험의 n 은 확인하지 못했다. [Judging the Judges](https://arxiv.org/html/2604.23178)
- 주의: Anthropic 의 공개 규칙은 2년 동안 5번 바뀌었다. 그래서 half_life 는 medium 이다.
- 관련 카드: `markdown-only-when-rendered`, `check-model-default-before-format-rules`.

## 지난 방식

- 2024-10 Sonnet 3.5 시스템 프롬프트: "Claude should not use bullet points or numbered lists unless the human explicitly asks for a list". 전면 금지였다. [Claude Sonnet 3.5 system prompts](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-sonnet-3-5)
- 2026-02 Opus 4.6 시스템 프롬프트: 보고서와 설명문을 산문으로 쓰고 불릿은 1~2문장 이상으로 쓰라고 명시했다. [Claude Opus 4.6 system prompts](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-opus-4-6)
- 2026-09 Fable 5.1 판에서 두 규칙이 "다면적일 때 허용" 으로 바뀌었다. 보고서를 산문으로 쓰라는 문장은 사라졌다.
