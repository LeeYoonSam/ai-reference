---
id: open-raw-data-and-computer
title: 골라 준 요약 대신 원본 데이터와 컴퓨터를 열어 준다
type: principle
scope: agent-task
tags: [context, raw-data, tools]
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

사용자는 데이터를 잘라 주거나 요약해 주지 않는다. 사용자는 Claude 에게 원본 데이터와 직접 쓸 컴퓨터를 준다. 데이터가 너무 많으면, 사용자는 데이터를 가져오는 도구를 준다. 사용자는 각 도구가 어떤 데이터를 가져오는지 명확하게 설명한다. 펠릭스는 이 판단을 "모델 경험" 으로 한다. 모델 경험은 "내가 Claude 라면 이 일에 무엇이 필요한가" 를 묻는 것이다.

## 언제 쓰나

- 사용자가 Claude 에게 넘길 자료를 직접 고르고 정리하고 있을 때 쓴다.
- 사용자가 에이전트마다 데이터 조각을 나눠 주려 할 때 쓴다. 펠릭스는 일을 잘하려면 비즈니스 전체를 보는 시야가 필요하다고 본다.
- 처음 시작할 때는 커넥터를 만들지 않는다. Claude 가 브라우저와 컴퓨터를 직접 쓰게 한다. 워크플로가 잘 돌면, 그때 커넥터를 검토한다.
- 이 방식은 초기 준비 비용이 든다. 펠릭스는 그 비용이 충분히 가치 있다고 말한다.

## 프롬프트 문장

```text
내가 골라 둔 요약 대신 원본에서 시작해 줘.
원본 데이터: [위치. 예: 크래시 리포트 폴더, 고객 통화 기록, 판매 데이터베이스]
도구: [도구 이름] 은 [가져오는 데이터] 를 가져온다. [도구 이름] 은 [가져오는 데이터] 를 가져온다.
필요하면 이 컴퓨터에 소프트웨어를 설치하고 직접 재현해 봐도 된다.
어떤 데이터를 쓸지는 네가 판단해 줘. 결론마다 근거가 된 원본 위치를 적어 줘.
```

## 근거

- 펠릭스는 사용자 경험과 대비되는 모델 경험을 생각해 보라고 말했다. 자신이 Claude 라고 가정하면 원시 데이터 접근, 컴퓨터 접근, 소프트웨어 설치 권한을 원하게 된다. [▶ 18:30](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1110s)
- 펠릭스는 데이터를 여러 조각으로 나눠 에이전트에게 주는 방식에 반대했다. 업무를 효과적으로 하려면 전체 비즈니스에 대한 시야가 필요하다. [▶ 16:00](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=960s)
- 자막은 엔지니어링 관리자 예를 든다. 코드 접근 권한만 있을 때보다 고객 데이터와 고객 통화 기록까지 있을 때 훨씬 유용하다. [▶ 16:16](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=976s)
- 펠릭스는 방대한 데이터에는 도구를 주라고 말했다. 각 도구가 어떤 데이터를 가져오는지 명확하게 설명한다. 그러면 모든 데이터를 직접 넣을 필요가 없다. [▶ 16:39](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=999s)
- 펠릭스는 초기 비용이 정말 그만한 가치가 있다고 말했다. 동시에 초기 비용이 생긴다는 점도 고려하라고 말했다. [▶ 19:24](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1164s)
- 펠릭스는 데스크톱 앱으로 시작하라고 말했다. 커넥터와 데이터 다운로드는 잊고 Claude 에게 키보드를 넘긴다. 워크플로가 작동하면 대시보드 수동 클릭보다 나은 연결 수단을 검토한다. [▶ 20:15](https://www.youtube.com/watch?v=gV0CtvIX5zk&t=1215s)
- 블로그 원문은 모델이 소프트웨어를 설치할 수 있는 컴퓨터와 관련 데이터 접근이 필요하다고 쓴다. 펠릭스는 Claude 가 크래시 리포트를 가져오고, 앱 버전을 git 커밋에 대응시키고, 여러 운영 체제에서 재현과 검증을 하도록 작업 환경을 다시 만들었다. [Felix 블로그](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)
- 합의: Anthropic 의 context engineering 글은 파일 경로를 가벼운 식별자로 들고 있다가 필요할 때 읽으라고 권한다. [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
