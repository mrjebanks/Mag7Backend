from fastapi import APIRouter, HTTPException
import requests
import os

fixtures_router = APIRouter()
API_KEY = os.getenv("FOOTBALL_DATA_API_KEY")
BASE_URL = "https://api.football-data.org/v4/competitions/PL/matches"

@fixtures_router.get("/")
def get_fixtures():
    headers = {"X-Auth-Token": API_KEY}
    try:
        response = requests.get(BASE_URL, headers=headers, params={"status": "SCHEDULED"})
        response.raise_for_status()
        data = response.json()
        fixtures = [{"home": m["homeTeam"]["name"], "away": m["awayTeam"]["name"], "date": m["utcDate"]} for m in data["matches"]]
        return {"fixtures": fixtures}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
