# AOD Brand Message SDK

앱에 Always-On Display(AOD) 브랜드 메시지 노출 기능을 붙일 수 있게 해주는
SDK + 리워드 정산 백엔드. 잠금화면 자체는 건드리지 않고, 저전력 상시노출
영역만 활용한다. 리워드는 잠금 해제와 무관하게, 사용자가 앱 내 리워드
센터를 능동적으로 열람했을 때 외부 제휴 포인트로 지급된다.

## 로드맵

| 문서 | 한 줄 소개 | 상태 |
|---|---|---|
| [PLAN_LOCKSCREEN_AD.md](./PLAN_LOCKSCREEN_AD.md) | AOD 브랜드 메시지 SDK 핵심 리워드 로직 | MVP 개발 중 |
| [PLAN_AD_TARGETING.md](./PLAN_AD_TARGETING.md) | 사용자 선택 카테고리 기반 광고 노출 빈도 조절 | 다음 스프린트 |

## 현재 상태

MVP 백엔드(`main.py`, `reward_engine.py`)만 구현된 초기 단계. 캠페인 데이터는
아직 인메모리로 처리하고 있고, PostgreSQL 연동은 다음 스프린트 예정
(`requirements.txt`에 드라이버만 먼저 추가해둠).

## 로컬 실행

\`\`\`bash
pip install -r requirements.txt
uvicorn main:app --reload
\`\`\`

\`\`\`bash
pip install -r requirements.txt
uvicorn main:app --reload
\`\`\`
