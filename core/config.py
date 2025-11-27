from typing import List
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DEBUG: bool = False
    PROJECT_NAME: str = "Coin Collection Manager"
    API_V1_STR: str = "/api"

    DATABASE_URL: str

    # JWT
    JWT_SECRET_KEY: str = "change_me_in_env"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 dia

    # CORS
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    # Config do Pydantic v2
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=True,
    )


settings = Settings()
