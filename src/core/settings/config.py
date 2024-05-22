import os
from typing import Dict, Type

from src.core.settings.app import AppSettings
from src.core.settings.base import AppEnvTypes
from src.core.settings.dev import DevAppSettings

environments: Dict[AppEnvTypes, Type[AppSettings]] = {
    AppEnvTypes.dev: DevAppSettings,
}


def get_app_settings() -> AppSettings:
	app_env = os.getenv("APP_ENV")

	if not app_env:
		app_env = 'dev'

	if app_env not in AppEnvTypes.to_list():
		raise Exception("This is an invalid app env.")

	config = environments[AppEnvTypes[app_env]]
	return config()


settings = get_app_settings()
