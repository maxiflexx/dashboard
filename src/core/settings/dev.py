import os

from src.core.services.file import get_root
from src.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    class Config(AppSettings.Config):
        env_file=os.path.join(get_root(), '.env')
