---
id: role-sentence-roleplay-trap
title: 역할을 씌우면 말투만 바뀐다. 전문가의 방법과 도구를 쓰게 한다
type: anti-pattern
scope: agent-task
tags: [delegation, role-prompt, depth]
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

사용자는 "너는 뛰어난 회계사야" 같은 역할 문장을 쓰지 않는다. 많은 모델이 역할 문장을 받으면 역할극을 한다. 어휘는 바뀌지만 방법은 그대로다. 사용자가 원하는 것은 전문가의 기술, 도구, 지식이다. 그래서 사용자는 Claude 에게 이 분야 최고 전문가가 쓸 방법과 도구를 먼저 말하게 한다. 그다음 Claude 가 그 방법과 도구를 실제로 쓰게 한다. 이 카드는 역할 문장 하나를 방법과 도구 요청으로 바꾸는 일만 다룬다. 프롬프트 전체를 더 깊게 다시 쓰려면 `deeper-not-bigger` 카드를 쓴다.

## 언제 쓰나

- 프롬프트 첫 줄이 "너는 ○○ 전문가야" 로 시작할 때 쓴다.
- 결과물이 전문가 말투인데 근거와 계산이 얕을 때 쓴다.
- 사용자가 에이전트마다 정체성을 미리 정하려 할 때 쓴다. 펠릭스는 이 방식이 모델 활용을 제약한다고 본다.
- 다른 분야를 불러올 때도 쓴다. 공매도 투자자처럼 쓰게 하지 않는다. 공매도 투자자가 하는 일을 하게 한다.
- 이 카드의 범위는 agent-task 다. 출력 형식만 맞추는 API 호출에는 아래 근거의 충돌 항목을 본다.

## 프롬프트 문장

```text
이 작업을 시작하기 전에, 이 분야 최고 수준의 전문가가 쓸 방법, 도구, 데이터를 구체적으로 정리해 줘.
그다음 정리한 방법과 도구를 실제로 써서 작업해 줘. 말투를 흉내 내지 말고, 그 전문가가 하는 일을 해 줘.
예: 마크다운 표 대신 데이터베이스와 통계 모델, 그림 설명 대신 Blender 같은 실제 제작 도구.
설명은 쉬운 말로 써 줘.
```

## 근거

- 펠릭스는 "아주 훌륭한 회계사처럼 행동하라" 고 말하면 많은 모델이 역할극을 한다고 말했다. 펠릭스는 이것을 오늘날 대부분의 모델이 여전히 가진 문제라고 말했다. [▶ 21:50](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1310s)
- 펠릭스는 역할극이 원하는 바가 아니라고 말했다. 원하는 것은 전문가가 쓰는 기술, 도구, 지식이다. 다섯 살 아이에게 말하듯 설명하더라도 그 분야 최고의 도구를 모두 쓰길 바란다. [▶ 22:02](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1322s)
- 펠릭스는 Claude 에게 이 분야 최고 전문가가 어떤 도구를 쓸지 말해 달라고 한다. 그다음 똑같은 것을 써 달라고 한다. [▶ 21:40](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1300s)
- 펠릭스는 등장인물을 미리 정해 놓듯 접근하면 오히려 인공지능 활용에 제약을 둔다고 말했다. 펠릭스는 에이전트에게 자신이 누구인지 알려 주지 않았다. [▶ 15:29](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=929s)
- 펠릭스는 모델을 뛰어난 제너럴리스트로 본다. 근거로 수학 전용 모델의 은메달 뒤에 범용 모델이 금메달을 딴 사례를 들었다. [▶ 14:47](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=887s)
- 펠릭스는 3D 와 모션 영상에서 "블렌더를 쓰세요", "전문 애니메이터들이 쓰는 도구를 똑같이 쓰세요" 라는 지시가 큰 변화를 만들었다고 말했다. [▶ 07:45](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=465s)
- 블로그 원문은 모델이 "often switch vocabulary without actually switching methods" 라고 쓴다. 블로그는 공매도 투자자처럼 쓰게 하지 말고 공매도 투자자가 하는 일을 하게 하라고 쓴다. [Felix 블로그](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)
- 충돌: Anthropic 공식 문서는 출력 형식을 맞출 때 한 줄 역할 부여를 여전히 권한다. [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) 연구 보고서는 두 입장의 적용 층위가 다르다고 본다. 그래서 이 카드의 scope 는 agent-task 다.
- 주의: 역할극은 모델의 행동이다. 다음 모델에서 이 행동이 사라질 수 있다. 그래서 이 카드의 half_life 는 short 다.

## 지난 방식

- 2024년 무렵: "Claude, 당신은 정말 훌륭한 엔지니어니까 여기 있는 문제들을 좀 해결해 주세요" 라고 썼다. 펠릭스는 지금 이 문장을 쓰지 않는다. [▶ 21:20](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1280s)
