
from fastapi import FastAPI
from app.routes.fixtures import router as fixtures_router

app = FastAPI()

app.include_router(fixtures_router)
