---
id: delegate-goal-not-task
title: 작업을 하나씩 집어 주지 말고 목표로 맡긴다
type: principle
scope: agent-task
tags: [delegation, altitude, goal]
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

사용자는 개별 작업 대신 그 작업이 이루려는 결과를 목표로 준다. 예: "이 크래시 고쳐 줘" 대신 "앱을 크래시 없이 유지해 줘" 라고 맡긴다. Claude 가 무엇을 먼저 하고 무엇을 하지 않을지 스스로 판단한다. 판단에 필요한 원본 데이터를 여는 방법은 `open-raw-data-and-computer` 카드를 본다. 펠릭스의 블로그는 이 방향을 Altitude 라고 부른다. 정리 노트는 이것을 "고도" 로 옮긴다.

## 언제 쓰나

- 사용자가 같은 종류의 작업을 Claude 에게 하나씩 넘기고 있을 때 쓴다. 이것은 사용자가 컨베이어 벨트 역할을 한다는 신호다.
- 사용자가 "다음에 무슨 일이 일어나길 원하나" 에 답할 수 있을 때 쓴다. 그 답이 목표가 된다.
- 목표가 "돈 벌어 와" 처럼 너무 넓으면, 지금 모델로는 큰 성과가 나지 않는다. 펠릭스는 이 한계를 최전선에 있다는 신호로 본다. 사용자는 같은 목표를 다음 세대 모델에서 다시 시도한다.

## 프롬프트 문장

```text
이번 일은 개별 작업이 아니라 목표로 맡길게.
목표: [결과. 예: 우리 앱을 크래시 없이 유지한다]
이유: [이 목표가 필요한 이유]
데이터: [원본 데이터 위치. 예: 크래시 리포트 전체]
무엇을 먼저 하고 무엇은 하지 않아도 되는지 직접 판단해서 진행해 줘. 판단마다 근거를 한 줄로 적어 줘.
검증: [결과가 맞는지 보여 줄 바깥 신호. 예: 직접 재현한 뒤 수정을 확인, 다음 주 크래시 수]
```

## 근거

- 펠릭스는 1년 반 전에 크래시를 하나씩 집어 Claude 앞에 놓았다고 말했다. 펠릭스는 자신이 "클로드의 컨베이어 벨트" 였다고 말했다. [▶ 19:01](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1141s)
- 펠릭스는 Claude 가 모든 크래시 데이터에 접근하고, 고칠 것과 고치지 않을 것을 스스로 판단해야 한다고 말했다. [▶ 19:17](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1157s)
- 펠릭스는 다음에 어떤 결과가 나오길 바라는지 생각하고, 그 목표를 모델에 계속 주라고 말했다. [▶ 34:51](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=2091s)
- 펠릭스는 Claude 에게 "돈이나 벌어라" 라고만 하면 아직 큰 성과가 나지 않는다고 말했다. 그 한계에 부딪히면 최전선에 있다는 뜻이라고 말했다. [▶ 35:12](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=2112s)
- 블로그 원문은 크래시 사례를 "Eventually I asked Claude to simply keep our apps crash-free." 로 쓴다. 블로그는 분기 보고를 3층으로 올리는 예도 든다. 1층 문장은 "Tell me what changed this quarter, why, and what we should do about it." 이다. 블로그는 "Claude, go make money" 가 2026년에는 대부분의 사업에서 그것만으로 통하지 않는다고 쓴다. 블로그는 모델이 강해질수록 더 높은 추상 수준에서 일한다고 쓴다. [Felix 블로그](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)

## 지난 방식

- 인터뷰 시점의 약 1년 반 전: 펠릭스는 크래시를 하나씩 골라 "이것도 고쳐 줘" 라고 넘겼다. 펠릭스는 이 방식을 버렸다. [▶ 19:01](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1141s)
