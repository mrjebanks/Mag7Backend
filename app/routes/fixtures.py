
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from app.db.database import SessionLocal
from app.db.models import Fixture

router = APIRouter()

class FixtureCreate(BaseModel):
    home_team: str
    away_team: str
    match_date: datetime

@router.post("/fixtures/add")
def add_fixture(fixture: FixtureCreate):
    db = SessionLocal()
    new_fixture = Fixture(**fixture.dict())
    db.add(new_fixture)
    db.commit()
    db.refresh(new_fixture)
    db.close()
    return {"message": "Fixture added", "id": new_fixture.id}
