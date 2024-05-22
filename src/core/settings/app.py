from typing import Any, Dict

from src.core.settings.base import BaseAppSettings


class AppSettings(BaseAppSettings):
    data_io_schema: str = "http"
    data_io_host: str = "localhost"
    data_io_port: int = 3001


    class Config:
        validate_assignment = True

