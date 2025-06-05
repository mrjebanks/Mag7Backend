from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db.database import SessionLocal
from ..models import models
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

@router.get("/overview")
def get_overview(token: str, db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get("sub"))
    except:
        return {"error": "invalid token"}
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user or not user.is_admin:
        return {"error": "unauthorized"}
    return {
        "leagues": ["Premier League"],  # placeholder
        "users": db.query(models.User).all(),
        "picks": db.query(models.Pick).all()
    }
