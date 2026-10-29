---
id: adversarial-review-with-judge
title: 적대적 리뷰 여러 개를 돌리고 판사 Claude 가 타당한 비판만 거른다
type: pattern
scope: agent-task
tags: [verification, review, adversarial-review]
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

사용자는 결과물을 만든 Claude 와 별도로 리뷰 스레드 여러 개를 만든다. 각 리뷰 스레드의 유일한 목표는 결과물이 틀렸다는 것을 증명하는 것이다. 비판이 많아지면, 판사 Claude 가 각 비판이 타당한지 검증한다. 타당한 비판만 만든 Claude 에게 돌아간다. 만든 Claude 가 반영 여부를 정한다.

## 언제 쓰나

- 글, 슬라이드, 문서, 코드처럼 완성본이 있고 틀린 곳을 찾고 싶을 때 쓴다.
- 리뷰가 서로 다른 의견을 내서 무엇을 따를지 모를 때 판사 단계를 더한다.
- 리뷰 스레드에는 한 단계 낮은 모델을 써도 된다. 흠을 찾는 일이 새로 만드는 일보다 쉽기 때문이다.

## 프롬프트 문장

```text
[리뷰 스레드마다 따로 붙여 넣는다]
아래 결과물이 틀렸다는 것을 증명하는 것이 이 스레드의 유일한 목표다.
사실관계 오류, 잘못된 가정, 오해한 부분, 빠진 반론을 찾아 근거와 함께 제시해 줘. 칭찬은 하지 마.
결과물: [경로 또는 본문]

[판사 스레드에 붙여 넣는다]
아래는 리뷰 스레드 [N]개가 낸 비판 목록이다.
각 비판이 타당한지 검증해서 타당, 부분 타당, 기각으로 분류하고 이유를 붙여 줘.
핵심을 놓쳤거나, 실행할 수 없거나, 유용하지 않은 비판은 기각해 줘.
작성자에게 넘길 타당한 비판만 우선순위대로 정리해 줘.
```

## 근거

- 펠릭스는 AI 가 자신 있게 오류를 내는 문제의 해결책으로 적대적 검토를 제시했다. 적대적 검토는 코딩과 수학에서 효과가 수치로 확인됐다. 한 Claude 가 작업하고, 적대적 검토자 10개가 그 작업이 왜 틀렸는지 증명한다. 펠릭스는 이것을 레드팀이나 공매도와 같은 개념이라고 말했다. [▶ 09:00](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=540s)
- 펠릭스는 결함을 찾는 일이 새로 만드는 일보다 쉽다고 말했다. 그래서 지능 수준을 한 단계 낮춰도 좋은 결과를 얻는다. [▶ 09:31](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=571s)
- 펠릭스는 Claude Projects 에서 블로그 글 1편에 스레드 5개를 만든다. 각 스레드가 글이 틀렸다는 것, 사실관계가 틀렸다는 것, 무언가를 오해했다는 것을 증명한다. [▶ 10:11](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=611s)
- 피드백이 너무 많다는 진행자의 질문에, 펠릭스는 해답이 다시 Claude 라고 답했다. 펠릭스는 이것을 판단자라고 불렀다. [▶ 11:21](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=681s)
- 판단자 Claude 는 피드백이 타당한지 검증하고 의견을 붙인다. 타당한 피드백은 결과물을 만든 Claude 에게 돌아간다. 만든 Claude 가 조치 여부를 정한다. [▶ 11:36](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=696s)
- 펠릭스는 피드백이 합리적이어도 핵심을 놓쳤거나, 실행할 수 없거나, 유용하지 않은 경우가 있다고 말했다. [▶ 12:05](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=725s)
- 정리 영상은 3겹 구조를 설명 슬라이드로 보여 준다. 이 구간에는 자막 발언이 없다. [▶ 13:35](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=815s)
- 블로그 원문에는 판사 구조가 없다. 블로그는 크루를 모을 때 레드팀으로 공매도 투자자와 포렌식 회계사를 넣으라고만 쓴다. 그래서 source_url 은 원 인터뷰다.
- 공식 문서와의 합의는 `grade-outside-session` 카드에 있다.
- 주의: 위 ▶ 타임스탬프는 AgentOS 정리 영상 기준이다. 원 인터뷰의 해당 시점은 아직 찾지 않았다. 그래서 source_url 에 `&t=` 를 붙이지 않았다.
