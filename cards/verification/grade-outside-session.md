---
id: grade-outside-session
title: 만든 세션이 아니라 바깥에서 채점한다
type: principle
scope: agent-task
tags: [verification, review]
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

사용자는 작업을 한 세션에게 그 작업이 잘 됐는지 묻지 않는다. 방금 일한 세션은 자기 작업을 판단하는 데 서툴다. 펠릭스가 믿지 못하는 대상은 Claude 가 아니라 세션 하나다. 그래서 검증은 세션 바깥의 신호로 한다. 급하면 다른 Claude 세션을 쓴다. 가장 좋은 신호는 실제 지표 같은 외부 증거다.

## 언제 쓰나

- 사용자가 결과 확인을 만든 세션의 "잘 됐어?" 한 번으로 끝내고 있을 때 쓴다.
- 사용자가 좋은 결과가 무엇인지 모를 때 쓴다. 펠릭스는 이때 AI 를 더 쓰고 토큰을 더 넣으라고 말한다.
- 사용자가 좋은 결과를 알면, 과정은 몰라도 된다. 사용자는 의뢰인 자리에서 결과만 판단해도 충분할 수 있다.

## 프롬프트 문장

```text
작업을 마치면 스스로 잘 됐다고 판정하지 말아 줘.
먼저 너와 나 말고 무엇이 이 결과가 맞다는 걸 보여 줄 수 있는지 정해 줘. 예: 테스트 실행 결과, 보지 않은 데이터에서의 예측 결과, 실제 지표.
그 신호를 직접 확인할 수 있으면 확인하고 결과를 보여 줘.
직접 확인할 수 없으면, 다른 세션이 검증할 수 있게 확인 항목 목록을 만들어 줘.
```

## 근거

- 펠릭스는 "Claude 에게 신뢰하지 못하는 부분" 보다 "단 한 번의 세션만으로 신뢰하지 못하는 부분" 이 더 중요하다고 말했다. [▶ 22:57](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1377s)
- 펠릭스는 실행 중인 Claude 세션이 Claude Code, Cowork, 채팅, 프로젝트 어디에 있든 자기 작업이 제대로 됐는지 판단하는 데 서툴다고 말했다. [▶ 23:16](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1396s)
- 펠릭스는 가능한 한 외부 신호를 찾는다고 말했다. 급할 때는 다른 Claude 세션을 쓴다. 펠릭스는 확실한 외부 증거를 더 선호한다. 때로는 과정을 믿고 Claude 에게 시간을 줘야 한다. [▶ 23:28](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1408s)
- 진행자는 외부 지표의 예로 조회수를 들었다. [▶ 23:52](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1432s)
- 펠릭스는 두 경우를 나눴다. 좋은 결과를 모르면 AI 를 더 쓴다. 좋은 결과를 어느 정도 알면 과정에 대한 의견은 필요 없을 수 있다. [▶ 12:57](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=777s)
- 블로그 원문은 "Do _not_ ask the model to judge itself." 라고 쓴다. 블로그는 모델이 직접 실행해서 바로 피드백을 받는 도구를 바깥 심판으로 권한다. [Felix 블로그](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)
- 주의: 같은 블로그는 이 한계가 "eventually be solved with increasing model intelligence" 라고 본다. 블로그는 "in October 2026" 에는 바깥 검증을 고집하라고 쓴다. 그래서 이 카드의 half_life 는 long 이 아니라 medium 이다. [Felix 블로그](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)
- 합의: Fable 5 공식 문서는 "Separate, fresh-context verifier subagents tend to outperform self-critique" 라고 쓴다. [Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)
- 합의: Boris Cherny 는 Claude 에게 검증 수단을 주면 품질이 "2-3x" 오른다고 했다. [InfoQ](https://infoq.com/news/2026/01/claude-code-creator-workflow/) 연구 보고서는 이 원칙을 2026-01 부터 2026-10 까지 바뀌지 않은 원칙으로 본다.
- 주의: 위 ▶ 타임스탬프는 AgentOS 정리 영상 기준이다. 원 인터뷰의 해당 시점은 아직 찾지 않았다. 그래서 source_url 에 `&t=` 를 붙이지 않았다.

## 지난 방식

- 2024년 무렵: 사용자는 작업한 세션에게 결과가 잘 됐는지 물었다. 원 인터뷰 제목 "Stop Using Claude Like It's 2024" 와 정리 영상 슬라이드가 이 방식을 2024년식으로 부른다. 펠릭스가 이 방식에 날짜를 붙인 발언은 자막에 없다. [▶ 26:26](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1586s)
