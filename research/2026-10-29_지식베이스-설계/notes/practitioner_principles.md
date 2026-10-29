# 최상위 AI 플랫폼 빌더의 Claude 위임 원칙 (2026-10-29 기준)

> 조사 범위: Boris Cherny, Thariq Shihipar, Cat Wu, Anthropic 공식 문서, Felix Rieseberg 원문, 그리고 Anthropic 외부의 Karpathy·Simon Willison·OpenAI Codex.
> 표기 규칙:
> - **[1차]** 는 본인의 글·스레드·공식 문서다.
> - **[2차]** 는 요약 사이트·기사다. 원문 확인이 필요하다.
> - **[미검증]** 은 조사자의 사전 지식이다. 이번 세션에서 URL 을 다시 열지 않았다.
> - 날짜는 원문 게시일이다.

---

## Q1. Boris Cherny (Claude Code 창시자) 의 공개 워크플로우와 팁

### Takeaway
Boris 의 조언은 2026 년 1월에서 10월 사이에 크게 변했다. 1월에는 "병렬 세션 + plan mode + CLAUDE.md 에 규칙 추가 + 검증 루프" 였다. 6월 이후에는 "auto mode + 최소 컨텍스트 + 자동화가 메타 스킬 + 검증을 PR 에 강제" 로 바뀌었다. 모든 시기에 공통인 1순위 원칙은 **Claude 에게 스스로 검증할 수단을 준다** 이다.

### Cited Findings

