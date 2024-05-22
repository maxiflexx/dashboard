from enum import Enum

from pydantic_settings import BaseSettings


class AppEnvTypes(Enum):
    dev = "dev"

    @classmethod
    def to_list(cls):
        return [c.value for c in cls]


class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = AppEnvTypes.dev

    class Config:
        env_file = ".env"
