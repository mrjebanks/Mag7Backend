from fastapi import APIRouter

router = APIRouter(prefix="/fixtures")

@router.get("/")
def get_fixtures():
    return [
        {"home": "Arsenal", "away": "Chelsea", "kickoff": "2025-08-17 14:00"},
        {"home": "Liverpool", "away": "Everton", "kickoff": "2025-08-18 16:30"},
    ]
