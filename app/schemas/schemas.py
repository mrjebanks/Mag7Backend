from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    email: str
    name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    is_admin: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class PickBase(BaseModel):
    week: int
    team: str

class PickCreate(PickBase):
    pass

class PickOut(PickBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
