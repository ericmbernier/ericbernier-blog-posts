from pydantic import BaseModel
from typing import List

from underdog_fastapi.underdog.team import Team


class PlayerBase(BaseModel):
    first_name: str
    last_name: str
    adp: float = None
    projected_points: float = None
    team_name: str
    team_abbreviation: Team


class Player(PlayerBase):
    id: int
    bye_week: int = None

    class Config:
        orm_mode = True


class PlayerStack(BaseModel):
    players: List[PlayerBase]
    average_adp: float
    median_adp: float
    projected_points_per_week: float
