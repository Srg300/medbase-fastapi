from typing import List, Optional

from pydantic import BaseModel


class PillBase(BaseModel):
    name: str
    is_active: bool



class Pill(PillBase):
    id: int

    class Config:
        orm_mode = True


class RecipeBase(BaseModel):
    days: str
    times: str
    pill_id: int
    pill: List[Pill] = []



class Recipe(RecipeBase):
    id: int

