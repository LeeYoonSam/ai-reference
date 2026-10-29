---
id: deeper-not-bigger
title: 맡기기 전에 깊이 프롬프트의 4가지 질문을 먼저 묻는다
type: prompt
scope: agent-task
tags: [delegation, depth, prompt]
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

사용자는 작업을 맡기기 직전에 Claude 에게 이 작업의 더 깊은 버전을 먼저 묻는다. 더 큰 버전을 묻지 않는다. Claude 는 아래 4가지 질문에 답한 뒤 사용자의 프롬프트를 다시 쓴다. 이 카드는 프롬프트 전체를 4가지 질문으로 다시 쓰는 일을 다룬다. 역할 문장 하나만 고칠 때는 `role-sentence-roleplay-trap` 카드를 쓴다.

1. 이 분야 최고의 전문가는 사용자가 요청하지 않은 무엇을 할까.
2. 이미 정리된 자료 대신 어떤 날것의 재료에서 시작할까.
3. 어떤 구체적인 방법과 도구를 쓸까.
4. Claude 와 사용자 말고 무엇이 결과가 맞다는 것을 보여 줄까.

## 언제 쓰나

- 사용자의 프롬프트가 "좋게 해 줘" 수준에 머물 때 쓴다.
- 사용자가 그 분야의 좋은 방법이나 도구를 모를 때 쓴다.
- 사용자가 작업의 양이 아니라 깊이를 원할 때 쓴다.

## 프롬프트 문장

블로그 원문이다.

```text
I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this field would do here that I'm not asking for; (2) name the rawest material they would start from instead of what has already been digested for me; (3) name the specific methods and tools they would use; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that.
```

한국어 버전이다.

```text
이 작업을 더 크게가 아니라 더 깊게 하고 싶어. 다시 쓰기 전에:
(1) 이 분야 최고의 전문가라면 내가 요청하지 않았지만 여기서 했을 일을 말해 줘.
(2) 이미 누군가 정리해 둔 것 대신, 그들이 시작했을 가장 날것의 재료가 뭔지 말해 줘.
(3) 그들이 쓸 구체적인 방법과 도구를 말해 줘.
(4) 너나 나 말고, 무엇이 이 결과가 맞다는 걸 보여 줄지 말해 줘.
그런 다음, 정확히 그걸 요구하도록 내 프롬프트를 다시 써 줘.
```

## 근거

- 4가지 질문의 원문은 펠릭스의 블로그에 있다. [Felix 블로그](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)
- 정리 영상은 이 프롬프트를 설명 슬라이드로 보여 준다. 이 구간에는 자막 발언이 없다. [▶ 27:01](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1621s)
- 펠릭스는 지식 노동에서는 좋은 결과물을 요구하기보다 중간 단계를 거치는 것이 더 중요하다고 말했다. 펠릭스는 그 분야 최고의 전문가가 어떻게 일하는지 살펴본다고 말했다. [▶ 06:13](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=373s)
- 펠릭스는 Claude 가 "이런 결과물을 원해요" 보다 "이 분야 전문가처럼 똑같은 단계를 밟아 보세요" 를 훨씬 잘 받아들인다고 말했다. [▶ 07:28](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=448s)
- 펠릭스는 날씨 예시를 들었다. 추측으로 맞힌 온도는 좋은 결과가 아니다. 위치를 찾고 믿을 만한 데이터 소스를 쓴 0.5도 오차가 더 나은 결과다. [▶ 04:54](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=294s)
- 질문 1과 3은 `role-sentence-roleplay-trap` 카드와 이어진다. 질문 2는 `open-raw-data-and-computer` 카드와 이어진다. 질문 4는 `grade-outside-session` 카드와 이어진다.
