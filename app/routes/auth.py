
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.models import User
from app.db.database import SessionLocal
from passlib.context import CryptContext

router = APIRouter(prefix="/auth")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserCreate(BaseModel):
    email: str
    password: str

@router.post("/register")
def register(user: UserCreate):
    db: Session = SessionLocal()
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    new_user = User(email=user.email, hashed_password=pwd_context.hash(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully"}

@router.post("/login")
def login(user: UserCreate):
    db: Session = SessionLocal()
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"access_token": "fake-token-for-demo"}
