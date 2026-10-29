---
id: feedback-to-rules
title: 내가 준 피드백을 모아 규칙 목록으로 바꾸고 리뷰 입력으로 쓴다
type: pattern
scope: agent-task
tags: [context, feedback, review]
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

사용자는 피드백이 실제로 오가는 장소를 먼저 찾는다. 사용자는 Claude 에게 그 도구의 접근 권한을 준다. 그다음 Claude 가 아래 3단계를 한다.

1. Claude 가 사용자가 지금까지 준 피드백을 모두 모은다.
2. Claude 가 그 피드백을 핵심 규칙과 원칙의 목록으로 줄인다.
3. 때때로 Claude 가 사용자가 믿지만 믿는 줄도 몰랐던 원칙을 찾는다.

사용자는 이 목록을 이후 리뷰의 입력 자료로 계속 쓴다.

## 언제 쓰나

- 팀원이나 Claude 의 결과물이 사용자 취향과 일부 다를 때 쓴다.
- 피드백이 Slack, GitHub, 텔레그램 같은 도구에 쌓여 있을 때 쓴다.
- 코딩이 아닌 업무에도 쓴다. 펠릭스는 고객 통화 녹취록에 대한 피드백을 예로 들었다.

## 프롬프트 문장

```text
[1단계] [피드백 장소. 예: Slack 채널, GitHub 리뷰 댓글, 문서 댓글] 에서 내가 지금까지 준 리뷰 피드백을 모두 모아 줘.
[2단계] 모은 피드백을 반복되는 패턴으로 묶어서, 다음 작업에 그대로 적용할 수 있는 규칙과 원칙 목록으로 줄여 줘. 규칙마다 대표 사례 1개를 붙여 줘.
[3단계] 내가 명시적으로 말한 적은 없지만 일관되게 따르는 숨은 원칙이 있으면 근거와 함께 제시해 줘.
```

완성된 목록은 이후 리뷰 요청에 입력 자료로 붙인다.

## 근거

- 진행자는 팀원의 결과물이 약 70% 는 비슷하고 30% 는 자신의 취향으로 달라진다고 말했다. 진행자는 이 피드백 루프를 어떻게 닫는지 물었다. [▶ 24:03](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1443s)
- 펠릭스는 피드백이 주로 이루어지는 장소를 먼저 파악하라고 답했다. [▶ 24:22](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1462s)
- 펠릭스는 Claude 가 GitHub, Slack 등 피드백이 있는 모든 곳에서 피드백을 찾아낸다고 말했다. 도구를 주면 사람이 피드백 목록을 따로 만들 필요가 없다. [▶ 25:06](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1506s)
- 펠릭스는 3단계 과정을 설명했다. 1단계는 모든 피드백 수집이다. 2단계는 핵심 규칙이나 원칙 목록으로 요약이다. [▶ 25:22](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1522s)
- 펠릭스는 3번째 라운드에서 믿는 줄도 몰랐던 원칙을 찾고, 그 목록을 지속적인 검토의 입력 자료로 쓴다고 말했다. 펠릭스는 이 방법이 효과가 좋았다고 말했다. [▶ 25:36](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1536s)
- 펠릭스는 코딩이나 텍스트가 아닌 업무도 비슷하게 접근할 수 있다고 말했다. 예: 고객 통화에 대한 피드백. [▶ 26:03](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1563s)
- 블로그 원문에는 이 방법이 없다. 그래서 source_url 은 원 인터뷰다.
- 합의: Boris Cherny 는 2026-01 에 Claude 가 틀릴 때마다 CLAUDE.md 에 규칙을 더하라고 했다. [Boris X 2026-01-02](https://x.com/bcherny/status/2007179832300581177)
- 주의: Boris 의 `/checkup` 은 2026-07 에 Boris 자신의 설정에서 매 세션 로드되는 약 10k 토큰의 CLAUDE.md 를 찾았다. [Boris X 2026-07-08](https://x.com/bcherny/status/2074997571563479143) Thariq Shihipar 는 Claude 5 세대 시스템 프롬프트에서 80% 이상을 지워도 코딩 평가 손실이 없었다고 썼다. [Thariq 블로그 2026-07-24](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/) 펠릭스는 규칙 목록을 리뷰의 입력 자료로 쓴다. 상시 로드되는 지시로 쓰라고 말하지 않았다.
- 주의: 위 ▶ 타임스탬프는 AgentOS 정리 영상 기준이다. 원 인터뷰의 해당 시점은 아직 찾지 않았다. 그래서 source_url 에 `&t=` 를 붙이지 않았다.
