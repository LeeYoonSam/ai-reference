---
id: nouns-to-verbs
title: 과제를 명사가 아니라 동사로 다시 정의하고 다른 분야의 방법을 끌어온다
type: pattern
scope: agent-task
tags: [delegation, range]
source_note: notes/2026-10-26_agentos_delegate-to-claude.md
source_url: "https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/"
author: Felix Rieseberg (Anthropic)
tier: T1
source_date: 2026-10-13
valid_as_of: 2026-10-29
model_context: Claude Opus 5.5, Claude Code v2.1
half_life: medium
review_by: 2027-10-29
status: active
superseded_by:
---
## 원칙

사용자는 과제를 결과물의 이름이 아니라 그 결과물이 하는 일로 다시 정의한다. 예: 분기 보고는 "덱" 이 아니다. 분기 보고는 바쁜 사람들이 30분 안에 인과관계에 대한 이야기를 믿고, 불확실성 속에서 결정하게 만드는 일이다. 동사로 바꾸면 어떤 분야의 관점이 도움이 될지 보인다. 사용자는 그 분야 사람들이 실제로 하는 일을 과제에 적용하게 한다. 펠릭스의 블로그는 이 방향을 Range 라고 부른다.

## 언제 쓰나

- 과제에 결과물의 형식 이름만 있고 목적이 흐릴 때 쓴다. 예: 덱, 보고서, 대시보드.
- 결과물이 한 분야의 방법만 써서 평범할 때 쓴다.
- 다른 분야를 끌어올 때 역할을 씌우지 않는다. 자세한 규칙은 `role-sentence-roleplay-trap` 카드를 본다.

## 프롬프트 문장

```text
이 과제를 명사가 아니라 동사로 다시 정의해 줘.
과제: [결과물 이름. 예: 분기 보고 덱]
예: "덱" 대신 "바쁜 사람들이 30분 안에 인과관계를 믿고 결정하게 만드는 일".
그 동사를 가장 잘하는 분야 5개를 골라 줘.
각 분야의 사람이 실제로 하는 일, 곧 조사 방법과 도구를 이 과제에 적용해 줘. 그 사람의 말투를 흉내 내지 말고 그 사람이 하는 일을 해 줘.
```

## 근거

- 블로그 원문의 Range 파트는 명사를 동사로 바꾸고 크루를 모으라고 쓴다. 크루의 예는 분석가, 저널리스트, 편집자, 디자이너다. 레드팀으로 공매도 투자자와 포렌식 회계사를 넣는다. 블로그는 공매도 투자자처럼 쓰게 하지 말고 그가 하는 일을 하게 하라고 쓴다. [Felix 블로그](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)
- 정리 영상은 야심의 네 갈래를 설명 슬라이드로 보여 준다. 네 갈래는 속도, 고도, 깊이, 범위다. 이 구간에는 자막 발언이 없다. [▶ 36:26](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=2186s)
- 펠릭스는 인터뷰에서 사람들이 가능하다고 믿는 틀을 벗어 던지고, 왜 이 일을 하는지 다시 생각하기를 바란다고 말했다. [▶ 34:41](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=2081s)
- 주의: 명사를 동사로 바꾸는 기법 자체는 자막에 없다. 이 기법의 근거는 블로그 원문이다.
