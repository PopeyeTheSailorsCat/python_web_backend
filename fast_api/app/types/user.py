from typing import List


class User(BaseModel):
    name: str
    skills: List[str]
