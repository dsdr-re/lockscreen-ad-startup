"""잠금화면 광고 시청 행동을 기반으로 리워드 포인트를 계산하는 핵심 로직.

PLAN_LOCKSCREEN_AD.md의 "광고 시청·해제 행동에 따라 리워드 포인트를 적립하는 로직"에
해당하는 부분 — 이 SDK의 핵심 아이디어라 특허 검토 대상 1순위.
"""

from dataclasses import dataclass

MIN_VIEW_SECONDS_TO_QUALIFY = 3  # 이 시간 미만이면 광고를 실제로 본 것으로 인정하지 않음
BASE_POINTS_PER_VIEW = 10
FULL_VIEW_BONUS_MULTIPLIER = 1.5  # 광고를 끝까지 본 경우 보너스


@dataclass
class UnlockEvent:
    user_id: str
    campaign_id: str
    ad_duration_seconds: int  # 광고 소재의 전체 길이
    view_duration_seconds: int  # 사용자가 실제로 본 시간
    unlocked: bool  # 잠금화면을 실제로 해제했는지 (광고만 보고 안 지나간 경우 방지)


def calculate_reward(event: UnlockEvent) -> int:
    """하나의 잠금화면 광고 시청 이벤트에 대해 지급할 포인트를 계산한다.

    규칙:
    - 잠금화면을 해제하지 않았으면 0점 (광고만 노출되고 실제 행동이 없었던 경우 방지)
    - 최소 시청 시간(MIN_VIEW_SECONDS_TO_QUALIFY) 미만이면 0점
    - 광고를 끝까지(전체 길이만큼) 봤으면 보너스 배율 적용
    """
    if not event.unlocked:
        return 0
    if event.view_duration_seconds < MIN_VIEW_SECONDS_TO_QUALIFY:
        return 0

    points = BASE_POINTS_PER_VIEW
    if event.view_duration_seconds >= event.ad_duration_seconds:
        points = int(points * FULL_VIEW_BONUS_MULTIPLIER)
    return points
