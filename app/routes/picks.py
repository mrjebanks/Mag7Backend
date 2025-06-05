from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.database import SessionLocal
from ..models import models
from ..schemas import schemas
from jose import jwt
import os

router = APIRouter()
SECRET_KEY = os.getenv("SECRET_KEY", "secret")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str, db: Session):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get("sub"))
    except:
        raise HTTPException(status_code=403, detail="Invalid token")
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=schemas.PickOut)
def create_pick(pick: schemas.PickCreate, token: str, db: Session = Depends(get_db)):
    user = get_current_user(token, db)
    existing = db.query(models.Pick).filter(models.Pick.user_id == user.id, models.Pick.week == pick.week).first()
    if existing:
        raise HTTPException(status_code=400, detail="Already picked this week")
    new_pick = models.Pick(user_id=user.id, team=pick.team, week=pick.week)
    db.add(new_pick)
    db.commit()
    db.refresh(new_pick)
    return new_pick

@router.get("/me", response_model=list[schemas.PickOut])
def get_my_picks(token: str, db: Session = Depends(get_db)):
    user = get_current_user(token, db)
    return db.query(models.Pick).filter(models.Pick.user_id == user.id).all()
