# 개인 AI 작업법 레퍼런스 라이브러리 구조 설계 (Claude Code + git, 2026-10-29 기준)

조사일: 2026-10-29. 대상 저장소: `/Users/leeyoonsam/Documents/ai-reference`.
현재 상태: `references/` 에 Aside 로 만든 한국어 PDF 2개가 있다.
- `클로드에게_일을_맡기는_법_실무레퍼런스.pdf`: Felix Rieseberg 인터뷰 정리. 원본 영상 2026-10-20, 정리 영상 2026-10-26, 함께 인용된 블로그 글 2026-10-13.
- `HR_AI_에이전트_실무_레퍼런스_왓츠인마이AI_ep03.pdf`: 원티드 피플팀 사례. 영상 게시일 2026-10-28.

로컬 PDF 확인 결과: 첫 번째 PDF 196~197행에 "좋은 스킬의 반감기는 짧다" 문장이 있다. 원문은 "이전 세대 모델에 맞춘 지시가 새 모델에선 오히려 방해가 됩니다. … '그냥 프롬프트만 보내 보기'도 시도해 볼 것" 이다. 같은 PDF 508행 체크리스트에 "오래된 스킬/지시문이 새 모델을 방해하고 있지 않나?" 항목이 있다. 두 PDF 모두 텍스트 레이어가 있다. 따라서 `pdftotext` 로 추출할 수 있다.

## Q1. Claude Code 공식 메커니즘별 로딩 시점·컨텍스트 비용·트레이드오프

### Takeaway
이 용도의 핵심 조합은 짧은 CLAUDE.md (항상 로드) 와 Skill (설명만 상시 로드, 본문은 필요할 때 로드) 이다. 카드 파일은 Claude 가 grep/Read 로 just-in-time 으로 읽게 한다. Subagent·Hook·MCP·Plugin 은 나중에 필요할 때 더한다. 공식 문서도 "트리거가 생길 때 하나씩 더하라" 고 권한다.

### Cited Findings

