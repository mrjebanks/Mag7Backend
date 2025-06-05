# app/routes/fixtures.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_fixtures():
    return {
        "week": 1,
        "fixtures": [
            {"home": "Arsenal", "away": "Chelsea"},
            {"home": "Liverpool", "away": "Man City"},
            {"home": "Tottenham", "away": "Brighton"},
        ]
    }
