# Lockscreen Ad SDK

앱에 잠금화면 광고 기능을 붙일 수 있게 해주는 SDK + 리워드 정산 백엔드.
개발자는 이 SDK를 앱에 추가하기만 하면, 별도의 잠금화면 앱을 새로 만들지 않고도
잠금화면 광고 지면을 확보하고 사용자에게 리워드를 지급할 수 있다.

## 로드맵

| 문서 | 한 줄 소개 | 상태 |
|---|---|---|
| [PLAN_LOCKSCREEN_AD.md](./PLAN_LOCKSCREEN_AD.md) | 잠금화면 광고 SDK 핵심 리워드 로직 | MVP 개발 중 |
| [PLAN_AD_TARGETING.md](./PLAN_AD_TARGETING.md) | 리뷰 감성 기반 광고 타겟팅 최적화 | 다음 스프린트 |

## 현재 상태

MVP 백엔드(`main.py`, `reward_engine.py`)만 구현된 초기 단계. 캠페인 데이터는
아직 인메모리로 처리하고 있고, PostgreSQL 연동은 다음 스프린트 예정
(`requirements.txt`에 드라이버만 먼저 추가해둠).

## 로컬 실행

\`\`\`bash
pip install -r requirements.txt
uvicorn main:app --reload
\`\`\`
