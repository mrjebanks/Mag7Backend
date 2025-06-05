from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db.database import SessionLocal
from ..models import models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_leaderboard(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    results = []
    for user in users:
        status = "active" if any(p.status == "pending" for p in user.picks) else "eliminated"
        results.append({
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "status": status
        })
    return results
