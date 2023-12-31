import os
import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import (AnyHttpUrl, BaseSettings, EmailStr, Field, HttpUrl,
                      PostgresDsn, validator)


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    PROJECT_NAME: str
    TAG: str = "DEV"

    class Config:
        case_sensitive = True


        # env_file = os.path.expanduser('.env')
settings = Settings()
