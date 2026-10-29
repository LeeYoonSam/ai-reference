---
id: skill-half-life-try-plain-prompt
title: 스킬은 금방 낡는다. 스킬 없는 기본 프롬프트와 비교한다
type: principle
scope: agent-task
tags: [context, skills, model-upgrade]
source_note: notes/2026-10-26_agentos_delegate-to-claude.md
source_url: "https://www.youtube.com/watch?v=D-SVFneJ_Nk"
author: Felix Rieseberg (Anthropic)
tier: T1
source_date: 2026-10-20
valid_as_of: 2026-10-29
model_context: Claude Opus 5.5, Claude Code v2.1
half_life: short
review_by: 2027-01-29
status: active
superseded_by:
---
## 원칙

좋은 스킬도 유효 기간이 짧다. 스킬에는 이전 세대 모델에 맞춘 지시가 들어간다. 새 모델에서는 그 지시가 결과를 떨어뜨릴 수 있다. 때로는 스킬을 완전히 빼면 결과가 더 좋다. 그래서 사용자는 스킬을 쓸 때와 뺄 때를 신중하게 정한다. 사용자는 스킬 없이 프롬프트만 보낸 결과와 비교한다.

## 언제 쓰나

- 새 모델이 나왔을 때 쓴다.
- 오래 쓴 스킬, CLAUDE.md, 반복해서 붙이는 지시문이 있을 때 쓴다.
- 이 비교는 결과의 좋고 나쁨을 판단할 수 있는 사람에게 가장 유용하다. 펠릭스도 이렇게 말한다.
- 이 라이브러리의 `/ref` 추천도 같은 규칙을 따른다. Claude 는 추천 프롬프트와 기본 프롬프트를 함께 낸다.

## 프롬프트 문장

사용자는 A 와 B 를 각각 새 세션에서 실행한다. Claude 는 아래 프롬프트로 두 결과의 차이 목록만 만든다. 어느 쪽이 나은지는 사용자가 판단한다. 펠릭스는 이 비교가 좋고 나쁨을 아는 사람에게 가장 유용하다고 말했다.

```text
같은 작업을 두 방식으로 실행한 결과의 차이를 정리해 줘. 어느 쪽이 나은지는 판정하지 마. 판정은 내가 한다.
작업 목표: [목표]
A: [스킬 이름] 을 쓴 실행 결과. 위치: [경로]
B: 스킬 없이 기본 프롬프트만 보낸 실행 결과. 위치: [경로]
판단 기준: [기준]
기준마다 A 와 B 가 어떻게 다른지 한 줄씩 적어 줘.
차이마다 그 차이를 만든 것으로 보이는 스킬의 지시를 인용해 줘.
```

사용자는 차이 목록을 보고 기준마다 나은 쪽을 정한다. B 가 같거나 나으면, 사용자는 그 스킬을 재검토한다.

## 근거

- 펠릭스는 스킬을 여전히 많이 쓴다고 말했다. 다만 Anthropic 의 공식 지침과 자신의 지침은 스킬 사용에 정말 신중하라는 것이다. [▶ 17:45](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1065s)
- 펠릭스는 모델에게 이전 세대 모델에 맞던 것을 알려 주는 경우가 많다고 말했다. AI 의 시간 압축이 심해서 좋은 스킬의 유효 기간은 매우 짧다. 때로는 스킬을 완전히 제거했을 때 더 나은 결과가 나온다. [▶ 17:56](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1076s)
- 대화는 "그냥 잊어버리고 프롬프트만 보내세요" 로 이어진다. [▶ 18:12](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1092s)
- 펠릭스는 이 방식이 아주 효과적이라고 말했다. 평가 경험이 있고 좋고 나쁨을 아는 사람에게 가장 유용하다. 펠릭스는 스킬을 언제 쓰고 언제 쓰지 않을지 매우 신중하게 판단한다. [▶ 18:17](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1097s)
- 정리 영상은 "좋은 스킬의 반감기는 짧다" 를 설명 슬라이드로 보여 준다. 이 구간에는 자막 발언이 없다. [▶ 19:43](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1183s)
- 펠릭스는 인터뷰 끝에서 오늘 한 조언도 10주 뒤에는 전부 새로 개정될 것이라고 말했다. [▶ 42:55](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=2575s)
- 블로그 원문은 스킬 반감기를 다루지 않는다. 블로그는 능력이 "every couple of weeks" 바뀐다고만 쓴다. 그래서 source_url 은 원 인터뷰다. [Felix 블로그](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)
- 합의: Fable 5 공식 문서는 "Skills developed for prior models are often too prescriptive for Claude Fable 5 and can degrade output quality" 라고 쓴다. [Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)
- 합의: Thariq Shihipar 는 Claude 5 세대 모델용 Claude Code 시스템 프롬프트에서 80% 이상을 지웠고 코딩 평가 손실이 없었다고 썼다. [Thariq 블로그 2026-07-24](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/)
- 합의: Boris Cherny 의 `/checkup` 은 Boris 자신의 설정에서 미사용 project skill 38개를 찾았다. [Boris X 2026-07-08](https://x.com/bcherny/status/2074997571563479143)
- 주의: 위 타임스탬프는 AgentOS 정리 영상 기준이다. 원 인터뷰의 해당 시점은 아직 찾지 않았다.
