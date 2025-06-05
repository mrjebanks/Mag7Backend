from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.db.database import SessionLocal, engine, Base
from sqlalchemy.orm import Session
from app.models.user import User
from passlib.context import CryptContext

router = APIRouter(prefix="/auth")

Base.metadata.create_all(bind=engine)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class RegisterInput(BaseModel):
    email: str
    password: str
    first_name: str
    surname: str

class LoginInput(BaseModel):
    email: str
    password: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(data: RegisterInput, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = pwd_context.hash(data.password)
    user = User(email=data.email, password=hashed_password, first_name=data.first_name, surname=data.surname)
    db.add(user)
    db.commit()
    return {"message": "User created successfully"}

@router.post("/login")
def login(data: LoginInput, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not pwd_context.verify(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "first_name": user.first_name}
