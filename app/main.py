from fastapi import FastAPI
from app.routers import router
from app.auth.router import router as auth_router
app = FastAPI(
    title="BasicApp",
    description="Right now it is BasicApp",
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)

app.include_router(router)
app.include_router(auth_router)