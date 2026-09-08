# V1_E006 PLAN

Status: EXTRACT_FIT
Food: 두부조림
Format: COVER 1 + BODY 6
Architecture: SIX_PANEL_BOARD_FIRST
Presentation shell: JIPBAP_PRESENTATION_SHELL_V2

## Reset receipt

- Reset date: 2026-09-09
- Reset authority: explicit user instruction
- Previous V1_E006 iteration: DISCARDED
- Previous storyboard approval: REVOKED
- Previous BODY approval / generation id / hash: REVOKED_AS_RUNTIME_AUTHORITY
- Previous COVER attempts: REJECTED_NON_CANONICAL
- Reuse rule: do not reuse any previous E006 storyboard, BODY/COVER artwork, generation provenance, approval identity or stale scene semantics.
- Git history may retain the discarded iteration for provenance only.

## Episode intent

비 오는 날 먹자골목을 지나가다 두부조림 냄새에 발이 붙잡히고, 결국 들어가 한 접시 먹는다.
첫입의 뜨끈하고 부드러운 두부보다 한 번 더 강한 payoff는 마지막이다.
남은 두부와 양념을 흰밥 위에 올린 뒤 숟가락으로 막 으깨며 쓱쓱 비비고, 그 밥을 크게 한입 먹는다.

조리법 설명보다:
- 비 오는 골목의 공기와 따뜻한 음식 냄새의 대비,
- 양념 밴 두부의 뜨거움과 부드러움,
- 숟가락으로 두부를 깨뜨릴 때의 촉감과 밥알 사이로 양념이 번지는 시각,
- 두부+양념+밥이 한 숟갈에 합쳐지는 2차 payoff
를 중심으로 한다.

배경은 S01의 먹자골목과 식당 맥락을 읽히는 정도만 사용하고, 이후에는 음식·손동작·표정 중심으로 단순화한다.

## Approval state

- STORYBOARD_USER_GATE: APPROVED
- BODY master BOARD: APPROVED_AND_LOCKED
- BODY generation id: `54838e01-8a57-41ad-8ab2-e3b2517cec0e`
- BODY session SHA-256: `10fa1ed93513497a3372e43f50416ab57710a83fb2e27ef70efe6cc753e0341d`
- BODY dimensions: 1024 × 1536
- COVER hero: APPROVED_AND_LOCKED
- COVER generation id: `100db926-2200-4ecf-8db7-9b8a6cb01639`
- COVER session SHA-256: `fd7cc633fdf13e2c50d505f884390b7474ace94ce8d11933e75d69a059aee284`
- COVER dimensions: 1122 × 1402
- ART_BUNDLE_USER_GATE: APPROVED
- FINAL_PUBLISH_GATE: NOT_STARTED

## Post-approval presentation QC

The first seven-page lettered attempt after artwork approval is rejected and non-canonical.

Reason:
- it used stochastic image generation to recreate COVER and each BODY page instead of preserving the exact approved COVER/BODY pixels;
- therefore character pose, background, food rendering and composition changed after the artwork lock;
- this violates approved-art immutability and approval identity;
- S05 also became less explicit about the spoon actively crushing the tofu at the visible contact moment, weakening the episode's required signature action.

Disposition:
- keep the approved BODY/COVER sources locked;
- discard only the seven regenerated lettered pages;
- rebuild from actual BODY border extraction + exact COVER FIT + presentation overlays.

## COVER storyboard

Role:
- episode hero / rain-day craving

Visual intent:
- 비가 맺힌 식당 창가 안쪽.
- 전경에는 김이 살짝 오르는 두부조림과 흰밥.
- 주인공은 막 숟가락을 들고 두부조림을 바라보는 기대감 있는 표정.
- 비 오는 바깥과 따뜻한 실내의 대비가 한눈에 읽히되 배경 디테일은 최소화.
- 제목을 얹을 자연스러운 여백은 남기지만 텍스트는 이미지 생성 단계에서 넣지 않는다.
- 카메라·구도·포즈·표정은 COVER 역할에 맞게 자유롭게 설계한다.

Working title:
- episode_no: 6
- topic_phrase: 비 오는 날
- food_name: 두부조림
- composed title candidate: `EP.6 비 오는 날과 두부조림`

## BODY storyboard / copy draft

### S01 — 비 오는 먹자골목, 냄새에 멈춤

Story function:
- trigger / craving hook

What becomes new:
- 비를 피해 지나가던 주인공이 식당 쪽에서 올라오는 두부조림 냄새를 맡고 걸음을 멈춘다.

Visual:
- 젖은 골목 바닥과 몇 개의 작은 식당 간판만 읽히는 먹자골목.
- 우산을 쓴 주인공이 걷다가 고개를 살짝 돌려 냄새가 오는 방향을 찾는 순간.
- 열린 식당 문이나 환기구 쪽에서 따뜻한 김/향의 흐름을 아주 절제되게 표현.
- 비 오는 배경은 분위기만 전달하고 인물·향의 방향이 주초점.

Person / food state:
- 아직 음식을 보거나 먹지 않음.
- 냄새만 먼저 감지.

