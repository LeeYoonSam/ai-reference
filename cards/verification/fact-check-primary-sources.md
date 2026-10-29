---
id: fact-check-primary-sources
title: 팩트 체크는 1차 자료를 찾고 그 자료의 신뢰성까지 확인하게 한다
type: prompt
scope: agent-task
tags: [verification, fact-check, prompt]
source_note: notes/2026-10-26_agentos_delegate-to-claude.md
source_url: "https://www.youtube.com/watch?v=D-SVFneJ_Nk"
author: Felix Rieseberg (Anthropic)
tier: T1
source_date: 2026-10-20
valid_as_of: 2026-10-29
model_context: Claude Opus 5.5, Claude Code v2.1
half_life: medium
review_by: 2027-10-29
status: active
superseded_by:
---
## 원칙

사용자는 수치와 사실 확인을 Claude 스레드 1개에 맡긴다. 조건은 2가지다. Claude 가 모든 수치의 1차 자료를 찾는다. Claude 가 그 자료가 믿을 만한 1차 자료인지 확인한다. 펠릭스는 이 조건이면 결과를 100% 신뢰한다고 말한다.

## 언제 쓰나

- 슬라이드, 보고서, 글에 수치와 사실 주장이 들어갈 때 쓴다.
- 팩트 체크 전용 에이전트를 따로 만들지 않는다. 펠릭스는 일반 Claude 스레드를 쓴다.
- 이 카드는 사실 확인만 다룬다. 주장과 해석의 타당성은 `adversarial-review-with-judge` 카드를 본다.

## 프롬프트 문장

```text
이 문서에 나오는 모든 수치와 사실 주장에 대해 1차 자료를 찾아 줘.
문서: [경로 또는 본문]
항목마다 출처 링크, 원문 인용, 그 자료가 신뢰할 만한 1차 자료인지에 대한 판정을 표로 정리해 줘.
2차 인용이나 블로그 재가공은 1차 자료로 인정하지 마.
1차 자료를 찾지 못한 항목은 따로 표시해 줘.
```

## 근거

- 펠릭스는 편집상의 사실 확인 결과를 이제 100% 신뢰한다고 말했다. 프레젠테이션 슬라이드의 모든 사실 확인을 맡기면 여러 번 확인할 필요가 없다. 펠릭스는 50개의 에이전트가 아니라 단 한 개의 에이전트를 전적으로 신뢰한다. [▶ 14:07](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=847s)
- 펠릭스가 쓰는 지시는 "제가 언급하는 모든 수치에 대한 1차 자료를 찾아 주세요. 그리고 그 자료가 믿을 만한 1차 자료인지 확인해 주세요." 다. [▶ 14:21](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=861s)
- 진행자가 사실 확인 전용 에이전트가 있는지 물었다. 펠릭스는 에이전트라는 개념이 너무 과하게 쓰인다고 답했다. [▶ 14:28](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=868s)
- 블로그 원문에는 이 방법이 없다. 그래서 source_url 은 원 인터뷰다.
- 주의: "100% 신뢰" 는 현재 모델에 대한 펠릭스 개인의 판단이다. 자막의 "이제" 는 이 판단이 최근에 생겼다는 뜻이다. 모델이 좋아지면 이 조언은 약해지지 않고 강해진다. 그래서 이 카드의 half_life 는 short 가 아니라 medium 이다. [▶ 14:07](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=847s)
- 주의: 위 ▶ 타임스탬프는 AgentOS 정리 영상 기준이다. 원 인터뷰의 해당 시점은 아직 찾지 않았다. 그래서 source_url 에 `&t=` 를 붙이지 않았다.
