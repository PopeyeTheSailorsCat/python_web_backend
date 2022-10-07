from pydantic import BaseModel
from typing import List
from app.contracts.user_contract import User


class Team(BaseModel):
    name: str
    track: str
    members: List[User]