Copy:
- inner_thought: `어? 두부조림 냄새.`

Camera / focus:
- 골목 맥락이 보이는 미디엄 와이드.
- 인물의 멈춘 동작과 고개 방향이 읽혀야 함.

Copy-space hint:
- 우산과 얼굴을 피한 상단 또는 측면 여백.

Avoid:
- 얼굴, 우산 손, 향이 오는 방향을 가리지 않는다.

Continuity:
- 다음 컷에서 식당 안의 실제 두부조림을 확인하게 된다.

### S02 — 자리에 앉자마자 두부조림 등장

Story function:
- reveal / appetite escalation

What becomes new:
- 냄새의 정체가 실제 두부조림 한 접시로 확인된다.

Visual:
- 식탁 위 막 나온 두부조림을 음식 중심으로 보여준다.
- 붉은 갈색 양념이 두부에 배어 있고 파/양파 같은 고명이 자연스럽게 보이되 과도한 실사 광택은 피한다.
- 흰밥 그릇이 옆에 있어 곧 함께 먹을 상황을 암시.
- 주인공의 손이나 상반신 일부는 있어도 되지만 음식이 주초점.

Person / food state:
- 먹기 직전.
- 두부와 밥은 아직 분리된 상태.

Copy:
- inner_thought: `비 오는 날 이 냄새는 못 지나치지.`

Camera / focus:
- 3/4 음식 클로즈.

Copy-space hint:
- 접시와 밥그릇을 피한 한쪽 여백.

Avoid:
- 두부 표면, 양념, 밥그릇을 가리지 않는다.

Continuity:
- S01에서 맡은 냄새의 원인이 자연스럽게 이어진다.

### S03 — 뜨거운 두부 첫입

Story function:
- first ingestion / flavor payoff

What becomes new:
- 두부조림이 처음 실제로 입에 들어간다.

Visual:
- 젓가락으로 집은 두부 한 조각을 입에 넣는 순간.
- 두부가 지나치게 단단한 큐브처럼 보이지 않고 부드러운 조직이 약간 느껴져야 함.
- 눈썹과 입 주변에 뜨거움+만족감이 동시에 읽히는 현실적인 반응.
- 접시와 밥은 프레임 일부에만 남겨 식사 맥락 유지.

Person / food state:
- 첫입 섭취 성립.
- 밥은 아직 흰밥 그대로.

Copy:
- inner_thought: `아 뜨거. 근데 두부 진짜 부드럽다.`

Camera / focus:
- 얼굴과 젓가락 접촉이 보이는 3/4 미디엄 클로즈.

Copy-space hint:
- 얼굴과 젓가락 경로 반대편의 측면 여백.

Avoid:
- 눈, 입, 젓가락, 두부를 가리지 않는다.

Continuity:
- 맛/식감 문구는 실제 섭취가 성립한 이 컷부터 사용.

### S04 — 밥 위에 두부와 양념 올리기

Story function:
- setup for second payoff

What becomes new:
- 그냥 두부만 먹던 흐름에서 밥과 합칠 준비로 전환한다.

Visual:
- 흰밥 위에 두부 한 조각과 양념을 숟가락 또는 젓가락으로 올리는 순간.
- 밥 일부는 여전히 새하얗고, 양념이 닿은 부분만 막 물들기 시작함.
- 두부는 아직 비교적 큰 조각으로 형태가 남아 있어 다음 컷의 으깨기 행동이 가능해야 함.

Person / food state:
- S03 이후.
- 아직 두부를 으깨지 않음.
- 비빈 밥도 아직 먹지 않음.

Copy:
- speech 또는 inner_thought: `이제 이걸 밥에다가...`

Camera / focus:
- 밥그릇과 손동작 중심의 하이앵글 클로즈.

Copy-space hint:
- 손과 밥그릇 외곽을 피한 작은 측면 여백.

Avoid:
- 밥 위 두부, 양념이 떨어지는 경계, 손 접촉부를 가리지 않는다.

Continuity:
- S05에서 이 큰 두부 조각이 실제로 으깨지기 시작한다.

### S05 — 막 으깨서 쓱쓱 비비는 중

Story function:
- tactile transformation / signature action

What becomes new:
- 숟가락이 두부를 눌러 깨뜨리면서 밥과 양념을 실제로 섞기 시작한다.

Visual:
- 완성된 비빔밥이 아니라 **막 으깨고 있는 진행 중 순간**.
- 밥 위 큰 두부 조각 일부는 아직 남아 있고, 숟가락 아래쪽만 작은 덩어리로 깨지는 중.
- 양념이 흰밥 사이로 퍼져 흰 부분과 붉은 갈색 부분이 동시에 보임.
- 숟가락이 두부를 누르고 끌면서 밥알과 섞이는 접촉부를 가장 맛있게 보여준다.
- 얼굴은 생략 가능. 손·숟가락·밥그릇이 주초점.

Person / food state:
- 두부 으깨기와 밥 비비기가 현재 진행 중.
- 아직 이 혼합밥을 먹지 않음.

Copy:
- sfx: `쓱쓱`
- optional inner_thought: `이렇게 으깨야 돼.`

