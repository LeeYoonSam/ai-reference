---
name: aside
description: YouTube 또는 글 링크 1개로 프로젝트 형식을 지키는 Aside 요청 프롬프트를 만들고, 클립보드에 복사하고, log.md 에 requested 줄을 남긴다. 사용자가 링크를 주며 "레퍼런스로 정리", "aside 프롬프트", "Aside 에 넣을 프롬프트" 라고 하거나 /aside 를 부를 때 쓴다.
argument-hint: "<YouTube 또는 글 링크>"
---

# /aside

저장소 루트는 `/Users/leeyoonsam/Documents/ai-reference` 다. 아래 경로는 모두 이 루트 기준 절대 경로로 쓴다.

## 1. 링크 확인

1. $ARGUMENTS 의 앞뒤 공백을 지운다. 결과를 링크로 쓴다.
2. 링크가 비어 있으면, 사용자에게 링크를 묻고 멈춘다.
3. 링크가 `http://` 나 `https://` 로 시작하지 않으면, 사용자에게 올바른 링크를 묻고 멈춘다.

## 2. 링크 종류와 문서 ID

1. 링크의 호스트가 `youtube.com`, `www.youtube.com`, `m.youtube.com`, `youtu.be` 중 1개이면, 종류를 `youtube` 로 정한다.
2. 그 밖의 링크는 종류를 `article` 로 정한다.
3. 종류가 `youtube` 이면, 아래 형식에서 영상 ID 를 뽑는다.
   - `youtube.com/watch?v=<영상 ID>` 는 `v` 파라미터 값을 쓴다.
   - `youtu.be/<영상 ID>` 는 경로 첫 부분을 쓴다.
   - `youtube.com/shorts/<영상 ID>` 는 `shorts/` 다음 경로 부분을 쓴다.
4. 쿼리 파라미터 `t`, `si`, `list` 는 버린다. 이 값은 같은 영상을 다른 문서 ID 로 만들기 때문이다.
5. 영상 ID 가 `[A-Za-z0-9_-]` 11자가 아니면, 사용자에게 영상 ID 를 뽑지 못했다고 알리고 멈춘다.
6. 종류가 `youtube` 이면, url 을 `https://www.youtube.com/watch?v=<영상 ID>` 로 정한다.
7. 종류가 `youtube` 이면, 문서 ID 를 `yt-<영상 ID>` 로 정한다.
8. 종류가 `article` 이면, url 을 사용자가 준 링크로 정한다.
9. 종류가 `article` 이면, 문서 ID 를 `web-<도메인>-<경로 마지막 부분>` 으로 정한다.
   - 도메인에서 앞의 `www.` 를 지운다.
   - 경로 마지막 부분은 비어 있지 않은 마지막 경로 조각이다. 경로가 없으면 `index` 를 쓴다.
   - 문서 ID 전체를 소문자로 바꾼다. `a-z`, `0-9`, `-` 밖의 글자는 `-` 로 바꾼다.

## 3. 중복 확인

1. `/Users/leeyoonsam/Documents/ai-reference/log.md` 가 없으면, log.md 에는 중복이 없다고 본다.
2. log.md 가 있으면, `grep -F '<문서 ID>' /Users/leeyoonsam/Documents/ai-reference/log.md` 로 문서 ID 를 찾는다.
3. `grep -rlF 'doc_id: <문서 ID>' /Users/leeyoonsam/Documents/ai-reference/notes/` 로 요약 노트의 frontmatter 를 찾는다.
4. 2단계나 3단계에서 찾은 줄이 있으면, 사용자에게 "이미 있음" 과 찾은 줄을 알리고 멈춘다. 같은 영상을 Aside 에 두 번 맡기지 않기 위해서다.

## 4. 템플릿 확인

1. 종류가 `article` 이고 `templates/aside-article.md` 가 없으면, 아래 3가지를 사용자에게 알리고 멈춘다.
   - 글 템플릿은 2단계 작업이다.
   - 그림이 필요 없는 글은 Aside 를 거치지 않아도 된다.
   - Claude 가 글을 직접 가져와서 `raw/` 에 저장하는 방법을 제안한다.
2. `/Users/leeyoonsam/Documents/ai-reference/templates/aside-<종류>.md` 를 Read 한다.
3. 템플릿 파일의 ```` ```text ```` 블록 1개의 내용만 꺼낸다. 맨 위의 주석은 프롬프트에 넣지 않는다.

## 5. 프롬프트 만들기

1. `{{url}}` 을 모두 2절에서 정한 url 로 바꾼다.
2. `{{doc_id}}` 를 모두 문서 ID 로 바꾼다.
3. 그 밖의 문장은 바꾸지 않는다. 형식 규칙의 원본은 `templates/` 1곳에만 두기 때문이다.
4. 결과에 `{{` 가 남아 있으면, 사용자에게 템플릿 자리표시자 오류를 알리고 멈춘다.
5. 완성된 프롬프트를 ```` ```text ```` 코드 블록 1개로 사용자에게 보여 준다.

## 6. 클립보드 복사

1. 아래 명령으로 프롬프트를 클립보드에 복사한다. heredoc 은 프롬프트 안의 따옴표를 그대로 지킨다.

   ```bash
   printf '%s' "$(cat <<'ASIDE_PROMPT'
   <완성된 프롬프트>
   ASIDE_PROMPT
   )" | pbcopy
   ```

2. 복사가 성공하면, 사용자에게 "클립보드에 복사함" 이라고 알린다.
3. 복사가 실패하면, 사용자에게 실패를 알린다. 5절의 코드 블록에서 직접 복사하라고 안내한다.

## 7. 작업 기록

1. `date +%F` 로 오늘 날짜를 얻는다.
2. log.md 가 없으면, `# 작업 기록` 머리글과 빈 줄 1개로 log.md 를 만든다.
3. log.md 의 마지막 글자가 줄바꿈이 아니면, 줄바꿈 1개를 먼저 더한다.
4. log.md 맨 끝에 `YYYY-MM-DD requested | <문서 ID> | <url>` 줄 1개를 `>>` 로 더한다.
5. log.md 의 기존 줄은 고치거나 지우지 않는다. log.md 는 줄을 추가만 하는 작업 기록이기 때문이다.

## 8. 다음 행동 안내

1. 사용자에게 아래 2가지를 안내한다.
   - 프롬프트를 Aside 에 붙여 넣는다.
   - Aside 의 요약이 끝나면, Claude 에게 "가져와줘" 라고 말한다.
2. Aside 를 직접 열거나 조작하지 않는다. Aside 작업은 사용자가 하기 때문이다.
