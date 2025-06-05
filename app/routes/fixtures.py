
from fastapi import APIRouter, HTTPException
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
    try:
        new_fixture = Fixture(
            home_team=fixture.home_team,
            away_team=fixture.away_team,
            match_date=fixture.match_date,
        )
        db.add(new_fixture)
        db.commit()
        db.refresh(new_fixture)
        return {"message": "Fixture added", "fixture_id": new_fixture.id}
    finally:
        db.close()
