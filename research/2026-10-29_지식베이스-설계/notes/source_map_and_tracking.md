# AI 플랫폼 빌더 소스 맵과 신규 콘텐츠 자동 추적 (2026-10-29 기준)

> 검증 방법 표기
> - **[피드 확인 10-29]**: 연구자가 2026-10-29 에 curl 로 URL 을 직접 요청했다. HTTP 200 과 RSS/Atom 루트 태그, 최신 날짜를 확인했다. 괄호 대신 "최신=" 으로 마지막 항목 날짜를 적는다.
> - **[학습 지식·미검증]**: 연구자의 학습 지식(2026-06 까지)에 근거한다. 10월 재확인을 하지 않았다. 리포트 작성자는 이 항목을 단정하지 않는다.
> - 소속·직함은 대부분 학습 지식 기준이다. 사람의 이직은 잦다. 리포트에서 "2026 상반기 기준" 으로 표기할 것을 권한다.

## 1. 2026 년 "AI 모델·에이전트와 일하는 법" 에서 가장 신뢰할 개인 소스 15–25 명은 누구인가? (Claude 위임 관련성 순위)

### Takeaway
Claude 위임 관련성 1 순위는 Claude Code 를 직접 만드는 Anthropic 인원이다. Boris Cherny, Cat Wu, Thariq Shihipar, Felix Rieseberg 가 여기에 든다. 그다음은 방법론을 1 차 자료로 공개하는 독립 실무자다. Simon Willison, Hamel Husain, Andrej Karpathy, swyx 가 여기에 든다. 개인 X 계정은 가장 빠른 채널이지만, 2026-09 이후 무료 RSS 경로가 사라졌다. 따라서 블로그·뉴스레터·팟캐스트 피드가 있는 사람을 우선 구독 대상으로 삼는다.

### Cited Findings

**A. 순위표** — 신뢰도(직접 빌드 여부)와 "Claude 에 일 맡기기" 관련성을 합산한 연구자 판단 순위다. 피드 열은 실측 결과다.

