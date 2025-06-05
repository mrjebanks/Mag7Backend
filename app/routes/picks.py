
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.db.database import SessionLocal
from app.db.models import Pick

router = APIRouter()

class PickCreate(BaseModel):
    fixture_id: int
    team_chosen: str

@router.post("/picks/make")
def make_pick(pick: PickCreate):
    db = SessionLocal()
    new_pick = Pick(**pick.dict(), user_id=1)  # Replace with real user logic
    db.add(new_pick)
    db.commit()
    db.refresh(new_pick)
    db.close()
    return {"message": "Pick saved", "id": new_pick.id}
