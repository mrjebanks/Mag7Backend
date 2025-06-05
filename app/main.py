
from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.fixtures import router as fixtures_router
from app.routes.picks import router as picks_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]  # Adjust as needed

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(fixtures_router)
app.include_router(picks_router)
