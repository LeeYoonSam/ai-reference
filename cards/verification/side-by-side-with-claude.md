---
id: side-by-side-with-claude
title: 넘기기 불안하면 내 피드백과 Claude 의 피드백을 나란히 비교한다
type: pattern
scope: agent-task
tags: [verification, review, delegation]
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

사용자가 병목인데 일을 한 번에 넘기기 불안하면, 사용자는 먼저 나란히 비교한다. 사용자는 문서를 읽고 피드백을 적는 일을 몇 번 반복한다. 그다음 같은 문서에 Claude 가 줄 피드백과 비교한다. 사용자는 같은 곳과 다른 곳을 본다. 다른 곳에서 워크플로를 개선할 지점이 보인다. 두 피드백이 완벽히 같을 필요는 없다.

## 언제 쓰나

- 모든 결과물이 사용자를 거쳐서 사용자가 회사의 병목일 때 쓴다.
- 사용자가 리뷰 권한을 하루아침에 모두 넘기기 불안할 때 쓴다.
- 비교에서 나온 차이를 규칙으로 만들려면 `feedback-to-rules` 카드를 함께 쓴다.

## 프롬프트 문장

사용자는 아래 두 메시지를 같은 세션에 차례로 보낸다. 1번 메시지에는 사용자의 피드백 A 를 넣지 않는다. Claude 가 A 를 먼저 읽으면 B 가 A 를 따라가기 때문이다.

```text
[1번 메시지]
아래 문서를 리뷰해서 피드백을 써 줘. 이 피드백을 B 라고 부른다.
문서: [경로 또는 본문]

[2번 메시지. B 를 받은 뒤에 보낸다]
아래는 같은 문서에 내가 먼저 남긴 리뷰 피드백 A 다.
피드백 A: [경로 또는 본문]
A 와 B 를 비교해서 둘 다 지적한 것, 나만 지적한 것, 너만 지적한 것으로 나눠 줘.
나만 지적한 것이 생긴 이유를 추정해 줘. 예: 네가 몰랐던 맥락, 내 취향.
그 이유를 다음 리뷰에 적용할 규칙으로 적어 줘.
```

## 근거

- 진행자는 모든 결과물이 팀을 거쳐 결국 자신을 거치므로 자신이 회사의 가장 큰 병목이라고 말했다. [▶ 27:36](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1656s)
- 펠릭스는 가장 먼저 할 일이 두 가지를 나란히 비교해 보는 것이라고 말했다. 펠릭스는 거의 모든 사람에게 이 실험을 추천한다. [▶ 27:49](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1669s)
- 펠릭스는 신뢰 문제로 모든 권한을 하루아침에 넘기기 내키지 않으면 나란히 비교하라고 말했다. 사용자가 피드백을 몇 번 적은 뒤, Claude 가 어떤 피드백을 줬을지 비교한다. 다른 곳과 같은 곳을 보면 워크플로 개선 지점을 찾는다. [▶ 27:55](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1675s)
- 펠릭스는 모델이 여전히 완벽하지 않다고 말했다. 같은 사람도 같은 문서를 월요일과 금요일에 다르게 검토한다. [▶ 28:17](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1697s)
- 정리 영상은 이 방식을 설명 슬라이드로 보여 준다. 이 구간에는 자막 발언이 없다. [▶ 29:07](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1747s)
- 블로그 원문은 새 분기 보고 방식을 지금 방식 옆에서 한 분기 동안 돌리라고 쓴다. 원문은 "run it beside the current one for a quarter." 다. [Felix 블로그](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) 블로그는 프로세스를 비교한다. 인터뷰는 피드백을 비교한다. 그래서 source_url 은 원 인터뷰다.
- 주의: 위 ▶ 타임스탬프는 AgentOS 정리 영상 기준이다. 원 인터뷰의 해당 시점은 아직 찾지 않았다. 그래서 source_url 에 `&t=` 를 붙이지 않았다.

## 지난 방식

- 2024년 무렵: 사용자는 모든 결과물을 직접 검토했다. 원 인터뷰 제목 "Stop Using Claude Like It's 2024" 와 정리 영상 슬라이드가 이 방식을 2024년식 "내가 다 본다" 로 부른다. 펠릭스가 이 방식에 날짜를 붙인 발언은 자막에 없다. [▶ 29:07](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1747s)
