from pydantic import BaseModel
from typing import List


class User(BaseModel):
    name: str
    mail: str
    skills: List[str]
