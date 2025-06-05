
from fastapi import APIRouter
from pydantic import BaseModel
from app.db.database import SessionLocal
from app.db.models import Pick

router = APIRouter(prefix="/picks")

class PickCreate(BaseModel):
    user_id: int
    fixture_id: int
    team_chosen: str

@router.post("/make")
def make_pick(pick: PickCreate):
    db = SessionLocal()
    new_pick = Pick(**pick.dict())
    db.add(new_pick)
    db.commit()
    db.refresh(new_pick)
    return new_pick
