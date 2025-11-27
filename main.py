from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from core.config import settings
from core.db import Base
from core.session import engine
from routers import auth, coins, dashboard

# Cria as tabelas (ou use Alembic em prod)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(o) for o in settings.BACKEND_CORS_ORIGINS] or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files para imagens
app.mount("/media", StaticFiles(directory="media"), name="media")

# Routers
app.include_router(auth.router, prefix=settings.API_V1_STR)
app.include_router(coins.router, prefix=settings.API_V1_STR)
app.include_router(dashboard.router, prefix=settings.API_V1_STR)


@app.get("/")
def healthcheck():
    return {"status": "ok", "app": settings.PROJECT_NAME}
