from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth import auth_router
from picks import picks_router
from fixtures import fixtures_router

app = FastAPI(title="Mag7 Last Man Standing API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(picks_router, prefix="/picks", tags=["picks"])
app.include_router(fixtures_router, prefix="/fixtures", tags=["fixtures"])
