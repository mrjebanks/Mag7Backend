
from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.models import Fixture
from app.db.database import SessionLocal

router = APIRouter(prefix="/fixtures")

class FixtureCreate(BaseModel):
    home_team: str
    away_team: str
    match_date: str

@router.post("/add")
def add_fixture(fixture: FixtureCreate):
    db: Session = SessionLocal()
    new_fixture = Fixture(**fixture.dict())
    db.add(new_fixture)
    db.commit()
    db.refresh(new_fixture)
    return new_fixture
