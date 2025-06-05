from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.fixtures import router as fixtures_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(fixtures_router)
