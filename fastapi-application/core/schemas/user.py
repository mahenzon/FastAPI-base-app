from datetime import datetime
from typing import Literal

from pydantic import BaseModel
from pydantic import ConfigDict


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
    created_at: datetime


class UserStatsRequest(BaseModel):
    user_id: int
    stat_type: Literal["addresses", "spam-and-eggs"]


class UserStatsResponse(BaseModel):
    user_id: int
    stat_type: Literal["addresses", "spam-and-eggs"]
    addresses: int = 0
