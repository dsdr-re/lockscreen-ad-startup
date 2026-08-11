"""잠금화면 광고 SDK의 리워드 정산 백엔드 (MVP).

현재는 인메모리 저장소를 쓰고 있고, PostgreSQL 연동은 requirements.txt에
psycopg2-binary만 먼저 추가해둔 상태 — 다음 스프린트에 실제 연동 예정.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from reward_engine import UnlockEvent, calculate_reward

app = FastAPI(title="Lockscreen Ad Reward API")

# TODO: psycopg2로 PostgreSQL 연동 예정 — 지금은 인메모리로 MVP만 구현
_campaigns: dict[str, dict] = {}
_user_points: dict[str, int] = {}


class CampaignCreate(BaseModel):
    name: str
    ad_duration_seconds: int


class UnlockEventRequest(BaseModel):
    user_id: str
    campaign_id: str
    view_duration_seconds: int
    unlocked: bool


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/campaigns")
def create_campaign(campaign: CampaignCreate):
    campaign_id = f"camp_{len(_campaigns) + 1}"
    _campaigns[campaign_id] = campaign.model_dump()
    return {"campaign_id": campaign_id, **campaign.model_dump()}


@app.get("/campaigns")
def list_campaigns():
    return _campaigns


@app.post("/events/unlock")
def record_unlock_event(req: UnlockEventRequest):
    campaign = _campaigns.get(req.campaign_id)
    if not campaign:
        raise HTTPException(status_code=404, detail="campaign not found")

    event = UnlockEvent(
        user_id=req.user_id,
        campaign_id=req.campaign_id,
        ad_duration_seconds=campaign["ad_duration_seconds"],
        view_duration_seconds=req.view_duration_seconds,
        unlocked=req.unlocked,
    )
    points = calculate_reward(event)
    _user_points[req.user_id] = _user_points.get(req.user_id, 0) + points
    return {"points_earned": points, "total_points": _user_points[req.user_id]}


@app.get("/users/{user_id}/points")
def get_user_points(user_id: str):
    return {"user_id": user_id, "total_points": _user_points.get(user_id, 0)}