**2026-01-02 스레드 (Part 1, 13 tips)** — [1차 X](https://x.com/bcherny/status/2007179832300581177), 인덱스: [2차 howborisusesclaudecode.com](https://howborisusesclaudecode.com/)
- Boris 는 별도 git checkout 에서 Claude 5 개를 병렬로 돌린다. 입력 요청은 알림으로 잡는다.
- Boris 는 Plan mode 로 시작하고, 계획이 맞으면 auto-accept 로 넘긴다.
- 팀은 공유 CLAUDE.md 를 git 에 둔다. Claude 가 틀릴 때마다 규칙을 추가한다.
- 반복 작업은 slash command 와 subagent 로 만든다. `--dangerously-skip-permissions` 대신 안전한 명령을 미리 허용한다.
- 가장 큰 팁: Claude 에게 작업을 검증할 수단을 주면 품질이 "2-3x" 오른다. — [2차 InfoQ](https://infoq.com/news/2026/01/claude-code-creator-workflow/)

**2026-01-31 스레드 (Part 2, 팀에서 모은 10 tips)** — [1차 X](https://x.com/bcherny/status/2017742741636321619), 미러: [2차 gist](https://gist.github.com/joyrexus/e20ead11b3df4de46ab32b4a7269abe0)
- Boris 는 "there is no one right way to use Claude Code" 라고 전제한다. — [1차 X](https://x.com/bcherny/status/2017742741636321619)
- 3–5 개 git worktree 를 병렬로 쓴다.
- 복잡한 작업은 plan 부터 한다. 일이 틀어지면 계속 밀지 않고 다시 plan 으로 돌아간다.
- 한 Claude 가 plan 을 쓰고, 두 번째 Claude 가 "staff engineer" 로서 그 plan 을 리뷰한다. — [2차 gist](https://gist.github.com/joyrexus/e20ead11b3df4de46ab32b4a7269abe0)
- 사용자가 Claude 를 교정한 뒤, Claude 에게 CLAUDE.md 를 고쳐 같은 실수를 반복하지 않게 하라고 시킨다.
- 하루에 두 번 이상 하는 일은 skill 이나 slash command 로 만들어 git 에 커밋한다.
- 버그는 Slack 스레드·CI 로그·Docker 로그를 통째로 주고 "fix" 만 지시한다. 예: "Go fix the failing CI tests." — [2차 gist](https://gist.github.com/joyrexus/e20ead11b3df4de46ab32b4a7269abe0)
- 도전 프롬프트 (원문):
  - "Grill me on these changes and don't make a PR until I pass your test." — [2차 howborisusesclaudecode.com](https://howborisusesclaudecode.com/). gist 미러에는 이 문구가 없다. 원 스레드 확인이 필요하다.
  - "Prove to me this works."
  - "Knowing everything you know now, scrap this and implement the elegant solution."
- 상세 spec 을 먼저 쓴 뒤 넘긴다. 긴 프롬프트는 음성 받아쓰기로 입력한다. "use subagents" 를 붙여 메인 컨텍스트를 깨끗하게 유지한다.

**2026-02 ~ 04 기능 중심 스레드** — [2차 인덱스](https://howborisusesclaudecode.com/)
- 2026-02-11: settings.json 을 git 에 체크인한다. 당시 Boris 는 모든 작업에 effort High 를 썼다. — [1차 X](https://x.com/bcherny/status/2021699851499798911)
- 2026-02-20: `claude --worktree`, agent frontmatter 의 `isolation: worktree`. — [1차 X](https://x.com/bcherny/status/2025007393290272904)
- 2026-02-27: `/simplify` 는 병렬 리뷰 에이전트를 돌린다. `/batch` 는 마이그레이션을 계획하고 worktree 에이전트 수십 개가 각각 PR 을 연다. — [1차 X](https://x.com/bcherny/status/2027534984534544489)
- 2026-03-24: auto mode 는 안전 분류기로 대부분의 권한 프롬프트를 대체한다. — [1차 X](https://x.com/bcherny/status/2036555259997462541)
- 2026-04 (Opus 4.7): 교정 대신 rewind 한다. `/compact` 와 `/clear` 를 의도적으로 구분한다. 위임할 때는 full brief 를 준다. — [2차 인덱스](https://howborisusesclaudecode.com/), 관련 [1차 Cat Wu X](https://x.com/_catwu/status/2044808533905178822), [1차 Boris X](https://x.com/bcherny/status/2044847848035156457)
- 2026-05-11~12: `/goal` 은 지정한 조건이 충족될 때까지 Claude 가 계속 일하게 한다. — [1차 X](https://x.com/bcherny/status/2053982327123132846), [1차 ClaudeDevs X](https://x.com/ClaudeDevs/status/2054351031279186040)

**2026-05-28 Opus 4.8 + dynamic workflows** — [1차 X](https://x.com/bcherny/status/2060048877944778995)
- Dynamic workflow 는 수백 개 병렬 subagent 를 돌린다. 프롬프트에서 막히지 않도록 auto mode 를 쓴다.
- Boris 는 이후 트리거 문구를 "use a workflow" 로 다듬었다. 단독 단어 "workflow" 는 오탐이 많았다. — [2차 인덱스](https://howborisusesclaudecode.com/)

**2026-06-08 "1년 회고"** — [1차 X](https://x.com/bcherny/status/2064034799711588805), [1차 영상](https://www.youtube.com/watch?v=Hth_tLaC2j8)
- Opus 4.6 이후 모델에서는 auto mode 가 plan mode 를 대체한다. Boris: 새 모델은 "don't actually need a planning step." — [2차 인덱스 요약](https://howborisusesclaudecode.com/)
- 무거운 프롬프트보다 최소 컨텍스트를 선호한다.
- Claude 가 틀리면, 다시 프롬프트하지 않고 CLAUDE.md 나 skill 에 규칙을 쓴다.

**2026-06-09 Fable 5** — [1차 X](https://x.com/bcherny/status/2064402671898075579)
- Boris: "Fable is the best model I have used for coding, by a wide margin."
- 요약 사이트는 이를 "less prompts and steers" 방향, 즉 최소주의와 위임으로 정리한다. — [2차](https://howborisusesclaudecode.com/)

**2026-07-08 `/checkup`** — [1차 X](https://x.com/bcherny/status/2074997571563479143)
- `/checkup` 은 Claude Code 설치 전체를 감사한다. Boris 자신의 설정에서 미사용 project skill 38 개와 매 세션 로드되는 약 10k 토큰의 CLAUDE.md 를 찾았다.

**2026-07-15 "Automation Is the Meta-Skill"** — [1차 X](https://x.com/bcherny/status/2077460395279692197)
- 원문 원칙: "a rejected PR is a failure of automation."
- 지식은 "the CLAUDE.md's, REVIEW.md's, skills, and docs that let agents work in their codebase" 에 넣는다.
- 고친 내용은 코드로 옮겨, 같은 종류의 버그를 자동으로 잡게 한다.

**2026-08-13 "Claude Maintains the Apps"** — [1차 X](https://x.com/bcherny/status/2088014489438621990)
- 루틴이 PR 388 개를 열고 180 개가 머지됐다. 머지율은 약 46% 다.
- PR 요구 조건 원문: "each pr must run /verify and post a repro and truth table to the pr."
- 원칙: PR 을 고치지 말고 루틴을 고친다. 모든 PR 은 Claude Code Review 와 사람 리뷰를 거친다.

**2026-09-10 diff 읽기** — [1차 X](https://x.com/bcherny/status/2098165206296011059)
- Boris: "I read diffs when it's touching critical code, or code that's important to get right."
- Ink renderer 는 "a black box with a ton of property-based tests and benchmarks" 로 다룬다. "Claude maintains it for us."

### Inferences
- Boris 의 흐름은 "사람이 매 세션을 조종" 에서 "사람이 검증 장치와 루틴을 설계" 로 이동했다. Felix 의 "grade outside the session" 과 같은 방향이다.
- 1월의 "틀릴 때마다 CLAUDE.md 에 규칙 추가" 는 7월의 `/checkup` 결과 (10k 토큰 CLAUDE.md) 와 충돌한다. 규칙 추가와 정기적 가지치기를 함께 해야 한다.

### Gaps
- 2026-10 의 Boris 스레드는 찾지 못했다. 인덱스 사이트의 최신 항목은 2026-09-25 다.
- X 원문은 직접 열지 못했다. 원문 문구는 요약 사이트를 거쳐 인용했다.

---

## Q2. Anthropic 의 다른 사람들과 공식 문서

### Takeaway
2026 년 Anthropic 공식 메시지는 "덜 지시하고, 이유를 주고, 판단을 맡기고, 검증은 별도 컨텍스트에서" 다. Thariq 는 Claude Code 시스템 프롬프트의 80% 이상을 지웠다. 공식 문서는 이전 모델용 skill 이 오히려 품질을 떨어뜨릴 수 있다고 명시한다.

### Cited Findings

**Thariq Shihipar, "The new rules of context engineering for Claude 5 generation models" (2026-07-24)** — [1차 블로그](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/), [1차 X](https://x.com/trq212/status/2080710971228918066)
- "We removed over 80% of Claude Code's system prompt for models like Claude Opus 5 and Claude Fable 5 with no measurable loss on our coding evaluations."
- "we were overconstraining Claude Code, both through our system prompt and in our CLAUDE.md files and skills."
- 충돌 예: "leave documentation as appropriate" 와 "DO NOT add comments" 가 같은 요청 안에 있었다.
- 6 개 신화와 대체 원칙:
  - 규칙 주기 → 판단 맡기기: "newer models have better judgement and can handle these decisions well without explicit rules."
  - 예시 주기 → 인터페이스 설계: "giving examples actually constrains them to a certain exploration space."
  - 전부 앞에 넣기 → progressive disclosure: "consider having a tree of files that can be loaded at the right time"
  - 반복하기 → 짧은 tool 설명. 도구 사용법은 시스템 프롬프트가 아니라 tool 설명에 둔다.
  - CLAUDE.md 에 기억 저장 → auto-memory.
  - 단순 spec → 풍부한 레퍼런스: "a HTML mockup of a design will generally produce better results than a description of the design or a screenshot."
- 새 규칙 예: "Write code that reads like the surrounding code: match its comment density, naming, and idiom."
- TodoWrite tool 설명은 약 9,100 자에서 "Create and update a task list for the current session" 한 줄과 상태 enum 으로 줄었다.
- CLAUDE.md: "Keep your CLAUDE.md lightweight ... spend most of the tokens on gotchas inside of the codebase." "Avoid stating 'the obvious' things Claude should know by looking at your file system or your repo."
- Skill: "think of skills as lightweight guides to let Claude find information when needed." "Avoid making them overconstrained, except in highly important areas."
- 루브릭: "Rubrics allow Claude to try and verify your taste in a particular field" — dynamic workflow 와 verifier agent 에 루브릭을 준다.
- `/doctor` 가 skill 과 CLAUDE.md 의 크기를 조정한다.
- 이 글은 대문자 강조 (CAPS) 나 역할 프롬프트를 직접 다루지 않는다.

**Thariq 외, 기타 스레드** — [2차 인덱스](https://howborisusesclaudecode.com/)
- 2026-06 "A Harness for Every Task" (Thariq, Sid Bidasaria): workflow 는 3 가지 실패를 막는다. agentic laziness, self-preferential bias, goal drift 다. 6 개 패턴은 classify-and-act, fan-out-and-synthesize, adversarial verification, generate-and-filter, tournament, loop-until-done 이다. Thariq: "Most traditional coding tasks do not need a panel of 5 reviewers." — [1차 X](https://x.com/trq212/status/2061907337154367865)
- 2026-07-03 "Finding Your Unknowns" (Thariq): "the map is not the territory." "reducing and planning for your unknowns is the skill of agentic coding." 코딩 전에 "blindspot pass" 를 요청한다. "Interview me one question at a time about anything ambiguous." implementation-notes.md 에 계획과 달라진 점을 기록한다. 머지 전에 Claude 에게 변경 내용으로 자신을 퀴즈하게 한다. — [1차 X](https://x.com/trq212/status/2073100352921215386)
- 2026-07-06 Loops (ClaudeDevs): "Every prompt you send is already a loop." "never call a UI change done from a successful edit alone." — [1차 X](https://x.com/ClaudeDevs/status/2074208949205881033)
- 2026-09-25 effort (Thariq): effort 는 "an approximation of how much compute you want it to spend on the task." 작업별로 low·medium·high·max 를 고른다. 루프는 interview → low 로 구현 → low 로 리뷰 → high 로 검증이다. 높은 effort 는 "does not fix when the model has the wrong approach." — [1차 X](https://x.com/trq212/status/2103576349499855160)

**공식 문서: Prompting best practices (현행, Fable 5.1 ~ Haiku 4.5 대상)** — [1차 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Claude 를 "a brilliant but new employee who lacks context on your norms and workflows" 로 대한다.
- 핵심 테스트: 맥락이 적은 동료에게 프롬프트를 보여 준다. 동료가 헷갈리면 Claude 도 헷갈린다.
- 이유를 준다. "NEVER use ellipses" 보다 TTS 엔진이 읽는다는 이유를 붙인 문장이 낫다. "Claude can generalize from the explanation."
- 예시는 여전히 권장한다. 3–5 개, `<example>` 태그로 감싼다.
- XML 태그는 여전히 권장한다. 지시·맥락·예시·입력이 섞일 때 쓴다.
- 역할 부여도 여전히 권장한다. "Even a single sentence makes a difference."
- 과잉 프롬프트를 줄인다. "If in doubt, use [tool]" 같은 문장은 과다 호출을 일으킨다. 이전 모델용 anti-laziness 프롬프트는 줄인다.
- prefill 은 Claude 4.6 부터 지원하지 않는다. `budget_tokens` 는 4.7 이상에서 400 에러다. 사고 깊이는 effort 로 조절한다.
- subagent 과다 사용을 경계한다. Opus 4.6 과 Opus 5 는 단순 grep 으로 충분한 경우에도 subagent 를 띄운다.

**공식 문서: Prompting Claude Fable 5** — [1차 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)
- "Skills developed for prior models are often too prescriptive for Claude Fable 5 and can degrade output quality. Review and consider removing older instructions if default performance is better."
- "Separate, fresh-context verifier subagents tend to outperform self-critique."
- "Start at the top of your difficulty range." 이전 모델에 주던 것보다 어려운 작업을 주고, Claude 가 범위를 잡고 질문하게 한다.
- 지시 준수가 좋아져서, 행동을 하나씩 나열하지 않고 짧은 지시 한 줄로 조종한다.
- "Give the reason, not only the request" — 템플릿은 Q5 에 있다.
- 진행 보고는 이번 세션의 tool 결과로 감사하게 한다. Anthropic 테스트에서 이 지시가 꾸며낸 상태 보고를 "nearly eliminated" 했다.
- 추론을 응답 본문에 다시 쓰라고 지시하지 않는다. 이 지시는 `reasoning_extraction` 거부를 일으킬 수 있다. "show your thinking" 류 지시는 감사해서 지운다.
- 메모리 시스템을 만들어 준다. 한 파일에 한 교훈을 쓰게 한다.

**Anthropic 엔지니어링 블로그**
- "Claude Code best practices" 원 블로그 글은 더 이상 유지되지 않는다. 현행 지침은 공식 docs 에 있다. — [1차](https://www.anthropic.com/engineering/claude-code-best-practices)
- "Effective harnesses for long-running agents": 새 컨텍스트가 상태를 빨리 잡도록 git 기록 옆에 progress 파일 (claude-progress.txt) 을 둔다. — [1차](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- "Effective context engineering for AI agents" (2025-09): compaction 은 아키텍처 결정과 미해결 버그를 남기고 중복된 tool 출력을 버린다. — [1차](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). [미검증] 같은 글은 "smallest possible set of high-signal tokens" 와 시스템 프롬프트의 "right altitude" 를 말한다.
- "How we contain Claude across products" (2026-05-25): 사용자는 권한 프롬프트의 약 93% 를 승인했다. 그래서 팀은 매 동작 승인보다 격리 (containment) 에 기댄다. — [2차 검색 요약](https://www.anthropic.com/engineering/how-we-contain-claude)
- [미검증] "Building effective agents" (Erik Schluntz, Barry Zhang, 2024-12): 가장 단순한 해법부터 찾고, 필요할 때만 복잡도를 더한다. workflow 와 agent 를 구분한다. tool 인터페이스 (ACI) 를 HCI 만큼 신경 쓴다. — [anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)
- [미검증] "Writing tools for agents" (2025-09): tool 은 에이전트를 위해 설계하고, 평가로 개선한다. — [anthropic.com/engineering/writing-tools-for-agents](https://www.anthropic.com/engineering/writing-tools-for-agents)

**Cat Wu (Claude Code·Cowork 제품 책임자)**
- 2026-05 Code with Claude 에서 다음 설계 과제로 proactivity 를 꼽았다. — [2차 TechCrunch 요약](https://thehuman2ai.pages.dev/product/radar/techcrunch-anthropic-cat-wu)
- "몇 달 뒤의 모델을 위해 만든다" 는 철학은 비영어 2차 출처에만 있다. 검증하지 못했다.
- Latent Space 에서 "I think I PM with a pretty light touch" 라고 말했다. — [2차 Latent Space wiki](https://latent.space/wiki/cat-wu/)

### Inferences
- 공식 docs 의 일반 원칙 (예시·XML·역할) 과 Thariq 의 6 신화는 표면상 충돌한다. 둘의 대상이 다르다. docs 는 API 로 출력 형식을 맞추는 경우다. Thariq 는 Claude Code 같은 에이전트 하네스의 행동 지시다.
- "덜 지시한다" 는 "덜 맥락을 준다" 가 아니다. Thariq 도 HTML 목업·루브릭·코드 레퍼런스 같은 풍부한 맥락은 늘리라고 한다.

### Gaps
- Amanda Askell, Alex Albert, Erik Schluntz 의 2026 년 위임 원칙 1차 자료는 찾지 못했다. Felix 원문은 Alex Albert 의 Blender 사례만 인용한다.
- Cat Wu 의 2026 Lenny's Newsletter 글은 유료라 원문을 보지 못했다.

---

## Q3. Anthropic 외부의 검증된 빌더

### Takeaway
외부 빌더도 "검증 가능성", "사람의 이해 유지", "짧은 지침 파일 + 필요 시 세부 문서" 에 동의한다. Karpathy 와 Willison 은 Anthropic 보다 "사람이 diff 와 spec 을 소유한다" 를 더 강하게 말한다.

### Cited Findings

**Andrej Karpathy, Sequoia Ascent 2026 요약 (2026-04-30)** — [1차 블로그](https://karpathy.bearblog.dev/sequoia-ascent-2026/)
- "You can outsource your thinking, but you can't outsource your understanding."
- "Traditional software automates what you can specify." LLM 과 RL 은 "automate what you can verify."
- 모델은 jagged 하다. 검증 신호가 있는 분야에서 가장 빨리 좋아진다. 그렇지 않으면 "it may fail in surprisingly basic ways."
- Software 3.0 에서 "the context window becomes the main lever."
- Agentic engineering 정의: "coordinating fallible agents while preserving correctness, security, taste, and maintainability."
- 좋은 agentic engineer 는 spec 을 설계하고, plan 을 감독하고, diff 를 보고, 테스트를 쓴다.
- 에이전트와 함께 "a detailed spec, maybe basically the docs" 를 설계한다. 사람은 최상위 범주와 감독을 맡는다.
- "They are not smooth human minds. They are jagged, alien tools."
- 문서·CLI·API·MCP 서버를 agent-legible 하게 만든다.

**Simon Willison, "Agentic Engineering Patterns" 가이드 (2026-02-23 시작)** — [1차 소개 글](https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/), [1차 목차](https://simonwillison.net/guides/agentic-engineering-patterns/)
- Agentic engineering 은 전문 엔지니어가 코딩 에이전트로 자기 전문성을 증폭하는 것이다. 코드에 신경 쓰지 않는 vibe coding 과 구분한다.
- 장 제목이 곧 원칙이다: "Writing code is cheap now", "Hoard things you know how to do", "AI should help us produce better code", "Red/green TDD", "First run the tests", "Agentic manual testing", "Linear walkthroughs", "Interactive explanations".
- 안티패턴: "Inflicting unreviewed code on collaborators."
- 부록 "Prompts I use" 에 실제 프롬프트가 있다. 이번 조사에서 본문은 열지 않았다.

**OpenAI Codex 공식 best practices** — [1차](https://developers.openai.com/codex/learn/best-practices) (검색 요약으로만 확인)
- Codex 를 한 번 쓰는 도구가 아니라, 설정하고 개선하는 팀원으로 다룬다.
- 모호한 아이디어는 Codex 가 먼저 사용자에게 질문하게 한다.
- 긴 작업은 PLANS.md 실행 계획 템플릿을 따르게 한다.
- AGENTS.md 에 저장소 구조, 빌드·테스트·린트 명령, PR 규칙, 금지 규칙, 완료 검증 방법을 쓴다.
- AGENTS.md 가 커지면 메인 파일을 짧게 두고 작업별 문서를 참조한다.

**Tobi Lütke (Shopify CEO), "context engineering"** — [미검증]
- 2025-06 X 게시물에서 "prompt engineering" 보다 "context engineering" 이라는 용어를 선호했다. 핵심 기술을 "the art of providing all the context for the task to be plausibly solvable by the LLM" 으로 정의했다. Karpathy 가 동의했다. 이번 세션에서 원문 URL 을 확인하지 못했다.

### Inferences
- Karpathy 의 "verify 가능한 것만 자동화된다" 는 Felix 의 "grade outside the session" 과 Boris 의 "검증 수단 = 2-3x" 의 이론적 근거다.
- Codex 의 AGENTS.md 지침과 Thariq 의 CLAUDE.md 지침은 거의 같다. 짧은 루트 파일 + 필요 시 세부 문서다.

### Gaps
- Cursor 팀, Hamel Husain 의 2026 자료는 이번 조사 예산 안에서 찾지 못했다.
- OpenAI Codex 페이지 원문은 404 리다이렉트로 열지 못했다. 위 내용은 검색 요약이다.

---

## Q4. 시간에 따른 원칙 변화 (2024 → 2025 → 2026)

### Takeaway
2024 년의 "프롬프트를 더 길고 더 구체적으로" 는 2026 년에 "지시는 짧게, 맥락과 검증은 풍부하게" 로 뒤집혔다. 역할 프롬프트·예시·XML 은 API 출력 제어에는 살아 있다. 에이전트 하네스 지시에서는 약해졌다.

### Cited Findings

| 원칙 | 2024–2025 | 2026 현재 상태 | 근거 |
|---|---|---|---|
| "You are an expert X" 역할 프롬프트 | 널리 권장 | API 시스템 프롬프트에는 여전히 권장한다. Felix 는 역할극을 피하고 전문가의 "행동" 을 요청하라고 한다. | [docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), [Felix](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) |
| Few-shot 예시 | 핵심 기법 | 출력 형식 제어에는 3–5 개를 권장한다. 에이전트 행동에는 "examples constrain exploration" 으로 줄인다. | [docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), [Thariq](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/) |
| XML 태그 | 핵심 기법 | 혼합 입력의 구조화에는 여전히 권장한다. | [docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) |
| "Think step by step" / 추론 출력 요청 | 권장 | 사고는 adaptive thinking 과 effort 로 조절한다. Fable 5 에서 추론을 본문에 쓰라는 지시는 `reasoning_extraction` 거부를 일으킬 수 있다. **구식** | [Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) |
| `budget_tokens`, prefill | 사용 | prefill 은 4.6 부터 미지원이다. `budget_tokens` 는 4.7 이상에서 400 에러다. **폐기** | [docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) |
| 대문자 강조·"If in doubt, use X" | 덜 따르는 모델 대응용 | 과다 호출과 지시 충돌을 일으킨다. 이유를 붙인 짧은 지시로 바꾼다. | [docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), [Thariq](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/) |
| 긴 시스템 프롬프트·규칙 목록 | 규칙 누적 | Claude Code 는 80% 이상을 지웠다. 평가 손실은 없었다. | [Thariq](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/) |
| CLAUDE.md 에 실수마다 규칙 추가 | 2026-01 Boris 권장 | 여전히 하지만, gotcha 중심으로 짧게 유지하고 `/doctor`·`/checkup` 으로 정리한다. 기억은 auto-memory 로 옮겼다. | [Boris 01-31](https://x.com/bcherny/status/2017742741636321619), [Boris 07-08](https://x.com/bcherny/status/2074997571563479143), [Thariq](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/) |
| Plan mode 먼저 | 2026-01 Boris 핵심 팁 | 2026-06 Boris 는 새 모델이 planning step 이 거의 필요 없다고 말한다. 대신 Thariq 는 "blindspot pass" 와 인터뷰로 미지수를 줄인다. | [Boris 06-08](https://x.com/bcherny/status/2064034799711588805), [Thariq 07-03](https://x.com/trq212/status/2073100352921215386) |
| 상세 skill | 2025-10 skill 발표 이후 확산 | 이전 모델용 skill 은 Fable 5 에서 품질을 떨어뜨릴 수 있다. 가벼운 안내서 + progressive disclosure 로 바꾼다. | [Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5), [Thariq](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/) |
| Anti-laziness 프롬프트 ("be thorough") | 필요 | 4.6 이후 모델은 과잉 탐색·과잉 엔지니어링 경향이 있다. 오히려 범위를 제한하는 문장이 필요하다. | [docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) |
| 자기 검토 ("check your work") | 권장 | 별도 fresh-context verifier 가 self-critique 보다 낫다. | [Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) |
| 매 동작 권한 승인 | 기본 | auto mode 와 격리로 대체한다. 사용자가 프롬프트의 약 93% 를 승인했기 때문이다. | [Boris 03-24](https://x.com/bcherny/status/2036555259997462541), [containment](https://www.anthropic.com/engineering/how-we-contain-claude) |

### Inferences
- 변화의 공통 원인은 지시 준수 능력의 향상이다. 모델이 짧은 지시를 잘 따르면, 긴 지시는 충돌과 과잉 반응의 원인이 된다.
- 모델이 바뀔 때마다 기존 프롬프트·skill 을 다시 평가해야 한다. Fable 5 docs 와 Thariq 와 Felix 가 모두 이 점에 동의한다.

### Gaps
- XML 태그의 효과가 줄었다는 1차 자료는 찾지 못했다. 현재 docs 는 여전히 권장한다.

---

## Q5. 복사해 쓰는 프롬프트 템플릿 (원문 유지)

### Takeaway
아래 템플릿은 모두 1차 출처의 원문이다. 출처가 2차인 것은 표시했다.

### Cited Findings

**목표와 이유 전달**
- `I'm working on [the larger task] for [who it's for]. They need [what the output enables]. With that in mind: [request].` — [Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)
- Felix altitude: `Tell me what changed this quarter, why, and what we should do about it.` / `Work out which three decisions are most urgent in the face of everything you've learned` — [Felix](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)
- Felix depth prompt (원문 조각): `I want a deeper version of this task, not a bigger one.` → 최고 전문가가 할 일, 가장 원천 자료, 구체 방법·도구, "what, other than you or me, would show the result is right" 를 말하게 한 뒤 `Then rewrite my prompt to ask for exactly that.` — [Felix](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)
- Felix 원천 데이터: `We believe churn is an onboarding problem. Try to reproduce that from the raw data.` — [Felix](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)

**미지수 줄이기·인터뷰**
- `Interview me one question at a time about anything ambiguous.` — [Thariq 07-03](https://x.com/trq212/status/2073100352921215386) (2차 인덱스 경유)
- "blindspot pass" 를 코딩 전에 요청한다. — 같은 출처

**검증·도전**
- `Grill me on these changes and don't make a PR until I pass your test.` — [Boris 01-31](https://x.com/bcherny/status/2017742741636321619) (2차 인덱스 경유)
- `Prove to me this works.` — 같은 출처
- `Knowing everything you know now, scrap this and implement the elegant solution.` — 같은 출처
- `each pr must run /verify and post a repro and truth table to the pr.` — [Boris 08-13](https://x.com/bcherny/status/2088014489438621990)
- `Establish a method for checking your own work at an interval of [X] as you build. Run this every [X interval], verifying your work with subagents against the specification.` — [Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)
- `Before reporting progress, audit each claim against a tool result from this session. Only report work you can point to evidence for; if something is not yet verified, say so explicitly. ...` — [Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)
- `never call a UI change done from a successful edit alone.` — [ClaudeDevs 07-06](https://x.com/ClaudeDevs/status/2074208949205881033)

**범위·자율성 제어**
- `When you have enough information to act, act. Do not re-derive facts already established in the conversation, re-litigate a decision the user has already made, or narrate options you will not pursue ...` — [Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)
- `Pause for the user only when the work genuinely requires them: a destructive or irreversible action, a real scope change, or input that only they can provide. If you hit one of these, ask and end the turn, rather than ending on a promise.` — 같은 출처
- `When the user is describing a problem, asking a question, or thinking out loud rather than requesting a change, the deliverable is your assessment. Report your findings and stop. ...` — 같은 출처
- `Don't add features, refactor, or introduce abstractions beyond what the task requires. ... do the simplest thing that works well. ...` — 같은 출처
- `Consider the reversibility and potential impact of your actions. ...` — [docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- `Write code that reads like the surrounding code: match its comment density, naming, and idiom.` — [Thariq](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/)

**위임·subagent**
- `Delegate independent subtasks to subagents and keep working while they run. Intervene if a subagent goes off track or is missing relevant context.` — [Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)
- `Use subagents when tasks can run in parallel, require isolated context, or involve independent workstreams that don't need to share state. For simple tasks, sequential operations, single-file edits, ... work directly rather than delegating.` — [docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Claude Code 에서 대규모 병렬 작업 트리거: `use a workflow` — [2차 인덱스](https://howborisusesclaudecode.com/)

**보고 형식**
- `Lead with the outcome. Your first sentence after finishing should answer "what happened" or "what did you find" ... Being readable and being concise are different things, and readability matters more.` — [Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)

**메모리·피드백을 규칙으로**
- `Store one lesson per file with a one-line summary at the top. Record corrections and confirmed approaches alike, including why they mattered. Don't save what the repo or chat history already records; ...` — [Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)
- `Reflect on the previous sessions we've had together. Use subagents to identify core themes and lessons, and store them in [X]. ...` — 같은 출처

**리서치**
- `Search for this information in a structured way. As you gather data, develop several competing hypotheses. Track your confidence levels in your progress notes to improve calibration. ...` — [docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)

**긴 작업·자율 실행**
- `You are operating autonomously. The user is not watching in real time and cannot answer questions mid-task, ... End your turn only when the task is complete or you are blocked on input only the user can provide.` — [Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)
- 새 컨텍스트 시작: `Review progress.txt, tests.json, and the git logs.` — [docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)

### Inferences
- 템플릿의 대부분은 "무엇을 하지 말라" 보다 "언제 멈추고 무엇을 증거로 삼으라" 를 말한다. 2026 년 지시의 중심이 행동 규칙에서 종료 조건과 증거로 옮겨 갔다.

### Gaps
- Simon Willison 의 "Prompts I use" 부록 본문은 열지 않았다.

---

## Q6. Felix Rieseberg 와의 합의·불일치

### Takeaway
다른 실무자들은 Felix 의 핵심 주장 대부분에 동의한다. 차이는 역할 프롬프트, 예시, plan 단계, "사람이 이해를 유지해야 하는가" 에서 나온다. 또한 사용자 요약의 "skill 반감기" 주장은 Felix 블로그 원문에 없다.

### Cited Findings

**원문 확인 결과 (중요)**
- Felix 블로그 원문 (2026-10-13) 은 skill·agent 의 반감기를 다루지 않는다. 원문은 능력이 "every couple of weeks" 바뀐다고만 말한다. — [Felix](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/). 사용자 요약의 이 항목은 인터뷰에서 나왔을 수 있다. 인터뷰 원문은 이번 조사에서 확인하지 못했다.
- Felix 블로그는 speed 를 "잘 알려진 것" 으로 보고 생략한다. altitude·depth·range 를 다룬다.
- 역할극 경고 원문: "It is easy to accidentally engage in role play, which will make your transcript weirder." "Don't ask the model to _write_ like a short seller, ask it to _do_ what a short seller _does_ to research their position."
- 자기 채점 금지 원문: "Do _not_ ask the model to judge itself." 이상적인 검증은 "a tool the model can run to get feedback immediately" 다.

**합의**
- 목표를 준다 ↔ "Give the reason, not only the request" ([Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)), `/goal` ([ClaudeDevs](https://x.com/ClaudeDevs/status/2054351031279186040)), "Start at the top of your difficulty range" (Fable 5 docs).
- 세션 밖에서 채점한다 ↔ fresh-context verifier ([Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)), self-preferential bias 와 adversarial verification ([Thariq](https://x.com/trq212/status/2061907337154367865)), 검증 수단 = 2-3x ([Boris](https://x.com/bcherny/status/2007179832300581177)), "automate what you can verify" ([Karpathy](https://karpathy.bearblog.dev/sequoia-ascent-2026/)).
- 원천 데이터와 컴퓨터를 연다 ↔ Slack 스레드·CI 로그를 통째로 주고 "fix" ([Boris gist](https://gist.github.com/joyrexus/e20ead11b3df4de46ab32b4a7269abe0)), "the context window becomes the main lever" ([Karpathy](https://karpathy.bearblog.dev/sequoia-ascent-2026/)), HTML 목업 같은 rich reference ([Thariq](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/)).
- 피드백을 규칙으로 만든다 ↔ 교정 후 CLAUDE.md 갱신 ([Boris](https://x.com/bcherny/status/2017742741636321619)), "a rejected PR is a failure of automation" ([Boris](https://x.com/bcherny/status/2077460395279692197)), 메모리 시스템 ([Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)).
- skill 은 금방 낡는다 ↔ 이전 모델용 skill 이 품질을 떨어뜨린다 ([Fable 5 docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)), 시스템 프롬프트 80% 삭제 ([Thariq](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/)), 미사용 skill 38 개 ([Boris](https://x.com/bcherny/status/2074997571563479143)).
- 병렬로 함께 돌린다 ↔ 병렬 세션·worktree ([Boris](https://x.com/bcherny/status/2017742741636321619)), Felix 의 "새 프로세스를 기존 프로세스 옆에서 한 분기 동안 돌린다" ([Felix](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)).

**불일치 또는 긴장**
- 역할 프롬프트: 공식 docs 는 시스템 프롬프트의 한 줄 역할을 여전히 권장한다 ([docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). Felix 는 역할극을 피하라고 한다. 둘은 양립한다. 한 줄 역할은 어조·영역을 정한다. Felix 의 대안은 전문가의 방법·도구·검증을 명시하는 것이다.
- 예시: docs 는 3–5 개 예시를 권장한다. Thariq 는 예시가 탐색 공간을 제한한다고 한다. Felix 의 depth 원칙은 Thariq 쪽에 가깝다.
- 사람의 이해: Karpathy 는 "you can't outsource your understanding" 이라고 하고, diff 검토와 spec 소유를 강조한다 ([Karpathy](https://karpathy.bearblog.dev/sequoia-ascent-2026/)). Willison 은 리뷰하지 않은 코드를 동료에게 넘기는 것을 안티패턴으로 꼽는다 ([Willison](https://simonwillison.net/guides/agentic-engineering-patterns/)). Boris 는 중요한 코드만 diff 를 읽고 나머지는 테스트·벤치마크에 맡긴다 ([Boris](https://x.com/bcherny/status/2098165206296011059)). Felix 의 "raise altitude" 는 Boris 쪽에 가깝다.
- 비용: Thariq 는 "Most traditional coding tasks do not need a panel of 5 reviewers" 라고 한다 ([Thariq](https://x.com/trq212/status/2061907337154367865)). 공식 docs 도 subagent 과다 사용을 경고한다. Felix 의 "ambition" 은 작업 규모와 검증 강도를 맞춰야 한다는 단서가 필요하다.
- 범위: Felix 는 더 높은 목표와 range 를 요구한다. Fable 5 docs 는 요청하지 않은 기능·리팩터링·행동을 막는 문장을 권장한다. 두 지침은 층위가 다르다. 목표는 넓게 주고, 실행 범위는 명시적으로 제한한다.

### Inferences
- 실무 공식은 "목표·이유는 넓게, 지시는 짧게, 맥락은 원천 그대로, 종료 조건과 검증은 세션 밖에" 로 요약된다. 이 공식은 Felix·Boris·Thariq·공식 docs·Karpathy 에 모두 근거가 있다.
- 레퍼런스 라이브러리는 각 원칙에 "모델 세대" 태그를 붙여야 한다. 원칙의 유효 기간이 모델 출시 주기와 같기 때문이다.

### Gaps
- Felix 인터뷰 (2026-10) 원문은 이번 조사에서 확인하지 못했다. skill 반감기·side-by-side 주장의 정확한 문구는 인터뷰에서 확인해야 한다.