**공식 비교표 (Extend Claude Code / features-overview)**
- 공식 문서는 기능별 로딩 시점과 비용을 다음처럼 정리한다. CLAUDE.md 는 세션 시작 시 전체가 로드되고 "Every request" 비용이 든다. Skill 은 시작 시 설명만, 사용 시 전체가 로드되고 비용은 "Low (descriptions every request)" 다. MCP 는 시작 시 tool 이름만, schema 는 필요 시 로드한다. Subagent 는 "Isolated from main session" 이다. Hook 은 "Zero, unless hook returns additional context" 다. — [Extend Claude Code](https://code.claude.com/docs/en/features-overview)
- 공식 권장 순서: "Claude gets a convention or command wrong twice → CLAUDE.md", "You keep typing the same prompt to start a task → user-invocable skill", "You paste the same playbook … for the third time → skill", "A side task floods your conversation → subagent", "You want something to happen every time without asking → hook", "A second repository needs the same setup → plugin". — [Extend Claude Code](https://code.claude.com/docs/en/features-overview)
- 공식 경험칙: "Keep CLAUDE.md under 200 lines. If it's growing, move reference content to skills or split into `.claude/rules/` files." — [Extend Claude Code](https://code.claude.com/docs/en/features-overview)
- Skill 은 "reference" 형과 "action" 형으로 나뉜다. reference 는 세션 내내 쓰는 지식이다. action 은 `/deploy` 같은 특정 작업 지시다. — [Extend Claude Code](https://code.claude.com/docs/en/features-overview)
- Claude 는 작업 내용을 skill description 과 대조해 skill 을 고른다. 공식 문서는 "If descriptions are vague or overlap, Claude may load the wrong skill or miss one" 이라고 경고한다. — [Extend Claude Code](https://code.claude.com/docs/en/features-overview)
- Subagent 는 자체 system prompt, `skills:` 필드의 skill 전문, CLAUDE.md, git status 를 받는다. 내장 Explore·Plan agent 는 CLAUDE.md 와 git status 를 받지 않는다. — [Extend Claude Code](https://code.claude.com/docs/en/features-overview)
- 지침을 반드시 지켜야 하면 Hook 을 쓰라고 공식 문서가 말한다: "An instruction like 'never edit .env' in CLAUDE.md or a skill is a request, not a guarantee." — [Extend Claude Code](https://code.claude.com/docs/en/features-overview)

**CLAUDE.md / memory**
- CLAUDE.md 는 작업 디렉터리와 그 상위 디렉터리의 파일을 실행 시 로드한다. 하위 디렉터리의 CLAUDE.md 는 Claude 가 그 디렉터리의 파일을 읽거나 쓸 때 로드한다. — [How Claude remembers your project](https://code.claude.com/docs/en/memory)
- `@path/to/import` 문법으로 다른 파일을 가져올 수 있다. 재귀 import 의 최대 깊이는 4 hops 다. 공백이 있는 경로는 공백마다 백슬래시를 붙여야 한다. — [Memory](https://code.claude.com/docs/en/memory)
- 공식 문서는 import 가 비용을 줄이지 않는다고 명시한다: "Imports help you organize a long file but don't reduce its context cost, because imported files load together with the CLAUDE.md that imports them." — [Memory](https://code.claude.com/docs/en/memory)
- `.claude/rules/*.md` 중 `paths` frontmatter 가 없는 파일은 실행 시 로드한다. `paths` 가 있는 파일은 일치하는 파일을 다룰 때만 로드한다. — [Memory](https://code.claude.com/docs/en/memory)
- Auto memory 는 Claude 가 직접 쓰는 노트다. 저장소 단위이고, 매 세션 "first 200 lines or 25KB" 를 로드한다. — [Memory](https://code.claude.com/docs/en/memory)
- AGENTS.md 는 CLAUDE.md 가 없을 때 대신 읽힌다. 직접 읽기는 v2.1.277 이상에서 지원한다. — [Memory](https://code.claude.com/docs/en/memory)
- `/doctor prompt-audit` 는 CLAUDE.md, rules, skills, commands, subagents, output styles 를 감사해 오래되거나 충돌하는 지시를 찾는다. v2.1.283 이상이 필요하다. — [Memory](https://code.claude.com/docs/en/memory); [Skills](https://code.claude.com/docs/en/skills)

**Skills**
- SKILL.md 는 YAML frontmatter 와 markdown 본문으로 구성된다. 개인 skill 은 `~/.claude/skills/<name>/SKILL.md`, 프로젝트 skill 은 `.claude/skills/<name>/SKILL.md` 에 둔다. — [Skills](https://code.claude.com/docs/en/skills)
- `description` 과 `when_to_use` 를 합친 문자열은 skill 목록에서 1,536자에서 잘린다. — [Skills](https://code.claude.com/docs/en/skills)
- Skill 을 호출하면 전문이 대화에 들어가 이후 턴에도 남는다. 지원 파일은 참조될 때만 로드된다. SKILL.md 는 500줄 미만을 권한다. — [Skills](https://code.claude.com/docs/en/skills)
- Compaction 뒤에는 skill 마다 최근 호출본의 첫 5,000 토큰을 다시 붙인다. 재부착 총 예산은 25,000 토큰이다. — [Skills](https://code.claude.com/docs/en/skills)
- `disable-model-invocation: true` 이면 설명도 컨텍스트에 들어가지 않는다. 사용자만 `/name` 으로 호출할 수 있다. `user-invocable: false` 이면 Claude 만 호출할 수 있다. — [Skills](https://code.claude.com/docs/en/skills)
- `context: fork` 는 skill 본문을 새 subagent 의 프롬프트로 쓴다. 이 subagent 는 대화 기록을 보지 않는다. — [Skills](https://code.claude.com/docs/en/skills)
- Custom slash command 는 skill 로 통합됐다. `.claude/commands/deploy.md` 와 `.claude/skills/deploy/SKILL.md` 는 둘 다 `/deploy` 를 만든다. 기존 command 파일은 계속 동작한다. 새 작업에는 skill 을 권한다. — [Skills](https://code.claude.com/docs/en/skills)
- `$ARGUMENTS`, `$0`, 명명 인자 `arguments: [...]`, `${CLAUDE_SKILL_DIR}`, `${CLAUDE_PROJECT_DIR}` 치환을 지원한다. — [Skills](https://code.claude.com/docs/en/skills)
- 버전 표기: `/skill-doctor` 는 v2.1.252 이상, claude.ai skill 의 터미널 동기화는 v2.1.273 이상이다. — [Skills](https://code.claude.com/docs/en/skills)
- Agent Skills 엔지니어링 글(2025-10-16)은 3단계 progressive disclosure 를 설명한다. 1단계는 name·description 을 system prompt 에 미리 넣는다. 2단계는 SKILL.md 본문, 3단계 이상은 연결 파일이다. 글은 "the amount of context that can be bundled into a skill is effectively unbounded" 라고 쓴다. 2025-12-18 업데이트로 Agent Skills 는 open standard(agentskills.io)가 됐다. — [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

**Plugin / Marketplace**
- Plugin 은 skill, hook, subagent, MCP server 를 하나로 묶는 배포 단위다. Plugin skill 은 `/plugin-name:skill-name` 으로 namespace 가 붙는다. 여러 저장소에서 같은 구성을 쓰거나 남에게 배포할 때 쓴다. — [Extend Claude Code](https://code.claude.com/docs/en/features-overview)

### Inferences
- 레퍼런스 카드 본문을 CLAUDE.md 에 `@import` 하면 안 된다. import 는 매 요청 비용을 그대로 낸다. 카드가 늘수록 context rot 이 커진다.
- 카드 라이브러리 자체는 "skill 의 3단계 파일" 과 같은 위치다. 읽기 전까지 비용이 0이다. 따라서 카드는 저장소 안의 일반 markdown 파일로 두고, skill 이 index 를 거쳐 필요한 카드만 읽게 한다.
- 이 저장소 밖(다른 업무 저장소)에서도 쓰려면 skill 을 `~/.claude/skills/` 개인 skill 로 두고, 본문에서 절대 경로 `/Users/leeyoonsam/Documents/ai-reference/` 를 가리키게 하면 된다. Plugin 은 두 번째 기기나 팀 배포가 필요할 때 검토한다.
- Hook 은 시작 단계에서 필요 없다. 후보 용도는 2가지다. 하나는 `SessionStart` 에서 만료 카드 개수를 알려 주는 것이다. 다른 하나는 커밋 전에 frontmatter 필수 필드를 검사하는 것이다.
- MCP 는 Notion·Obsidian·Slack 에서 새 자료를 가져올 때만 쓴다. 라이브러리의 진실 원천(source of truth)은 git 저장소 하나로 둔다.

### Gaps
- 전체 skill 목록 예산(모든 description 합계의 상한)의 정확한 숫자를 확인하지 못했다. Skills 페이지가 길어 해당 절이 잘렸다.
- Plugins/marketplace 세부 문서(`plugins/overview`)는 직접 읽지 않았다. 개요 페이지의 요약만 인용했다.
- Subagent 의 persistent memory 기능 세부는 확인하지 않았다.

## Q2. 신뢰할 만한 사람들이 제안한 LLM 친화 지식베이스 패턴

### Takeaway
Karpathy 의 LLM wiki 가 이 용도에 가장 잘 맞는다. 구조는 "불변 raw 원천 → LLM 이 유지하는 markdown wiki → index.md + log.md → schema 문서(CLAUDE.md)" 다. Anthropic 의 context engineering 지침도 같은 방향이다. 파일 경로를 가벼운 식별자로 두고, 필요할 때 읽고, 폴더 구조·이름·날짜를 메타데이터 신호로 쓴다.

### Cited Findings

**Karpathy "LLM wiki" (GitHub gist, 2026-04-04 작성)**
- 핵심 개념: LLM 이 질문마다 원본에서 답을 다시 만들지 않는다. 대신 원본과 사용자 사이에 지속되는 상호 링크 markdown wiki 를 점진적으로 만들고 유지한다. Gist 는 이를 "a persistent, compounding artifact" 라고 부른다. — [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- 3개 레이어: (1) raw sources 는 불변이다. LLM 은 읽기만 한다. (2) wiki 는 LLM 이 만들고 유지하는 요약·entity·concept 페이지다. (3) schema 는 구조·규칙·워크플로를 정의하는 CLAUDE.md 또는 AGENTS.md 다. — [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- 3개 작업: Ingest 는 새 원천을 읽고 기존 페이지에 통합한 뒤 index 와 log 를 갱신한다. 원천 하나가 10~15 페이지를 건드릴 수 있다. Query 는 index 를 먼저 읽고 관련 페이지를 찾아 인용 답변을 만든다. 좋은 답변은 새 페이지로 wiki 에 다시 넣는다. Lint 는 모순, 오래된 주장(stale claims), 고아 페이지, 누락 링크, 데이터 공백을 정기 점검한다. — [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- `index.md` 는 카테고리별 카탈로그다. 페이지마다 링크와 한 줄 요약을 둔다. `log.md` 는 append-only 시간순 기록이다. 일관된 접두어를 써서 명령줄 도구로 파싱하기 쉽게 한다. — [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- 규모 기준: 원천 약 100개, 페이지 수백 개 규모에서는 index 파일이 "surprisingly well" 동작한다. 이 규모에서는 embedding 기반 RAG 가 필요 없다. 더 커지면 검색 도구가 유용해진다. — [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- 언급된 도구: Obsidian(뷰어·graph view), qmd(로컬 markdown hybrid 검색, CLI/MCP), Obsidian Web Clipper, Marp, Dataview(frontmatter 쿼리), git(버전 기록). — [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- 2차 자료들도 같은 구조(raw/ 불변, LLM 소유 wiki, schema 문서)를 요약한다. — [classmethod 해설(일본어)](https://dev.classmethod.jp/articles/karpathy-llm-knowledge-base/); [implicator.ai](https://www.implicator.ai/karpathys-llm-wiki-got-16-million-views-the-code-isnt-the-point-2.md)

**Anthropic "Effective context engineering for AI agents" (2025-09-29)**
- 목표: "the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome." — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Just-in-time: agent 는 데이터를 미리 넣지 않는다. 대신 "lightweight identifiers (file paths, stored queries, web links, etc.)" 를 들고 있다가 도구로 필요할 때 읽는다. — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- 파일 시스템 메타데이터: "Folder hierarchies, naming conventions, and timestamps all provide important signals." — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Hybrid 전략: Claude Code 는 CLAUDE.md 를 미리 넣고, 나머지는 glob·grep 으로 just-in-time 으로 가져온다. — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Context rot: 컨텍스트가 커질수록 정보 회상 정확도가 떨어진다. — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- 구조화 노트(agentic memory): agent 가 컨텍스트 밖에 노트를 쓰고 나중에 다시 읽는다. 예로 `NOTES.md` 를 든다. — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- 예시: 규칙을 길게 나열하지 말고 "a set of diverse, canonical examples" 를 큐레이션하라고 권한다. — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

**Simon Willison TIL 저장소**
- 주제별 폴더(`github-actions/`, `python/`, `sqlite/`, `datasette/`)를 둔다. 노트 하나가 markdown 파일 하나다(예: `sqlite/null-case.md`). README 는 주제별 index 이고 항목마다 날짜가 붙는다. til.simonwillison.net 에서 검색할 수 있다. — [simonw/til](https://github.com/simonw/til)

**llms.txt (Jeremy Howard, 2024-09-03 제안, v2 2026-08-10)**
- 형식: H1 프로젝트 이름(유일한 필수 항목), blockquote 요약, 선택 설명, H2 "file list" 섹션(`[name](url): 설명` 목록), 생략 가능한 링크를 모은 "Optional" H2 섹션. — [llmstxt.org](https://llmstxt.org/)
- Claude Code 공식 문서 자체도 `https://code.claude.com/docs/llms.txt` 를 색인으로 제공한다. — [Memory 문서 상단 안내](https://code.claude.com/docs/en/memory)

**Skill 문서화 원칙 (Anthropic skill authoring best practices)**
- "Default assumption: Claude is already very smart." Claude 가 이미 아는 설명은 넣지 않는다. — [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- 참조는 SKILL.md 에서 한 단계 깊이로만 둔다. 중첩 참조에서 Claude 는 `head -100` 같은 부분 읽기를 할 수 있다. — [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- 100줄이 넘는 참조 파일은 맨 위에 목차를 둔다. — [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- 파일 이름은 내용을 드러내야 한다(`form_validation_rules.md` 는 좋고 `doc2.md` 는 나쁘다). 디렉터리는 도메인·기능별로 나눈다. — [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- 용어는 한 개념에 하나만 쓴다. — [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

### Inferences
- 사용자의 규모(PDF 2개, 앞으로 수십~100개)는 Karpathy 가 말한 "index 만으로 충분한" 범위다. 따라서 vector DB·RAG·MCP 검색 서버는 시작 단계에 필요 없다. `index.md` 와 `grep` 으로 충분하다.
- Karpathy 의 wiki 는 "LLM 이 소유하는" 레이어다. 사용자가 원하는 "원칙 카드" 는 이 wiki 레이어에 해당한다. Ingest 는 "PDF 1개 → 카드 N개 + index 갱신 + log 1줄" 로 정의하면 된다.
- Simon Willison 방식(주제 폴더 + 1노트 1파일 + 날짜 붙은 README index)은 사람이 훑어보기 좋다. Karpathy 방식(index.md 를 LLM 이 먼저 읽음)은 Claude 가 찾기 좋다. 두 방식은 같은 `index.md` 하나로 합칠 수 있다.
- llms.txt 형식은 `index.md` 의 서식 규칙으로 빌려 쓸 만하다. H1, 한 줄 요약 blockquote, H2 카테고리별 `[카드](경로): 한 줄 요약` 목록, 폐기 카드를 모은 `## Optional` 섹션 순서로 쓴다.
- Obsidian 사용자이므로 저장소 폴더를 Obsidian vault 로 열 수 있다. 그러면 graph view 와 Dataview frontmatter 쿼리를 추가 비용 없이 쓴다.

### Gaps
- Karpathy gist 본문 중 100,000자 이후(댓글 부분)는 읽지 않았다. 본문 요약은 앞부분에서 얻었다.
- Simon Willison TIL 의 README 자동 생성 방식(GitHub Actions 스크립트, SQLite 빌드)은 페이지에서 확인하지 못했다. 저장소에 `.github/workflows` 폴더가 있다는 사실만 확인했다.
- "Atomic notes"(Zettelkasten) 원전 자료는 이번 조사에서 직접 확인하지 않았다. 아래 Q3 의 "카드 1장 = 원칙 1개" 는 이 개념과 같은 방향이지만, 별도 출처는 없다.

## Q3. 원본 PDF 보존 + markdown 카드 파생 구조, 메타데이터 schema, 폴더 구조

### Takeaway
원본 PDF 는 불변 raw 로 남긴다. PDF 마다 `sources/` 요약 노트 1개를 만들고, 거기서 원칙 1개당 카드 1장을 `cards/` 에 만든다. 카드 frontmatter 에는 출처·날짜·유효 기준일·반감기·신뢰도·재검증 일자를 둔다. Claude 는 `index.md` 를 먼저 읽고 필요한 카드만 연다.

### Cited Findings
- Karpathy 구조의 raw 레이어는 불변이고 LLM 은 읽기만 한다. wiki 레이어만 LLM 이 쓴다. — [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- Karpathy 는 frontmatter 쿼리 도구로 Obsidian Dataview 를 언급한다. — [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- 폴더 계층·이름 규칙·timestamp 는 agent 에게 파일 용도와 시점을 알려 주는 신호다. — [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- 시간에 민감한 정보는 본문에 섞지 않는다. 대신 "Current method" 와 접힌 "Old patterns" 섹션으로 나누고, 폐기 날짜를 적는다(예: "Legacy v1 API (deprecated 2025-08)"). — [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- 사용자의 PDF 에는 이미 원본 영상·게시일·길이·타임스탬프 링크가 표로 들어 있다. 예: "AgentOS … (43:36, 2026-10-26)", "채널 원티드 / 2026-10-28 (길이 19:38)". — 로컬 파일 `references/*.pdf` (`pdftotext` 추출 결과)

### Inferences

**제안 폴더 구조 (시작용)**

```
ai-reference/
├── CLAUDE.md                 # schema: 폴더 규칙·카드 형식·작업 절차. 200줄 미만.
├── index.md                  # llms.txt 형식 카탈로그. 카드마다 한 줄. Claude 가 먼저 읽는다.
├── log.md                    # append-only. "2026-10-29 ingest | …" 형식.
├── raw/                      # 불변 원본. 현재 references/ 를 이름만 바꾼다.
│   └── 2026-10-26_felix-rieseberg_delegate-to-claude.pdf
├── sources/                  # 원본 1개당 1파일. 원본 메타 + 전체 요약 + 파생 카드 목록.
│   └── 2026-10-26_felix-rieseberg_delegate-to-claude.md
├── cards/                    # 원칙·패턴 1개당 1파일.
│   ├── delegation/
│   │   └── ask-for-expert-method-first.md
│   ├── prompting/
│   ├── skills-and-agents/
│   │   └── skill-half-life-try-plain-prompt.md
│   └── hr-automation/
│       └── human-reviews-exceptions-only.md
├── prompts/                  # 검증된 프롬프트 템플릿. 카드를 인용한다.
└── .claude/skills/
    ├── ingest-reference/SKILL.md     # PDF → sources + cards + index + log
    ├── recommend-prompt/SKILL.md     # 작업 설명 → 카드 읽기 → 프롬프트 제안
    └── review-freshness/SKILL.md     # 만료 카드 점검
```

- `references/` 를 `raw/` 로 바꾸는 이유는 Karpathy 의 용어와 맞추기 위해서다. 이름을 유지해도 동작에는 문제가 없다.
- 파일 이름에 날짜 접두어를 붙이면 `ls` 만으로 시간순 정렬이 된다. Anthropic 이 말한 "timestamps as signals" 를 파일 이름에 담는 방법이다.
- 카테고리 폴더는 처음에 3~4개만 만든다. 카드가 10장을 넘는 폴더만 나눈다.

**제안 카드 frontmatter schema**

```yaml
---
id: skill-half-life-try-plain-prompt
title: 좋은 스킬의 반감기는 짧다 — 스킬 없이 plain prompt 도 비교한다
type: principle            # principle | pattern | prompt | case | anti-pattern
tags: [skills, model-upgrade, prompting]
source: sources/2026-10-26_felix-rieseberg_delegate-to-claude.md
source_url: https://…      # 원본 영상 URL + 타임스탬프
author: Felix Rieseberg (Anthropic)
source_date: 2026-10-20     # 원본 발화·게시 날짜
added: 2026-10-29
valid_as_of: 2026-10-29     # 마지막으로 유효함을 확인한 날짜
model_context: Claude Opus 5.5 / Claude Code v2.1.x   # 어떤 모델·도구 기준의 주장인지
half_life: short            # short(3개월) | medium(12개월) | long(원칙급)
review_by: 2027-01-29       # valid_as_of + half_life 로 계산
confidence: medium          # high(공식문서·재현) | medium(전문가 발언) | low(일화)
status: active              # active | needs-review | deprecated
superseded_by:              # 폐기 시 대체 카드 id
---
```

- 본문 형식 제안: `## 원칙` 1~2문장 → `## 언제 쓰나` → `## 적용 예시 프롬프트` → `## 근거` 원문 인용과 타임스탬프 → `## Old patterns` 폐기된 내용만.
- `model_context` 필드가 핵심이다. 사용자의 핵심 레퍼런스가 "이전 세대 모델에 맞춘 지시가 새 모델을 방해한다" 고 경고하기 때문이다. 이 필드가 있으면 모델 교체 시 영향받는 카드를 `grep` 으로 찾을 수 있다.
- `half_life` 는 3단계면 충분하다. 도구 기능·버전 관련 카드는 short, 작업 방식 카드는 medium, "불편함이 출발점" 같은 원칙은 long 으로 둔다.
- `index.md` 의 한 줄 형식 제안: `- [제목](cards/…/id.md): 한 줄 요약 · tags · review_by`. `review_by` 를 넣으면 Claude 가 index 만 읽어도 만료 여부를 안다.

### Gaps
- frontmatter schema 를 실제로 운영한 개인 사례의 효과 데이터는 찾지 못했다. 위 schema 는 공식 지침과 Karpathy 패턴에서 추론한 제안이다.
- `half_life` 기간(3개월·12개월)의 근거 수치는 없다. 사용자가 운영하며 조정해야 한다.

## Q4. "프롬프트 추천" skill 의 동작 방식과 공개 사례

### Takeaway
추천 skill 은 짧은 절차형 SKILL.md 로 시작한다. 절차는 다음과 같다. 사용자 작업 입력 → `index.md` 읽기 → 관련 카드 3~5장 읽기 → 만료 카드 표시 → 카드 id 를 인용한 프롬프트 제안 → "skill/카드 없이 plain prompt" 대안 병기. 공개 사례로는 `severity1/claude-code-prompt-improver`(hook + skill)와 Anthropic `skill-creator` 가 가장 가깝다. 레퍼런스 라이브러리 기반 추천 skill 의 정확한 공개 사례는 찾지 못했다.

### Cited Findings
- `severity1/claude-code-prompt-improver`: UserPromptSubmit hook 이 프롬프트가 모호한지 평가한다. 명확하면 그대로 진행한다. 모호하면 prompt-improver skill 을 불러 맥락을 조사하고 근거 있는 질문 1~6개를 묻는다. v0.4.0 에서 평가 프롬프트는 hook 에, 조사·질문은 `skills/prompt-improver/` 에 나눴다. 저자는 이 변경으로 토큰이 31% 줄었다고 보고한다. MIT 라이선스, 약 974 stars(집계 사이트 기준). — [awesome.ecosyste.ms](https://awesome.ecosyste.ms/projects/github.com%2Fseverity1%2Fclaude-code-prompt-improver); [newreleases.io v0.4.0](https://newreleases.io/project/github/severity1/claude-code-prompt-improver/release/v0.4.0)
- 이 프로젝트는 awesome-claude-code 목록에 포함된 것으로 집계 사이트가 표시한다. — [awesome.ecosyste.ms](https://awesome.ecosyste.ms/projects/github.com%2Fseverity1%2Fclaude-code-prompt-improver)
- `anthropics/skills` 저장소에서 전용 prompt-engineering skill 은 확인하지 못했다. 가장 가까운 것은 `skill-creator` 다. 2차 자료는 이 skill 이 3단계 progressive disclosure 와 eval 기반 개선 루프(테스트 작성 → 실행 → 채점 → 개선 → benchmark)를 담는다고 설명한다. — [prompt-context-patterns 카탈로그](https://wenbo97.github.io/prompt-context-patterns/catalog/categories/patterns-open-source-skills)
- 공식 skill 작성 지침의 "Research synthesis workflow" 예시는 체크리스트 형태다: 원천 읽기 → 주제 식별 → 주장 교차 확인 → 구조화 요약 → 인용 검증. 인용이 불완전하면 3단계로 돌아간다. — [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- 공식 지침은 평가를 먼저 만들라고 권한다. 순서는 "skill 없이 대표 작업 실행 → 실패 기록 → 시나리오 3개 → baseline 측정 → 최소 지시 작성 → 반복" 이다. — [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- 공식 지침은 Claude A(설계)·Claude B(실사용 테스트) 반복 방식을 권한다. — [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Skill description 은 3인칭으로 쓰고, 무엇을 하는지와 언제 쓰는지를 함께 쓴다. 최대 1,024자다(API 기준). — [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- 스킬을 쓰지 않는 선택도 필요하다는 원천 주장: "스킬을 완전히 빼면 결과가 더 좋아지는 경우도 있으니 … '그냥 프롬프트만 보내 보기'도 시도해 볼 것." — 로컬 파일 `references/클로드에게_일을_맡기는_법_실무레퍼런스.pdf` 196~197행
- 같은 PDF 0장 표는 "역할을 씌운다", "작업을 하나씩 집어 준다", "만든 세션이 채점한다" 를 2024년식으로 분류한다. 대안은 "최고의 사람이 거치는 단계와 도구를 밟게 한다", "바깥에서 채점한다" 다. — 로컬 파일 같은 PDF 1쪽

### Inferences

**`recommend-prompt` skill 초안 (시작용)**

```markdown
---
name: recommend-prompt
description: Recommends a prompt for a work task based on the ai-reference card library, citing the cards it used. Use when the user describes a task and asks how to prompt Claude for it, or says "프롬프트 추천", "이 일 어떻게 시키지".
argument-hint: [작업 설명]
---

1. Read `/Users/leeyoonsam/Documents/ai-reference/index.md`.
2. Pick 3–5 cards that match $ARGUMENTS. Read only those cards.
3. If a card has `review_by` before today or `status: needs-review`, mark it "재검증 필요".
4. Write one recommended prompt. Cite each applied card id inline.
5. Write one plain-prompt alternative that uses no card or skill.
6. Say which of the two to try first, and why, in one sentence.
```

- Claude 는 카드 원칙을 프롬프트 문장으로 "번역" 한다. 카드 본문을 그대로 붙이지 않는다. 이렇게 해야 최신 모델이 과잉 지시를 받지 않는다.
- 5단계의 plain-prompt 대안은 사용자의 핵심 레퍼런스(스킬 반감기 경고)를 절차에 내장하는 장치다.
- 처음에는 `context: fork` 를 쓰지 않는다. 추천은 현재 대화 맥락(무슨 일을 하는 중인지)이 필요하기 때문이다.
- 다른 저장소에서도 쓰려면 이 skill 을 `~/.claude/skills/recommend-prompt/` 에 두고 절대 경로를 쓴다. 이 저장소 전용이면 `.claude/skills/` 에 둔다.
- 프롬프트가 실제로 잘 동작하면 사용자는 결과를 `prompts/` 에 저장한다. 이것이 Karpathy 의 "좋은 query 답변을 wiki 에 다시 넣는다" 와 같은 루프다.
- prompt-improver 처럼 매 프롬프트마다 hook 을 거는 방식은 시작 단계에 과하다. 사용자가 명시적으로 `/recommend-prompt` 를 부르는 방식으로 시작한다.

### Gaps
- `anthropics/skills` 저장소의 현재 skill 목록을 GitHub 에서 직접 확인하지 않았다. 2차 자료만 확인했다.
- awesome-claude-code 원본 목록과 "prompt library" 형 저장소(카드 기반 추천)의 구체 사례는 찾지 못했다.
- prompt-improver 의 stars·토큰 절감 수치는 집계 사이트 기준이다. GitHub README 원문으로 재확인하지 않았다.

## Q5. 오래된 지식(stale knowledge) 관리 방법

### Takeaway
3가지 장치를 함께 쓴다. (1) 카드마다 `valid_as_of`·`review_by`·`model_context` 날짜 메타데이터를 둔다. (2) 폐기 내용은 지우지 않고 `Old patterns` 섹션이나 `status: deprecated` + `superseded_by` 로 옮긴다. (3) 정기 lint 를 한다. Karpathy 의 lint, Claude Code 의 `/doctor prompt-audit`, 모델 교체 시 "plain prompt 비교" 를 쓴다.

### Cited Findings
- Karpathy wiki 의 Lint 작업은 모순, 오래된 주장(stale claims), 고아 페이지, 누락 cross-reference, 데이터 공백을 정기 점검한다. — [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- Anthropic 은 시간에 민감한 정보를 본문에 쓰지 말라고 한다. 폐기된 방식은 날짜를 붙여 "Old patterns" 섹션에 접어 둔다. — [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Anthropic 은 지시 파일을 주기적으로 검토해 오래되거나 충돌하는 지시를 지우라고 권한다. 충돌하는 지시가 있으면 Claude 가 임의로 하나를 고를 수 있다. `/doctor prompt-audit` 가 이를 찾아 준다(v2.1.283 이상). — [Memory](https://code.claude.com/docs/en/memory)
- 모델 세대가 바뀌면 옛 프롬프트가 해가 될 수 있다는 공식 근거: "Claude Opus 4.5 and Claude Opus 4.6 are also more responsive to the system prompt than previous models. If your prompts were designed to reduce undertriggering on tools or skills, these models might now overtrigger. The fix is to soften any aggressive language." — [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 같은 문서의 migration 항목: "Tune anti-laziness prompting: If your prompts previously encouraged the model to be more thorough or use tools more aggressively, reduce that guidance." — [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 2026-10-29 현재 이 문서가 다루는 모델: Claude Fable 5.1, Mythos 5.1, Fable 5, Mythos 5, Opus 5.5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 5.5, Sonnet 5, Sonnet 4.6, Haiku 5.5, Haiku 4.5. — [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 공식 skill 지침은 skill 을 사용할 모든 모델(Haiku·Sonnet·Opus)로 테스트하라고 한다. "Does the Skill avoid over-explaining?" 를 Opus 점검 질문으로 든다. — [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- 공식 skill 지침은 skill 없는 baseline 을 먼저 측정하라고 한다. — [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Simon Willison TIL 은 index 항목마다 날짜를 붙인다. — [simonw/til](https://github.com/simonw/til)

### Inferences
- 신선도 점검은 3가지 트리거로 돌린다. (1) 월 1회 `/review-freshness` 를 실행한다. (2) 새 모델이 나오면 `model_context` 로 short 카드를 골라 재검증한다. (3) 새 원천을 ingest 할 때 기존 카드와 모순이 있는지 확인한다.
- `review-freshness` skill 은 결정적 작업이므로 스크립트를 함께 둔다. 공식 지침도 "Prefer scripts for deterministic operations" 라고 권한다. 예: frontmatter 의 `review_by < today` 인 카드 목록을 뽑는 짧은 스크립트.
- 재검증 방법: Claude 가 같은 작업을 "카드 적용 프롬프트" 와 "plain prompt" 로 각각 실행한다. 사용자가 결과를 비교한다. plain 쪽이 같거나 나으면 카드를 `deprecated` 로 바꾼다.
- 카드 내용이 바뀌면 `log.md` 에 1줄을 남긴다. git 이력이 세부 변경을 보존하므로 별도 버전 필드는 필요 없다.
- 반복 실행은 Claude Code 의 `/schedule`(cloud routine) 이나 `/loop` 로 자동화할 수 있다. 이 환경에 두 skill 이 있다. 시작 단계에서는 수동 실행을 권한다.

### Gaps
- 개인 지식베이스에서 "valid as of / review-by" 필드를 쓴 신뢰할 만한 공개 사례는 찾지 못했다. Docs-as-code 분야의 "last reviewed" 관행이 있으나 이번 조사에서 출처를 확보하지 않았다.
- 반감기 기간의 실증 데이터는 없다.

---

### 종합 추천: 1인 유지용 시작점 (보고서 작성자 참고용 추론)
1. `references/` 를 `raw/` 로 바꾸고, 파일 이름에 원본 날짜 접두어를 붙인다.
2. 루트에 `CLAUDE.md` 를 만든다. 내용은 폴더 규칙, 카드 frontmatter schema, ingest·query·lint 절차 요약이다. 100줄 이내로 쓴다.
3. 루트에 `index.md` 와 `log.md` 를 만든다.
4. Claude 에게 PDF 2개를 ingest 시킨다. 결과는 `sources/` 2개, `cards/` 10~20장, `index.md` 갱신이다.
5. `.claude/skills/recommend-prompt/SKILL.md` 1개만 만든다. 2주 실사용 뒤 ingest·freshness skill 을 더한다.
6. Plugin, hook, MCP 검색, vector DB 는 만들지 않는다. 공식 문서가 "트리거가 생길 때 더하라" 고 권하기 때문이다.

대안 비교 요약:

| 옵션 | 장점 | 단점 | 판단 |
|---|---|---|---|
| A. CLAUDE.md 에 전부 `@import` | 설정이 가장 쉽다 | 매 요청 전체 비용. 카드가 늘면 context rot | 쓰지 않는다 |
| B. 카드 파일 + index.md + skill 1~3개 | 읽기 전 비용 0. git·Obsidian 호환. Karpathy·Anthropic 지침과 일치 | 사용자가 ingest 습관을 유지해야 한다 | **시작점으로 추천** |
| C. B + 개인 skill(`~/.claude/skills`) | 다른 업무 저장소에서도 `/recommend-prompt` 사용 | 절대 경로 의존 | B 이후 1~2주 안에 전환 |
| D. Plugin + marketplace 배포 | 여러 기기·팀 공유 | 1인에게 과한 관리 비용 | 팀 공유가 필요할 때 |
| E. MCP 검색 서버(qmd 등) / RAG | 수백~수천 페이지 규모에서 검색 품질 | 인프라 유지 비용 | 카드가 수백 장을 넘을 때 |
| F. Notion/Obsidian 을 원본 저장소로 | 기존 도구 활용 | Claude Code 의 grep·git 이력과 분리 | git 을 원천으로 두고 Obsidian 은 뷰어로만 |
