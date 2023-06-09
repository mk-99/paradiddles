from pathlib import Path
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    bot_token: str = Field(..., env="BOT_TOKEN")

    class Config:
        env_file = f"{Path(__file__).resolve().parent}/.env"


settings = Settings()
