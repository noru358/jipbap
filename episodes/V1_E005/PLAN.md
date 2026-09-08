# V1_E005 PLAN

Status: PRESENTATION_MASTER_DRAFT
Food: 엽기떡볶이
Format: COVER 1 + BODY 6
Architecture: SIX_PANEL_BOARD_FIRST
Presentation shell: JIPBAP_PRESENTATION_SHELL_V2

## Episode intent

회사에서 상사에게 깨진 날, 퇴근길의 분노를 매운 엽기떡볶이로 풀어내는 PROXY_EATER 에피소드.
초반 2컷은 감정 상황을 빠르게 설명하고, S03부터 음식/먹는 동작/감각 payoff가 중심이다.

## Approval state

- STORYBOARD_USER_GATE: APPROVED
- JIPBAP_FOOD_STYLE_CARRIER_V1: USER_LOCKED
- BODY master BOARD: APPROVED
- COVER hero: APPROVED
- FINAL_PUBLISH_GATE: PENDING_QUALITY_FIRST_PRESENTATION_MASTER

## COVER

Title fields:
- episode_no: 5
- topic_phrase: 박살난 멘탈
- food_name: 엽기떡볶이
- composed title: EP.5 박살난 멘탈과 엽기떡볶이

Distinct COVER hero:
- BODY 셀 재사용 없음.
- 집 식탁에서 치즈 엽떡을 앞에 둔 주인공.
- 매워서 눈가가 살짝 촉촉하지만 젓가락은 다음 떡을 향함.
- 음식이 주초점, 인물은 강한 보조 초점.
- 상단 title-safe negative space 확보.

## BODY storyboard / approved copy

### S01 — 퇴근길 / 멘탈 박살

Visual:
- 회사에서 상사에게 깨진 장면을 회상하며 집으로 터덜터덜 걷는 주인공.
- 저녁 퇴근길, 어깨가 처지고 피곤하고 화가 남.
- 회상은 무문자 흐릿한 기억 요소로만 표현.

Copy:
- inner thought: "아직도 열받네..."

### S02 — 엽떡 가게 / 분노 급전환

Visual:
- 같은 가게 정면 한 공간 안에서 time-compression comedy.
- 화면 안쪽의 작은 주인공은 화난 채 들어감.
- 전경의 큰 주인공은 포장 봉투를 들고 가볍게 나옴.
- 두 시점은 별도 패널처럼 분할하지 않음.

Copy:
- dialogue 없음.
- 콧노래 느낌의 비언어 SFX만 허용.

### S03 — 뚜껑 여는 순간

Visual:
- 집 식탁에서 포장 용기를 열음.
- 빨간 엽떡 위에 모짜렐라 치즈가 녹아 있음.
- 김/열기와 향이 올라오고 음식이 주초점.

Copy:
- inner thought: "냄새 미쳤다... 벌써부터 매워"

Continuity:
- 아직 먹기 전이므로 맛/식감 claim 없음.

### S04 — 양념 묻은 떡 집기

Visual:
- 양념이 잔뜩 묻은 떡을 젓가락으로 집어 올리는 클로즈업.
- 입에는 아직 닿지 않음.
- 음식은 appetizing illustrated style을 유지하고 사진식 질감으로 점프하지 않음.

Copy:
- narration / inner voice: "양념 잔뜩 묻은 떡을 집어서..."

### S05 — 첫입 / 식감 payoff

Visual:
- 떡이 실제로 입에 들어간 상태가 명확함.
- 입/젓가락/떡 접촉이 자연스러움.
- 매운맛과 만족이 함께 읽히는 반응.

Copy:
- inner thought: "쫀득하고 달큰해. 혀에 달라 붙는다 ㅠㅠ"

Continuity:
- 실제 ingestion 이후이므로 맛/식감 표현 허용.

### S06 — 매운데 다음은 소세지

Visual:
- 눈물이 맺힐 정도로 맵지만 만족감이 남음.
- 한 손은 입가 쪽, 다른 손의 젓가락은 다음 소세지를 향함.
- 음식도 계속 화면에 충분히 보임.

Copy:
- inner thought 1: "매워"
- inner thought 2: "다음은 소세지~"

## Visual rhythm

- S01: 멀고 무거운 퇴근길
- S02: 정면 고정 코미디 / 입장-퇴장 대비
- S03: 음식 reveal
- S04: 음식+손 detail
- S05: 얼굴 반응 close-up
- S06: 음식+인물 medium
- 다양성은 story benefit에 따라 유지하고 기계적 shot template으로 고정하지 않는다.

## Runtime receipts

Food style carrier:
- session SHA-256: e2cb04ff82671fff655830b1a3be540561d3dde108eb18bed7a8cc6d09a9c73a
- dimensions: 1254 × 1254
- status: USER_LOCKED_SESSION_VALIDATED

Approved BODY BOARD:
- SHA-256: f1c27c4a635406d616f1649127318767ba22ba5d2d51f87088db4808fd76c126
- dimensions: 1024 × 1536
- six-cell extraction geometry: x interiors [12,503], [520,1012]; y interiors [9,487], [504,986], [1003,1522]
- BOARD user approval: APPROVED

Approved distinct COVER hero:
- SHA-256: eba699359373e2534fe5edcfd027c78af0e77962c2609607b086047960828fc8
- dimensions: 1122 × 1402
- COVER user approval: APPROVED

## Presentation architecture revision

User structural feedback on 2026-09-09:
- the prior tool-first final candidate visibly degraded bubble/typography quality versus earlier quality-first lettered drafts;
- root cause classification: editor/shell defaults were being used as upstream design authority rather than downstream editable representation;
- approved BODY BOARD and COVER artwork remain accepted and unchanged;
- presentation stage is reopened only.

New path:
1. Build a quality-first fully lettered 7-page `PRESENTATION_MASTER_DRAFT` from the approved artwork/copy, without constraining creative presentation to current ToonDesk defaults.
2. Use that completed carousel at `FINAL_PUBLISH_GATE`.
3. After approval, reconstruct its presentation intent into `EDITABLE_COMPOSITION_PACKAGE_V1` using exact approved artwork bytes and exact approved copy.
4. Bind page-level presentation-target provenance/hash.
5. Run `PRESENTATION_PARITY_QC`.
6. If ToonDesk cannot reproduce the approved bubble/font/layout quality, extend editor/scene capability rather than simplifying the approved design.
7. Persist canonical package and receipt only after parity passes.

## Exact next action

Create the quality-first fully lettered seven-page `PRESENTATION_MASTER_DRAFT` for V1_E005 from the already approved BODY BOARD and COVER hero. Do not regenerate artwork.
