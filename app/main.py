from fastapi import FastAPI
from app.routers import router
from app.user.router import router as user_router
from app.teams_show.router import router as team_router
from app.tracks_show.router import router as track_router



app = FastAPI(
    title="BasicApp",
    description="Right now it is BasicApp",
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)

# app.include_router(router)
app.include_router(user_router)
app.include_router(team_router)
app.include_router(track_router)