Camera / focus:
- 탑다운에 가까운 극근접 또는 높은 하이앵글.
- 숟가락 끝과 으깨지는 두부/밥의 경계가 주초점.

Copy-space hint:
- SFX만 동작선 주변의 작은 여백에 배치.

Avoid:
- 숟가락 끝, 두부가 깨지는 부분, 양념이 번지는 경계를 가리지 않는다.

Continuity:
- S04의 큰 두부 조각이 그대로 이어져야 한다.
- 이미 전부 으깨진 상태로 시작하면 안 된다.

### S06 — 두부 비빈 밥 크게 한입

Story function:
- second ingestion / final payoff

What becomes new:
- S05에서 만든 두부+양념+밥 조합을 실제로 먹는다.

Visual:
- 숟가락 위에 양념 밴 밥과 잘게 으깨진 두부가 같이 보임.
- 주인공이 그 숟가락을 크게 한입 먹고, 만족감이 바로 올라오는 순간.
- 밥그릇 안에는 완전히 균질한 죽처럼 섞인 것이 아니라 밥알과 작은 두부 덩어리가 살아 있음.
- 음식이 충분히 보이도록 구성하고 표정만 남는 얼굴 클로즈업은 피한다.
- 마무리 장면은 식탁과 밥그릇까지 읽히는 조금 더 여유 있는 구도로 설계해, 첫입과 다른 리듬을 준다.

Person / food state:
- 비빈 밥 첫 섭취 성립.
- S05의 혼합 상태가 자연스럽게 이어짐.

Copy:
- inner_thought: `양념 밴 밥에 두부까지 풀리니까 그냥 술술 들어가네.`

Camera / focus:
- 인물+숟가락+밥그릇이 함께 읽히는 미디엄 3/4 또는 살짝 낮은 앵글.

Copy-space hint:
- 얼굴과 숟가락 동선을 피한 측면 여백.

Avoid:
- 눈, 입, 숟가락 내용물, 밥그릇을 가리지 않는다.

Continuity:
- S05에서 섞은 밥이 그대로 이어져야 한다.
- 밥이 다시 완전한 흰밥으로 리셋되거나 두부가 온전한 큰 조각으로만 돌아가면 안 된다.

## Overall visual rhythm

- S01: 비 오는 먹자골목 미디엄 와이드
- S02: 음식 중심 3/4 클로즈 reveal
- S03: 얼굴+젓가락 첫입 미디엄 클로즈
- S04: 밥그릇/손 하이앵글 클로즈
- S05: 으깨는 접촉부 극근접
- S06: 인물+숟가락+밥그릇이 함께 보이는 여유 있는 마무리

이 리듬은 이번 에피소드의 스토리 선택이며 영구 슬롯 템플릿이 아니다.

## Copy rhythm

- S01은 냄새를 알아채는 짧은 혼잣말.
- S02는 비 오는 날의 욕구를 한 줄로 연결.
- S03에서 실제 첫 섭취 뒤에 뜨거움/부드러움을 말함.
- S04는 말끝을 열어 다음 행동을 예고.
- S05는 `쓱쓱` 동작감을 중심으로 텍스트를 최소화.
- S06에서 두부가 밥에 풀린 식감을 최종 payoff로 설명.
- 문어체보다 실제 혼잣말/커뮤니티 말투에 가깝게 유지하되 과도한 유행어 남발은 피한다.

## Exact next action

1. Present this restarted COVER + S01..S06 storyboard to the user.
2. Stop at STORYBOARD_USER_GATE.
3. If approved, bind the USER_LOCKED PERSON/FOOD renderer carriers in the approval turn.
4. Generate a fresh INITIAL_ART_BUNDLE: BODY 2×3 master board + independent COVER hero.
5. Never reuse the discarded E006 iteration as authority.


## Presentation draft v2 QC

Status: `REJECTED_NON_CANONICAL_FOR_PIPELINE`

Visual findings:
- COVER lettering/layout: GOOD.
- S01: GOOD hook and readability.
- S02: GOOD as a presentation image, but artwork staging changed from the approved source cell.
- S03: ingestion and hot/soft reaction read correctly.
- S04: intact tofu-on-rice setup reads correctly.
- S05: improved active-mixing readability; still does not show the spoon visibly deforming a large tofu piece as explicitly as intended.
- S06: payoff reads correctly.
- all literal copy appears visually correct.
- repeated cloud-shaped thought bubbles are a soft quality issue.

Pipeline finding:
- FAIL. The draft was created by stochastic page-level image generation rather than actual approved-BOARD border extraction + exact-pixel 4:5 FIT + presentation overlays.
- do not use these pixels as artwork authority or canonical FIT outputs.
- remain at `EXTRACT_FIT`.

Required next action:
1. extract S01..S06 from the exact approved BODY bytes with the existing border detector;
2. persist `JIPBAP_BOARD_EXTRACTION_V1` box/output hashes;
3. 4:5 FIT the exact extracted rasters and exact approved COVER without stretch/redraw;
4. add title/bubble/text/SFX as presentation-layer overlays;
5. only then build/show the seven-page presentation master.
