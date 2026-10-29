---
id: set-absurd-goal
title: 목표는 일부러 터무니없이 높게 잡고 해 볼 만하다고 말해 준다
type: pattern
scope: agent-task
tags: [delegation, depth, goal]
source_note: notes/2026-10-26_agentos_delegate-to-claude.md
source_url: "https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/"
author: Felix Rieseberg (Anthropic)
tier: T1
source_date: 2026-10-13
valid_as_of: 2026-10-29
model_context: Claude Opus 5.5, Claude Code v2.1
half_life: short
review_by: 2027-01-29
status: active
superseded_by:
---
## 원칙

사용자는 목표를 실제로 필요한 수준보다 훨씬 높게 잡는다. 예: 지금 10초 걸리는 페이지를 5초로 줄여야 하면, 사용자는 Claude 에게 0.2초를 요구한다. 그리고 사용자는 Claude 에게 그 목표가 충분히 해 볼 만하다고 말한다.

## 언제 쓰나

- 성능, 비용, 시간처럼 숫자로 잴 수 있는 목표가 있을 때 쓴다.
- 사용자가 목표를 가능해 보이는 만큼으로 낮춰 잡고 있을 때 쓴다. 펠릭스는 사람들이 실제로 가능한 것이 아니라 가능하다고 믿는 것에 갇혀 왔다고 말한다.
- 높은 목표가 모델의 한계에 닿아도 쓴다. 펠릭스는 그 한계를 최전선에 있다는 신호로 본다.

## 프롬프트 문장

```text
지금 [지표. 예: 페이지 로딩 시간] 은 [현재 값. 예: 10초] 이다. 실제로 필요한 값은 [필요 값. 예: 5초] 이다.
목표는 [필요 값보다 훨씬 높은 값. 예: 0.2초] 로 잡는다. 이 목표는 충분히 해 볼 만하다.
목표에 닿는 방법을 찾아 줘.
도중에 막히면, 어디에서 막혔는지와 그때까지 측정한 최선 값을 보여 줘.
```

## 근거

- 블로그 원문은 Depth 기법으로 터무니없는 목표를 든다. 원문의 예는 10초 로딩을 200밀리초로 줄이라고 요구하고, 모델에게 그 목표가 합리적이라고 말하는 것이다. [Felix 블로그](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)
- 정리 영상은 "지금 10초, 필요한 건 5초, 요구는 0.2초" 를 설명 슬라이드로 보여 준다. 이 구간에는 자막 발언이 없다. [▶ 27:16](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1636s)
- 펠릭스는 사람들이 항상 가능하다고 생각하는 것에 갇혀 있었고, 실제로 가능한 것에 갇히지 않았다고 말했다. [▶ 34:12](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=2052s)
- 펠릭스는 "돈이나 벌어라" 같은 목표에는 아직 한계가 있다고 말했다. 그 한계에 부딪히면 최전선에 있다는 것을 알게 되고, 차세대 모델에서 큰 이점을 얻는다. [▶ 35:12](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=2112s)
- 정리 영상은 블로그의 조지 단치히 이야기를 설명 슬라이드로 보여 준다. 1939년 UC 버클리 대학원생 단치히는 칠판의 미해결 문제 2개를 숙제로 알고 풀었다. 이 구간에는 자막 발언이 없다. [▶ 36:00](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=2160s)
- 주의: "해 볼 만하다고 말해 준다" 의 효과를 잰 수치는 요약 노트와 자막에 없다.
