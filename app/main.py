from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.auth import router as auth_router
from .routes.fixtures import router as fixtures_router
from .routes.picks import router as picks_router
from .routes.admin import router as admin_router
from .routes.leaderboard import router as leaderboard_router

from app.db.init_db import init_db
init_db()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth")
app.include_router(fixtures_router, prefix="/fixtures")
app.include_router(picks_router, prefix="/picks")
app.include_router(admin_router, prefix="/admin")
app.include_router(leaderboard_router, prefix="/leaderboard")
