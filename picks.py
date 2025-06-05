from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from database import SessionLocal
from models import Pick, User
from pydantic import BaseModel
import datetime
import os

SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
ALGORITHM = "HS256"

picks_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_from_token(token: str, db: Session):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

class PickRequest(BaseModel):
    token: str
    matchweek: int
    team: str

@picks_router.post("/make")
def make_pick(pick_data: PickRequest, db: Session = Depends(get_db)):
    user = get_user_from_token(pick_data.token, db)
    existing = db.query(Pick).filter(Pick.user_id == user.id, Pick.matchweek == pick_data.matchweek).first()
    if existing:
        raise HTTPException(status_code=400, detail="Pick already made this week")
    past_pick = db.query(Pick).filter(Pick.user_id == user.id, Pick.team == pick_data.team).first()
    if past_pick:
        raise HTTPException(status_code=400, detail="Team already picked this season")
    new_pick = Pick(user_id=user.id, matchweek=pick_data.matchweek, team=pick_data.team)
    db.add(new_pick)
    db.commit()
    return {"message": f"Pick for {pick_data.team} recorded"}
