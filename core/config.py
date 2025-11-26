from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn
    DEBUG: bool = False
    SECRET_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
