from pydantic import BaseModel
from typing import List
from app.contracts.team_contract import Team


class Track(BaseModel):
    name: str
    description: str
    teams: List[Team]