| # | 이름 | 소속·역할 | 신뢰 근거 | 주요 채널 | 기계 판독 피드 | 게시 빈도 | 강점 주제 |
|---|---|---|---|---|---|---|---|
| 1 | Boris Cherny | Anthropic, Claude Code 창시자·리드 [학습 지식·미검증] | Claude Code 를 직접 만들었다. 2026-01 X 스레드로 자기 작업 흐름을 공개했다 | X @bcherny, GitHub [github.com/bcherny](https://github.com/bcherny) | 개인 블로그 RSS 없음. X RSS 경로 소멸(질문 4 참조) | X 수시. 장문은 드묾 | Claude Code 작업 흐름, 병렬 세션, Plan Mode, CLAUDE.md, 검증 루프 |
| 2 | Cat Wu | Anthropic, Claude Code 프로덕트 리드 [학습 지식·미검증] | Claude Code 제품 결정을 직접 한다 | X @_catwu [학습 지식·미검증], Latent Space 출연 [학습 지식·미검증] | 없음 | 드묾 | 기능 의도, 팀 단위 도입 |
| 3 | Thariq Shihipar | Anthropic, Claude Code·Agent SDK 팀 [학습 지식·미검증] | SDK·Skills 기능을 직접 설명한다 | X @trq212 [학습 지식·미검증] | 없음 | X 수시 | Agent SDK, Skills, 훅 |
| 4 | Felix Rieseberg | Anthropic, Claude 데스크톱 앱 계열 리드. Electron 메인테이너 출신 [학습 지식·미검증] | 데스크톱 에이전트 제품을 직접 만든다 | 블로그 [felixrieseberg.com](https://www.felixrieseberg.com), GitHub [github.com/felixrieseberg](https://github.com/felixrieseberg) | **[피드 확인 10-29]** [https://www.felixrieseberg.com/rss](https://www.felixrieseberg.com/rss) 최신=2026-10-28 | 월 1회 내외 [학습 지식·미검증] | 데스크톱 에이전트, 로컬 도구 연동 |
| 5 | Simon Willison | 독립. Datasette·LLM CLI 작성자, Django 공동 창시자 | 매일 실험 결과와 코드를 공개한다. 출처 링크를 항상 단다 | [simonwillison.net](https://simonwillison.net), X @simonw, GitHub [github.com/simonw](https://github.com/simonw), YouTube UCMZiuY-vetBbvPlL2w6bp4A | **[피드 확인 10-29]** [전체](https://simonwillison.net/atom/everything/) 최신=2026-10-28, [장문만](https://simonwillison.net/atom/entries/), [claude-code 태그](https://simonwillison.net/tags/claude-code.atom) | 하루 여러 건 | 도구 리뷰, 프롬프트 인젝션, Claude Code 실사용, 모델 비교 |
| 6 | Hamel Husain | 독립 컨설턴트, 평가(evals) 강의 공동 운영 | 실제 고객 평가 파이프라인 경험을 쓴다 | [hamel.dev](https://hamel.dev), X @HamelHusain | **[피드 확인 10-29]** [https://hamel.dev/index.xml](https://hamel.dev/index.xml) 최신=2026-10-20 | 월 1–2회 | evals, 오류 분석, LLM-as-judge |
| 7 | Andrej Karpathy | 독립(Eureka Labs). 전 OpenAI·Tesla | "vibe coding" 같은 용어를 만들었다. 직접 코드를 공개한다 | X @karpathy, [karpathy.bearblog.dev](https://karpathy.bearblog.dev/blog/), YouTube UCXUPKJO5MZQN11PqgIvyuvQ | **[피드 확인 10-29]** [bearblog 피드](https://karpathy.bearblog.dev/feed/) 최신=2026-04-30. [github.io 피드](https://karpathy.github.io/feed.xml) 최신=2026-04-10 | 블로그는 분기 1회 미만. X 가 주 채널 | LLM 작동 원리, 에이전트 시대 소프트웨어 관점 |
| 8 | swyx (Shawn Wang) | Latent Space 진행자, AI Engineer 컨퍼런스 공동 창립자 | 빌더 인터뷰를 가장 많이 한다. "AI Engineer" 용어를 대중화했다 | [latent.space](https://www.latent.space), [swyx.io](https://www.swyx.io), X @swyx | **[피드 확인 10-29]** [Latent Space](https://www.latent.space/feed) 최신=2026-10-28. [swyx.io](https://www.swyx.io/rss.xml) 최신=2026-07-05 | Latent Space 주 1–2회 | 업계 지형, 빌더 인터뷰 |
| 9 | Erik Schluntz · Barry Zhang | Anthropic 응용 AI [학습 지식·미검증] | "Building effective agents" 공동 저자 | [anthropic.com/engineering](https://www.anthropic.com/engineering) | Anthropic 엔지니어링 피드를 통해 받는다(질문 2) | 드묾 | 에이전트 설계 패턴 |
| 10 | Alex Albert | Anthropic, Claude Relations 리드 [학습 지식·미검증] | 공식 발표와 사용 팁을 가장 먼저 낸다 | X @alexalbert__ [학습 지식·미검증] | 없음 | X 수시 | 신기능 요약, 프롬프트 팁 |
| 11 | Amanda Askell · Zack Witten | Anthropic. Claude 성격·시스템 프롬프트, 프롬프트 엔지니어링 [학습 지식·미검증] | 모델 행동을 직접 설계한다 | X @AmandaAskell, @zswitten [학습 지식·미검증], Anthropic YouTube 출연 | 없음 | 드묾 | 프롬프트 설계, 모델 성향 |
| 12 | Jason Liu | 독립 컨설턴트, Instructor 라이브러리 작성자 | RAG·구조화 출력 실무 경험이 많다 | [jxnl.co](https://jxnl.co), X @jxnlco | **[피드 확인 10-29]** [https://jxnl.co/feed_rss_created.xml](https://jxnl.co/feed_rss_created.xml) 최신=2026-10-28 | 주 1회 내외 | RAG, 컨텍스트 설계, 코딩 에이전트 활용 |
| 13 | Drew Breunig | 독립 연구자·작가 | 컨텍스트 엔지니어링 실패 유형 정리로 인용이 많다 [학습 지식·미검증] | [dbreunig.com](https://www.dbreunig.com) | **[피드 확인 10-29]** [https://www.dbreunig.com/feed.xml](https://www.dbreunig.com/feed.xml) 최신=2026-10-24 | 주 1회 내외 | context engineering, DSPy |
| 14 | Philipp Schmid | Google DeepMind DevRel [학습 지식·미검증] | Gemini 쪽 에이전트 가이드를 직접 쓴다 | [philschmid.de](https://www.philschmid.de), X @_philschmid | **[피드 확인 10-29]** [https://www.philschmid.de/rss](https://www.philschmid.de/rss) 최신=2026-09-28 | 월 1–2회 | context engineering, Gemini 에이전트 |
| 15 | Addy Osmani | Google 엔지니어링 리더 [학습 지식·미검증] | AI 보조 개발 관행을 꾸준히 정리한다 | [addyo.substack.com](https://addyo.substack.com), X @addyosmani | **[피드 확인 10-29]** [https://addyo.substack.com/feed](https://addyo.substack.com/feed) 최신=2026-10-29 | 주 1회 내외 | 에이전트 코딩 워크플로우, 팀 도입 |
| 16 | Thorsten Ball | Sourcegraph Amp 엔지니어 [학습 지식·미검증] | 코딩 에이전트를 직접 만든다 | [Register Spill](https://registerspill.thorstenball.com), [ampcode.com/news](https://ampcode.com/news) | **[피드 확인 10-29]** [Register Spill](https://registerspill.thorstenball.com/feed) 최신=2026-10-29. [Amp news](https://ampcode.com/news.rss) 최신=2026-10-28 | 주 1회 | 에이전트 구조, 코딩 에이전트 UX |
| 17 | Geoffrey Huntley | 독립 | 반복 루프형 자율 코딩 실험("Ralph" 루프)으로 알려졌다 [학습 지식·미검증] | [ghuntley.com](https://ghuntley.com) | **[피드 확인 10-29]** [https://ghuntley.com/rss/](https://ghuntley.com/rss/) 최신=2026-10-28 | 주 1회 내외 | 장시간 자율 실행, 프롬프트 루프 |
| 18 | Armin Ronacher | 독립(Flask 작성자) | 에이전트 코딩 실사용기를 솔직하게 쓴다 | [lucumr.pocoo.org](https://lucumr.pocoo.org) | **[피드 확인 10-29]** [https://lucumr.pocoo.org/feed.atom](https://lucumr.pocoo.org/feed.atom) 최신=2026-10-09 | 월 1–2회 | 에이전트 코딩 한계, 도구 설계 |
| 19 | Mitchell Hashimoto | 독립(Ghostty, HashiCorp 공동 창업자) | 실제 OSS 개발에 에이전트를 쓴 기록을 공개한다 | [mitchellh.com](https://mitchellh.com) | **[피드 확인 10-29]** [https://mitchellh.com/feed.xml](https://mitchellh.com/feed.xml) 최신=2026-10-06 | 월 1회 내외 | 에이전트 코딩 실무 |
| 20 | Ethan Mollick | Wharton 교수 | 비개발자 관점 위임 실험이 많다 | [oneusefulthing.org](https://www.oneusefulthing.org) | **[피드 확인 10-29]** [https://www.oneusefulthing.org/feed](https://www.oneusefulthing.org/feed) 최신=2026-10-29 | 주 1회 | 업무 위임, 조직 도입 |
| 21 | Eugene Yan | Anthropic 소속으로 알려짐 [학습 지식·미검증] | 추천·평가 시스템 실무 글이 깊다 | [eugeneyan.com](https://eugeneyan.com) | **[피드 확인 10-29]** [https://eugeneyan.com/rss/](https://eugeneyan.com/rss/) 최신=2026-06-21 | 분기 1–2회 | evals, 제품 패턴 |
| 22 | Lilian Weng | Thinking Machines Lab 공동 창업자, 전 OpenAI [학습 지식·미검증] | 에이전트·환각 개관 글이 표준 참고문헌이다 | [lilianweng.github.io](https://lilianweng.github.io) | **[피드 확인 10-29]** [https://lilianweng.github.io/index.xml](https://lilianweng.github.io/index.xml) 최신=2026-07-04 | 연 2–3회 | 에이전트 이론, 연구 개관 |
| 23 | Alexander Embiricos · Romain Huet | OpenAI Codex 프로덕트·개발자 경험 [학습 지식·미검증] | Codex 를 직접 만든다 | X @embirico, @romainhuet [학습 지식·미검증] | 개인 피드 없음. OpenAI 개발자 블로그로 받는다(질문 2) | X 수시 | Codex 작업 흐름, harness 설계 |
| 24 | Logan Kilpatrick | Google AI Studio·Gemini API 프로덕트 [학습 지식·미검증] | Gemini 개발자 기능을 직접 발표한다 | X @OfficialLoganK [학습 지식·미검증] | 없음 | X 매일 | Gemini 신기능 |
| 25 | Lee Robinson · Michael Truell | Cursor(Anysphere) [학습 지식·미검증] | Cursor 제품을 직접 만든다 | [cursor.com/blog](https://cursor.com/blog), YouTube Cursor UC6YYHJzM6PhZ2Yey9BQiUaw | 개인 피드는 [leerob.com/rss](https://leerob.com/rss) 404. Cursor 피드는 질문 2 참조 | 블로그 월 수회 | IDE 에이전트, 모델 라우팅 |

**B. 보조 사실**
- Boris Cherny 의 작업 흐름 스레드는 2026-01 초에 X 에 올라왔다. 2 차 요약 글들은 팁 개수를 10·13·22·53 개로 서로 다르게 센다 — [VentureBeat](https://venturebeat.com/technology/the-creator-of-claude-code-just-revealed-his-workflow-and-developers-are), [Medium 요약](https://medium.com/@joe.njenga/boris-cherny-claude-code-creator-shares-these-22-tips-youre-probably-using-it-wrong-1b570aedefbe), [jitendrazaa 요약](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)
- 그 스레드의 핵심은 다음과 같다. 터미널에서 Claude 5 개, 웹에서 5–10 개 세션을 병렬로 돌린다. 복잡한 작업은 Plan Mode 로 시작한다. Claude 가 실수하면 CLAUDE.md 에 추가한다. 검증 수단 제공이 품질의 최대 요인이다 — [VentureBeat](https://venturebeat.com/technology/the-creator-of-claude-code-just-revealed-his-workflow-and-developers-are), [getpushtoprod 요약](https://getpushtoprod.substack.com/p/how-the-creator-of-claude-code-actually)
- 30 일 동안 PR 259 개를 머지했다는 수치는 본인 주장이다. 독립 검증은 없다 — [Medium 요약](https://medium.com/@joe.njenga/boris-cherny-claude-code-creator-shares-these-22-tips-youre-probably-using-it-wrong-1b570aedefbe)
- Lance Martin 블로그 피드는 살아 있다. 다만 최신 글이 2026-01-10 이다 — [rlancemartin.github.io/feed.xml](https://rlancemartin.github.io/feed.xml) [피드 확인 10-29]
- Shreya Shankar(evals 연구자)의 피드 후보 URL 은 404 였다 — https://www.sh-reya.com/blog/rss.xml [피드 확인 10-29]
- HumanLayer(Dex Horthy, "12-factor agents") 블로그 피드 후보 URL 은 404 였다 — https://www.humanlayer.dev/blog/rss.xml [피드 확인 10-29]

### Inferences
- 개인 블로그 피드가 확실한 사람만 자동 추적 1 군에 넣는다. 1 군 후보는 Simon Willison, Hamel Husain, Felix Rieseberg, Jason Liu, Drew Breunig, Thorsten Ball, Addy Osmani, Latent Space 다.
- Anthropic 빌더 대부분은 X 에만 짧게 쓴다. 그들의 생각은 결국 Anthropic 엔지니어링 블로그, 공식 문서, 팟캐스트 출연으로 장문화된다. 따라서 공식 채널과 팟캐스트 피드가 X 를 대체하는 현실적 경로다.
- Karpathy, swyx 개인 블로그, Eugene Yan, Lilian Weng 은 게시 빈도가 낮다. 놓칠 위험은 작고, 신호 가치는 크다. 피드를 넣어도 소음이 거의 없다.

### Gaps
- Anthropic·OpenAI·Google·Cursor 인원의 2026-10 현재 직함·소속은 재확인하지 못했다. 이유는 X·LinkedIn 프로필을 비로그인으로 읽을 수 없기 때문이다.
- Boris Cherny 의 2026 년 팟캐스트 출연 목록은 1 차 출처로 확인하지 못했다. Lenny's Podcast·Latent Space 출연은 학습 지식 기준이다.
- 각 개인의 정확한 게시 빈도는 피드 항목 수를 세지 않아 대략값이다.

## 2. 실무 가이드를 내는 공식 채널은 무엇이고, RSS 가 있는가?

### Takeaway
Anthropic 은 문서 쪽 피드를 공식 제공한다. Claude Code 변경 이력과 Claude Platform 릴리스 노트가 여기에 든다. GitHub 저장소 Atom 피드도 모두 작동한다. 반면 anthropic.com/engineering, anthropic.com/news, claude.com/blog 에는 공식 RSS 가 없다. 이 3 곳은 커뮤니티가 만든 GitHub 기반 피드(Olshansk/rss-feeds)로 대체할 수 있다. OpenAI 와 Google 은 공식 RSS 를 제공한다.

### Cited Findings

**Anthropic 공식 채널** — 모든 상태는 [피드 확인 10-29] 결과다.

| 채널 | 페이지 | 공식 피드 | 상태 |
|---|---|---|---|
| Anthropic Engineering 블로그 | [anthropic.com/engineering](https://www.anthropic.com/engineering) | 없음. `/engineering/rss.xml`, `/rss.xml` 모두 404 | 대체: [Olshansk feed_anthropic_engineering.xml](https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_engineering.xml) lastBuildDate=2026-10-20 |
| Anthropic News | [anthropic.com/news](https://www.anthropic.com/news) | 없음. `/news/rss.xml` 404 | 대체: [Olshansk feed_anthropic_news.xml](https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_news.xml) lastBuildDate=2026-10-29. Research·Red 피드도 같은 저장소에 있다 |
| Claude 블로그 | [claude.com/blog](https://claude.com/blog) | 없음. `/blog/rss.xml` 404 | 대체: [Olshansk feed_claude.xml](https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_claude.xml) lastBuildDate=2026-10-28 |
| Claude Code 변경 이력(문서) | [code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog) | **있음**: [https://code.claude.com/docs/en/changelog/rss.xml](https://code.claude.com/docs/en/changelog/rss.xml) — 페이지 `<link rel=alternate>` 로 확인 | lastBuildDate=2026-10-29, 항목 15 개 |
| Claude Platform 릴리스 노트 | [docs.claude.com/en/release-notes/overview](https://docs.claude.com/en/release-notes/overview) | **있음**: [https://platform.claude.com/docs/en/release-notes/feed.xml](https://platform.claude.com/docs/en/release-notes/feed.xml) | lastBuildDate=2026-10-23, 항목 158 개 |
| Claude Code GitHub 릴리스 | [github.com/anthropics/claude-code](https://github.com/anthropics/claude-code) | **있음**: [releases.atom](https://github.com/anthropics/claude-code/releases.atom) | updated=2026-10-27 |
| Claude Code CHANGELOG.md 원문 | [raw CHANGELOG.md](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md) | 피드 아님. 평문이라 diff 에 적합하다 | HTTP 200 |
| anthropics/skills | [github.com/anthropics/skills](https://github.com/anthropics/skills) | **있음**: [commits/main.atom](https://github.com/anthropics/skills/commits/main.atom) | updated=2026-10-28 |
| Claude cookbooks | [github.com/anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | **있음**: [commits/main.atom](https://github.com/anthropics/claude-cookbooks/commits/main.atom). 옛 이름 anthropic-cookbook URL 도 같은 피드로 연결된다 | updated=2026-10-24 |
| 공식 플러그인 저장소 | [github.com/anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | **있음**: [commits/main.atom](https://github.com/anthropics/claude-plugins-official/commits/main.atom) | updated=2026-10-27 |
| Agent SDK (Python) | [github.com/anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) | **있음**: [releases.atom](https://github.com/anthropics/claude-agent-sdk-python/releases.atom) | updated=2026-10-24 |
| Anthropic YouTube | [youtube.com/@anthropic-ai](https://www.youtube.com/@anthropic-ai) | channel_id=UCrDwWp7EBBv4NwvScIpBDOA | 피드 URL 은 2026-10-29 에 404. 질문 4 참조 |
| Claude YouTube | [youtube.com/@claude](https://www.youtube.com/@claude) | channel_id=UCV03SRZXJEz-hchIAogeJOg | 위와 같음 |

**OpenAI · Google DeepMind · Cursor 대응 채널** — [피드 확인 10-29]

| 채널 | 피드 URL | 상태 |
|---|---|---|
| OpenAI News | [https://openai.com/news/rss.xml](https://openai.com/news/rss.xml) | lastBuildDate=2026-10-29 |
| OpenAI Developers 블로그 | [https://developers.openai.com/rss.xml](https://developers.openai.com/rss.xml) — [blog](https://developers.openai.com/blog) 페이지에서 발견 | 최신 pubDate=2026-04-30. 항목 1 개만 확인되어 불안정하다. 대체: [Olshansk feed_openai_developer.xml](https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_openai_developer.xml) lastBuildDate=2026-10-27 |
| OpenAI Engineering | 공식 URL `openai.com/news/engineering/rss.xml` 은 403 | 대체: Olshansk `feed_openai_engineering.xml` 존재 확인(내용 미확인) |
| OpenAI Codex 릴리스 | [github.com/openai/codex/releases.atom](https://github.com/openai/codex/releases.atom) | updated=2026-10-28 |
| OpenAI Codex 변경 이력 | [developers.openai.com/codex/changelog](https://developers.openai.com/codex/changelog) | 페이지 200. 피드 링크 미확인 |
| OpenAI Cookbook | [github.com/openai/openai-cookbook/commits/main.atom](https://github.com/openai/openai-cookbook/commits/main.atom) | updated=2026-10-26. `cookbook.openai.com/rss.xml` 은 404 |
| OpenAI YouTube | channel_id=UCXZCJLdBC09xxGZ6gcdrc6A | — |
| Google DeepMind 블로그 | [https://deepmind.google/blog/rss.xml](https://deepmind.google/blog/rss.xml) | lastBuildDate=2026-10-28 |
| Google 블로그 DeepMind 섹션 | [https://blog.google/technology/google-deepmind/rss/](https://blog.google/technology/google-deepmind/rss/) | lastBuildDate=2026-10-27 |
| Google 블로그 Developers 섹션 | [https://blog.google/technology/developers/rss/](https://blog.google/technology/developers/rss/) | lastBuildDate=2026-10-28 |
| Google Developers Blog | [https://developers.googleblog.com/feeds/posts/default](https://developers.googleblog.com/feeds/posts/default) | lastBuildDate=2026-10-29 |
| Gemini API 변경 이력 | [ai.google.dev/gemini-api/docs/changelog](https://ai.google.dev/gemini-api/docs/changelog) | 페이지 200. 피드 미확인 |
| Gemini CLI 릴리스 | [github.com/google-gemini/gemini-cli/releases.atom](https://github.com/google-gemini/gemini-cli/releases.atom) | updated=2026-10-28 |
| Google DeepMind YouTube | channel_id=UCP7jMXSY2xbc3KCAE0MHQ-A | — |
| Cursor 변경 이력 | [https://cursor.com/changelog/rss.xml](https://cursor.com/changelog/rss.xml) | lastBuildDate=2026-10-29 |
| Cursor 블로그 | 공식 `cursor.com/blog/rss.xml` 은 404 | 대체: Olshansk `feed_cursor.xml` 존재 확인 |

- 실무 가이드성 Anthropic 글의 예시로 [Claude Code best practices](https://www.anthropic.com/engineering/claude-code-best-practices) 페이지가 200 으로 살아 있다 [피드 확인 10-29].
- OpenAI "harness engineering" 글 URL 은 연구 환경에서 403 이었다. 봇 차단으로 보이며, 존재 여부는 미확인이다 — https://openai.com/index/harness-engineering

### Inferences
- Claude 위임 학습에 가장 밀도 높은 피드 3 개는 다음과 같다. Claude Code 변경 이력 RSS, anthropics/claude-code releases.atom, Anthropic Engineering 대체 피드.
- 문서 변경 이력 피드는 "내 라이브러리의 어떤 항목이 낡았는가" 판정에 가장 직접적이다. 기능 이름 변경 사례로 "routines → scheduled tasks" 가 있다(질문 5).
- Olshansk/rss-feeds 는 제3자 스크레이퍼다. 사이트 구조가 바뀌면 조용히 멈출 수 있다. lastBuildDate 가 7 일 넘게 멈추면 경고하도록 설계한다.

### Gaps
- Anthropic 이 공식 RSS 를 숨겨 두었는지 확인하지 못했다. anthropic.com 페이지 소스에서 `<link rel=alternate>` 를 찾지 못했고, sitemap.xml 에서도 /engineering 경로를 추출하지 못했다.
- Olshansk/rss-feeds 의 갱신 주기와 유지보수 지속성은 확인하지 못했다.

## 3. 이런 사람들을 정기적으로 초대하는 YouTube 채널·팟캐스트는 무엇인가? (한국어 채널 포함)

### Takeaway
영어권 핵심은 Latent Space, Lenny's Podcast, Every 의 AI & I, AI Engineer 채널이다. 4 곳 모두 오디오·뉴스레터 피드가 살아 있어 YouTube 피드 장애를 우회할 수 있다. 한국어 채널은 AgentOS(@ai-AgentOS)와 원티드(@ch.wanted)의 "왓츠인마이AI" 시리즈 존재를 확인했다. 다만 한국어 채널은 1 차 빌더가 아니라 요약·적용 채널이다. 따라서 "발견용" 으로만 쓰고, 사실 판단은 원문으로 돌아가서 한다.

### Cited Findings

**영어권** — channel_id 는 각 채널 페이지 소스의 externalId 에서 추출했다 [피드 확인 10-29].

| 채널 | YouTube channel_id | 오디오·글 피드 | 비고 |
|---|---|---|---|
| Latent Space (swyx, Alessio) | [@LatentSpacePod](https://www.youtube.com/@LatentSpacePod) UCxBcwypKK-W3GHd_RZ9FZrQ. 커뮤니티 라이브는 [@LatentSpaceTV](https://www.youtube.com/@LatentSpaceTV) UCvi5jNRoRVm436TVAXet1kQ | [https://www.latent.space/feed](https://www.latent.space/feed) 최신=2026-10-28 | Anthropic·OpenAI 빌더 출연이 가장 잦다 [학습 지식·미검증] |
| Lenny's Podcast | [@LennysPodcast](https://www.youtube.com/@LennysPodcast) UC6t1O76G0jYXOAoYCm153dA | [https://www.lennysnewsletter.com/feed](https://www.lennysnewsletter.com/feed) 최신=2026-10-29 | 피드에 뉴스레터와 팟캐스트가 섞인다 |
| Every — AI & I (Dan Shipper) | [@EveryInc](https://www.youtube.com/@EveryInc) UCjIMtrzxYc0lblGhmOgC_CA | [https://every.to/feeds/all.xml](https://every.to/feeds/all.xml), [chain-of-thought](https://every.to/feeds/chain-of-thought) 200. `every.to/podcast/feed.xml` 은 404 | 채널 설명: "stay at the edge of AI" |
| AI Engineer (컨퍼런스) | [@aiDotEngineer](https://www.youtube.com/@aiDotEngineer) UCLKPca3kwwd-B59HNr-_lvA | 없음 | 빌더 발표 원본. 예: Anthropic Skills 발표 [학습 지식·미검증] |
| No Priors (Elad Gil, Sarah Guo) | [@NoPriorsPodcast](https://www.youtube.com/@NoPriorsPodcast) UCSI7h9hydQ40K5MJHnCrQvw | 미확인 | 채널 설명: "leading engineers, researchers and founders" |
| Silicon Valley Girl (Marina Mogilko) | [@SiliconValleyGirl](https://www.youtube.com/@SiliconValleyGirl) UCiq1FIgtEK7LRAOB1JXTPig | 미확인 | 채널 설명: 주간 AI·기술 팟캐스트, CEO·창업자 인터뷰. 빌더 깊이는 낮다 |
| 기타 Substack 팟캐스트 피드 | — | [api.substack.com/feed/podcast/1084089.rss](https://api.substack.com/feed/podcast/1084089.rss) 최신=2026-10-27 | 어느 프로그램인지 제목 추출 실패. 사용 전 확인 필요 |
| Andrej Karpathy | [@AndrejKarpathy](https://www.youtube.com/@AndrejKarpathy) UCXUPKJO5MZQN11PqgIvyuvQ | — | 장편 강의 |
| Cursor / Anysphere | [@cursor_ai](https://www.youtube.com/@cursor_ai) UC6YYHJzM6PhZ2Yey9BQiUaw, [@anysphere](https://www.youtube.com/@anysphere) UCAl0OZcxg0ILdXKMg9hxv8w | — | — |

**한국어** — [피드 확인 10-29]

| 채널 | channel_id | 확인 내용 | 성격 |
|---|---|---|---|
| AgentOS | [@ai-AgentOS](https://www.youtube.com/@ai-AgentOS) UC2ODfJSf8L4PeCw4ebTECJQ | 채널 설명: "AI 에이전트 시대의 생존 가이드 · Claude Code · Agentic Flow · AI 커리어 전략". YouTube 검색 "AgentOS 클로드 코드" 결과 상위 48 건이 이 채널이었다 | 요약·적용. 주의: `@AgentOS` 핸들은 다른 우크라이나어 채널이다 |
| 원티드 — 왓츠인마이AI | [@ch.wanted](https://www.youtube.com/@ch.wanted) channel_id 미추출 | 검색 결과 영상 제목: "실무에서 바로 써먹는 클로드 디자인 워크플로우! 경력직 디자이너들의 AI 활용 비법 대공개 \| 왓츠인마이AI ep.2". 같은 채널에 "업무 시간 90% 단축! 뉴스레터 빌더 사이트 제작기" 같은 사내 제작기 영상이 있다 | 한국 기업 실무자의 적용 사례. 주의: `@wantedlab`(UC4MiQC0E-P11Zmap85IfBLA)은 별도 채널이다 |
| AI Frontier Korea (노정석) | [@chester_roh](https://www.youtube.com/@chester_roh) UCz-BiVywYdO6iXhjXkw_Kgw | 채널 존재 확인 | 창업자 관점 해설 [성격은 학습 지식·미검증] |
| 테디노트 | [@teddynote](https://www.youtube.com/@teddynote) UCt2wAAXgm87ACiQnDHQEW6Q | 채널 존재 확인 | LangChain·RAG 실습 [성격은 학습 지식·미검증] |
| 조코딩 | [@jocoding](https://www.youtube.com/@jocoding) UCQNE2JmbasNYbjGAcuBiRRg | 채널 존재 확인 | 대중 입문·뉴스 [성격은 학습 지식·미검증] |

- 웹 검색으로는 "원티드 왓츠인마이AI" 채널을 찾지 못했다. YouTube 검색 결과 페이지에서만 확인되었다 — [WebSearch 결과에 원티드랩 LinkedIn 게시물만 나옴](https://kr.linkedin.com/in/bokkeelee)
- 웹 검색 "AgentOS Claude Code" 결과는 Builder Methods 의 Agent OS, Julian Goldie 의 Agent OS 같은 동명 영어권 프로젝트와 섞였다 — [Builder Methods Agent OS](https://buildermethods.com/agent-os/v2/adaptability), [Julian Goldie Podcast](https://share.transistor.fm/s/1608f7d6)

### Inferences
- 팟캐스트는 Substack·RSS 오디오 피드로 추적한다. YouTube 피드보다 안정적이다. 영상이 꼭 필요할 때만 YouTube 를 쓴다.
- 한국어 채널은 2 단계 소스로 분류한다. 한국어 영상이 소개한 원문(영상·글·스레드) 링크를 반드시 따라가서 원문을 라이브러리에 넣는다.

### Gaps
- 각 팟캐스트의 2026 년 Anthropic 빌더 출연 회차 목록은 확인하지 못했다.
- @ch.wanted 의 channel_id, 왓츠인마이AI 전체 회차 수, 업로드 주기는 확인하지 못했다.
- Silicon Valley Girl 의 빌더 출연 빈도는 확인하지 못했다.

## 4. 유료 API 없이 YouTube RSS 와 X 콘텐츠를 받는 방법은? 2026 년에 무엇이 작동하고 무엇이 깨지는가?

### Takeaway
YouTube 채널 RSS 형식은 `https://www.youtube.com/feeds/videos.xml?channel_id=UC...` 이다. 그러나 2026-10-29 연구 환경에서 5 개 채널 모두 404 가 났다. 2025-12 이후 간헐적 404 보고가 있다. 그러므로 yt-dlp 같은 대체 경로를 함께 둔다. X 는 더 나쁘다. Nitter 는 2026-09-11 에 저장소가 보관 처리되었다. XCancel 은 2026-09-14 에 무기한 중단되었다. 무료 X RSS 경로는 현재 사실상 없다.

### Cited Findings

**YouTube**
- 피드 URL 형식: `https://www.youtube.com/feeds/videos.xml?channel_id=<UC로 시작하는 ID>`. 업로드 재생목록 형식 `?playlist_id=UU<ID 나머지>` 도 있다. 2026-10-29 연구 환경에서 Anthropic, AI Engineer, Lenny's 채널 피드와 `user=GoogleDevelopers` 형식이 모두 404 였다. 3 회 재시도해도 같았다 [피드 확인 10-29]
- 2025-12-27 Google AI 개발자 포럼에 간헐적 404 보고가 있다. 오류는 주로 09:00–12:00 UTC 에 났다. 같은 URL 이 브라우저에서는 작동했다 — [discuss.ai.google.dev](https://discuss.ai.google.dev/t/youtube-rss-feed-endpoint-returns-404-errors/113379), [n8n community 미러](https://community.n8n.io/t/youtube-rss-feed-endpoint-returns-404-errors/241692)
- 한 피드 리더 가이드는 2025-12 부터 간헐적 404 가 있다고 쓴다. 이 가이드는 데이터센터 IP 에서 특히 불안정하다고 경고한다. 간헐적 404 를 "채널 소멸" 로 처리하지 말라고 권한다 — [feeder.co 도움말](https://feeder.co/ko/help/rss/youtube-feeds/)
- 핸들(@이름)을 channel_id 자리에 넣으면 404 가 난다. UC 로 시작하는 ID 를 써야 한다 — [kakafarm 글](https://kakafarm.codeberg.page/posts/2025/01/02/youtube-channel-rss-feed.html)
- channel_id 추출: 채널 페이지 HTML 에서 `"externalId":"UC..."` 를 찾는다. 연구자는 이 방법으로 질문 3 의 ID 를 모두 추출했다 [피드 확인 10-29]
- 일부 사용자는 Piped 같은 프록시 프런트엔드를 써서 Google 을 직접 호출하지 않는다 — [techlore 포럼](https://discuss.techlore.tech/t/suddenly-lost-access-to-youtube-rss-feeds/6963)
- 공개 RSSHub 인스턴스(rsshub.app)는 연구 환경에서 403 을 반환했다 [피드 확인 10-29] — https://rsshub.app/anthropic/news

**X (Twitter)**
- 2026-08 에 X 가 Nitter 에 중지 요청서를 보냈다. 2026-09-11 에 Nitter GitHub 저장소가 보관(읽기 전용) 처리되었다. 2026-09-14 에 XCancel 이 "추가 공지까지" 서비스를 중단했다. TechCrunch 기사는 작동하는 대안을 제시하지 않는다 — [TechCrunch 2026-09-15](https://techcrunch.com/2026/09/15/nitter-and-xcancel-are-dead-again-after-xs-latest-legal-actions)
- 2026-10-29 실측: `xcancel.com/bcherny/rss` 는 HTTP 451(법적 사유로 이용 불가)을 반환했다. `nitter.net/bcherny/rss` 는 HTTP 410(영구 삭제)을 반환했다. nitter.poast.org, nitter.privacydev.net 은 연결 자체가 실패했다 [피드 확인 10-29]
- 2026-05 자료 기준으로도 xcancel 은 리더별 화이트리스트가 필요했다. nitter.net 은 강한 속도 제한이 있었다. nitter.poast.org 는 CAPTCHA 뒤에 있었다 — [WP RSS Aggregator finder](https://finder.wprssaggregator.com/rss-feeds/platform/x-twitter)

### Inferences
- YouTube 는 2 중 경로로 운영한다. 1 차는 RSS 피드다. 실패하면 yt-dlp 로 채널 `/videos` 목록을 받는다. 명령 예: `yt-dlp --flat-playlist --print "%(id)s %(title)s" https://www.youtube.com/@LatentSpacePod/videos`. 이 명령은 [학습 지식·미검증] 이며, 연구 환경에 yt-dlp 가 없어 실행하지 못했다.
- 자막 추출은 yt-dlp 의 `--write-auto-subs --sub-langs en,ko --skip-download` 로 한다 [학습 지식·미검증]. 추출한 자막은 Claude 가 요약·대조하는 입력이 된다.
- 개인 Mac 에서 실행하면 데이터센터 IP 문제를 줄일 수 있다. 근거는 위 포럼 보고의 "브라우저에서는 작동" 이라는 관찰이다.
- X 는 자동 추적을 포기하는 편이 유지 비용이 가장 낮다. 대안은 다음과 같다.
  - 빌더의 X 내용은 결국 공식 블로그·변경 이력·팟캐스트로 옮겨진다. 이 채널 피드로 대체한다.
  - Simon Willison 이 빌더의 X 글을 자주 인용한다. 그의 피드가 X 의 간접 필터 역할을 한다 [학습 지식·미검증].
  - 사용자가 로그인한 X 에서 "AI 빌더" 리스트를 만든다. 주 1 회 수동으로 훑는다.
  - X 공식 API 유료 요금제는 비용과 가격 정책을 확인하지 못했다. Gaps 참조.
- 깨지기 쉬운 순서(연구자 판단): X 미러 > 공개 RSSHub > YouTube RSS > 제3자 스크레이프 피드(Olshansk) > 공식 RSS·GitHub Atom.

### Gaps
- YouTube 404 가 이 연구 환경 IP 만의 문제인지, 전역 장애인지 확인하지 못했다. 사용자 Mac 에서 재시험이 필요하다.
- YouTube Data API v3 의 2026 년 무료 할당량은 확인하지 못했다.
- X 공식 API 의 2026 년 가격·무료 등급은 확인하지 못했다.
- 2026-10 이후 Nitter 대체 프로젝트가 생겼는지 확인하지 못했다.

## 5. 1 인 사용자를 위한 자동화 선택지는? 가장 간단한 시작점과 Claude 트리아지 설계

### Takeaway
가장 간단한 시작점은 "GitHub 저장소 1 개 + Claude Code 클라우드 예약 작업 1 개" 다. 예약 작업은 Pro 이상 요금제에서 쓸 수 있다. 노트북을 닫아도 클라우드에서 돈다. 최소 주기는 1 시간이다. 주의점이 하나 있다. 기본 클라우드 환경은 허용 목록 도메인만 통과시킨다. 그래서 RSS 를 직접 받으려면 네트워크 접근 수준을 바꿔야 한다. 피드 수집은 GitHub Actions cron 으로 분리하는 방식이 더 견고하다. 그 경우 Claude 는 수집된 신규 항목의 트리아지만 맡는다.

### Cited Findings

**Claude Code 예약 작업(구 routines)**
- 클라우드 예약 작업은 프롬프트, 저장소, 커넥터를 묶은 저장된 설정이다. Anthropic 관리 클라우드에서 실행되어 노트북을 닫아도 작동한다. 상태는 연구 프리뷰다 — [Claude Code docs: routines](https://code.claude.com/docs/en/routines)
- 트리거는 3 종이다. 일정(매시·매일·매주·1 회), API(HTTP POST + bearer 토큰), GitHub 이벤트 — [같은 문서](https://code.claude.com/docs/en/routines)
- Pro, Max, Team, Enterprise 요금제에서 쓸 수 있다. [claude.ai/code/routines](https://claude.ai/code/routines) 또는 CLI `/schedule` 로 만든다. `/routines` 는 별칭이다. 예: `/schedule daily PR review at 9am` — [같은 문서](https://code.claude.com/docs/en/routines)
- 사용자 정의 cron 을 지원한다. cron 시간은 UTC 로 쓴다. `CRON_TZ=` 접두사로 시간대를 지정할 수 있다. 1 시간보다 짧은 주기는 거부된다. 정각 예약은 몇 분 늦을 수 있어 9:07 같은 시각을 권한다 — [같은 문서](https://code.claude.com/docs/en/routines)
- 실행마다 저장소를 새로 clone 한다. Claude 는 `claude/` 접두사 브랜치에 push 한다 — [같은 문서](https://code.claude.com/docs/en/routines)
- 기본 환경의 네트워크 수준은 "Trusted" 다. 패키지 레지스트리 같은 기본 허용 목록만 통과한다. 목록 밖 호스트 요청은 `403`, `x-deny-reason: host_not_allowed` 로 실패한다. 커넥터 트래픽은 Anthropic 서버를 거치므로 허용 목록과 무관하다 — [같은 문서](https://code.claude.com/docs/en/routines)
- 사용량은 대화형 세션과 같은 구독 한도를 쓴다. 별도로 계정당 예약 실행 100 회/시간 한도가 있다 — [같은 문서](https://code.claude.com/docs/en/routines)
- GitHub 연결이 끊기면 최대 72 시간 실행을 건너뛴다. 72 시간이 지나면 작업이 꺼진다 — [같은 문서](https://code.claude.com/docs/en/routines)
- 예약 실행은 확인 없이 비공개 artifact 를 새로 게시할 수 있다 — [같은 문서](https://code.claude.com/docs/en/routines)
- 예약 방식 3 종 비교: 클라우드는 기계가 꺼져 있어도 되고 로컬 파일 접근이 없다. 최소 1 시간이다. Desktop 예약 작업은 기계가 켜져 있어야 하고 로컬 파일에 접근한다. `/loop` 는 열린 세션이 필요하고 최소 1 분이다 — [Compare scheduling options](https://code.claude.com/docs/en/scheduled-tasks.md)

**기타 선택지**
- GitHub Actions cron + RSS diff: 피드 URL 목록을 받아 이전 상태 파일과 비교하고, 새 항목을 마크다운으로 커밋한다. 무료 시간 한도와 cron 지연 특성은 [학습 지식·미검증] 이다.
- n8n: RSS Read 노드가 있다. YouTube RSS 404 문제가 n8n 커뮤니티에도 보고되었다 — [n8n community](https://community.n8n.io/t/youtube-rss-feed-endpoint-returns-404-errors/241692). 자체 호스팅 서버 관리 부담이 있다 [학습 지식·미검증].
- Readwise Reader · Feedly: RSS·뉴스레터·YouTube 를 한곳에서 읽는다. Readwise 는 하이라이트 내보내기 API 가 있다 [학습 지식·미검증]. 2026 년 X·YouTube 수집 지원 상태는 미확인이다.
- yt-dlp 자막 추출: 질문 4 의 Inferences 참조.

### Inferences

**권장 시작 구성(연구자 설계)**
1. 사용자가 비공개 GitHub 저장소를 만든다. 예: `ai-reference`.
2. 사용자가 `sources.yaml` 에 질문 1–3 의 피드 URL 을 넣는다. 각 항목에 tier, 주제 태그, 신뢰 등급을 단다.
3. GitHub Actions 가 매일 1 회 cron 으로 피드를 받는다.
4. 스크립트가 `state/seen.json` 과 비교해 새 항목만 `inbox/2026-10-29.md` 에 쓴다.
5. 스크립트가 피드별 최신 날짜를 기록한다. 7 일 이상 정지한 제3자 피드는 경고 목록에 넣는다.
6. Claude Code 클라우드 예약 작업이 매일 09:07 KST 에 같은 저장소에서 돈다.
7. Claude 가 inbox 항목을 라이브러리와 대조한다. 결과를 `triage/2026-10-29.md` 로 `claude/` 브랜치에 커밋한다.
8. 사용자가 주 1 회 트리아지 결과를 보고 머지한다.

- 수집을 Actions 로 분리하는 이유: 클라우드 기본 환경은 임의 도메인을 막는다. Actions 는 공개 인터넷에 자유롭게 접근한다. 또한 결정적 diff 는 LLM 이 아닌 스크립트가 맡아야 재현성이 생긴다.
- 더 단순한 대안: 클라우드 환경의 네트워크 접근을 넓힌다. 그러면 예약 작업 하나가 수집과 트리아지를 모두 한다. 대신 피드 도메인 목록을 환경 설정에 따로 관리해야 한다.
- 로컬 파일이 필요하면 Desktop 예약 작업을 쓴다. 예: Obsidian 볼트에 직접 쓰기. 단, Mac 이 켜져 있어야 한다.

**Claude 트리아지 프롬프트 설계(연구자 설계)**
- 판정 라벨 4 개를 쓴다.
  - `NEW`: 라이브러리에 없는 개념·기법이다.
  - `UPDATE`: 기존 항목의 사실을 바꾼다. 예: 기능 이름 변경, 한도 변경, 지원 중단.
  - `DUP`: 기존 항목과 같은 내용이다. 원문이 더 1 차적이면 출처만 교체한다.
  - `SKIP`: 마케팅, 채용, 관련 없는 주제다.
- 각 판정에 근거 1 문장과 영향받는 라이브러리 파일 경로를 쓰게 한다.
- 라이브러리 각 항목 머리말에 `last_verified`, `source_url`, `depends_on` 을 둔다. `depends_on` 의 예는 `claude-code>=2.x`, `feature:routines` 다.
- 낡은 항목 판정 규칙 2 개를 둔다.
  - 변경 이력 피드가 `depends_on` 의 기능 이름을 언급하면, 그 항목을 `STALE?` 로 표시한다.
  - `last_verified` 가 90 일을 넘으면, 그 항목을 재검증 목록에 넣는다.
- 실제 사례: 2026 문서는 "scheduled tasks, formerly routines" 라고 쓴다. "routines" 로 쓴 라이브러리 항목은 `UPDATE` 대상이 된다 — [Claude Code docs](https://code.claude.com/docs/en/routines)
- Claude 는 원문 전체를 라이브러리에 붙이지 않는다. 요약, 핵심 인용 1–2 개, 원문 링크만 저장한다. 이유는 저작권과 라이브러리 크기 관리다.

### Gaps
- GitHub Actions 무료 한도의 2026 년 수치를 확인하지 못했다.
- Readwise Reader, Feedly 의 2026 년 가격과 YouTube·X 수집 지원 여부를 확인하지 못했다.
- 예약 작업의 클라우드 환경에서 "Full" 네트워크 수준의 정확한 이름과 선택지를 확인하지 못했다. 문서는 "network access level" 변경 절차만 확인했다.

## 6. 신뢰도 기준: "플랫폼을 직접 만드는 사람" 과 "인플루언서 재포장" 을 어떻게 구별하는가?

### Takeaway
1 차 빌더는 코드, 공식 문서, 제품 결정, 재현 가능한 수치라는 산출물을 남긴다. 재포장 콘텐츠는 원문 링크 없이 개수를 붙인 팁 목록을 만든다. 같은 원문을 두고도 숫자가 서로 달라지는 특징이 있다. Boris Cherny 스레드 요약이 10·13·22·53 개로 갈린 것이 실제 사례다.

### Cited Findings
- Boris Cherny 스레드를 다룬 2 차 글들은 팁 개수를 서로 다르게 센다. 검색 결과에는 원본 X 게시물이 나오지 않고 요약본만 나왔다 — [VentureBeat](https://venturebeat.com/technology/the-creator-of-claude-code-just-revealed-his-workflow-and-developers-are), [Medium](https://medium.com/@joe.njenga/boris-cherny-claude-code-creator-shares-these-22-tips-youre-probably-using-it-wrong-1b570aedefbe), [madappgang](https://madappgang.com/blog/claude-code-tips-from-its-creator-boris-cherny/), [Product Hunt](https://www.producthunt.com/p/how-boris-uses-claude-code)
- 재포장 제목 패턴 예: "Boris Cherny … Shares These 22 Tips (You're Probably Using It Wrong)" — [Medium](https://medium.com/@joe.njenga/boris-cherny-claude-code-creator-shares-these-22-tips-youre-probably-using-it-wrong-1b570aedefbe)
- "AgentOS" 같은 이름은 영어권 동명 프로젝트·채널이 여럿이다. 이름만으로 출처를 판단할 수 없다 — [Builder Methods](https://buildermethods.com/agent-os/v2/adaptability), [Julian Goldie Podcast](https://share.transistor.fm/s/1608f7d6)

### Inferences
**1 차 빌더 신호(연구자 판단 기준)**
- 공식 저장소에 커밋이나 릴리스 기록이 있다. 예: anthropics/claude-code, openai/codex.
- 회사 공식 엔지니어링 블로그나 문서에 저자로 오른다.
- 제품 기능의 "왜" 를 설명한다. 트레이드오프와 한계를 함께 말한다.
- 재현 가능한 코드, 프롬프트 원문, 수치를 공개한다.
- 다른 1 차 빌더가 그 사람을 인용한다.

**재포장 신호**
- 제목에 숫자 + 과장이 붙는다. 예: "N 가지 팁", "당신은 잘못 쓰고 있다".
- 원문 링크가 없거나, 원문 날짜·버전을 밝히지 않는다.
- 같은 원문의 다른 요약과 내용·개수가 다르다.
- 코드나 재현 절차가 없다.
- 강의·제휴 링크 판매가 본문보다 앞선다.

**운영 규칙**
- 2 차 소스는 "발견" 에만 쓴다. 라이브러리에는 2 차 소스가 가리킨 원문만 저장한다.
- 독립 실무자는 중간 등급으로 둔다. 예: Simon Willison, Hamel Husain. 이들은 플랫폼을 만들지는 않지만 1 차 실험 결과를 공개한다.
- 각 소스에 신뢰 등급을 단다. T1 은 플랫폼 빌더·공식 채널이다. T2 는 1 차 실험을 공개하는 독립 실무자다. T3 는 요약·해설 채널이다. 한국어 요약 채널 대부분이 T3 에 든다.

### Gaps
- 신뢰도 판정 기준을 다룬 학술·업계 표준 자료는 찾지 못했다. 위 기준은 연구자 판단이다.
