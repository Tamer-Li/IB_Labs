import uuid
import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_FILE = os.path.join(BASE_DIR, '../../.env')


class Settings:

    def __init__(self, settings_file: str):
        self._settings_file = settings_file

    def load_settings(self):
        if not os.path.exists(self._settings_file):
            raise FileNotFoundError("Not found ENV file")

        load_dotenv(self._settings_file)

        self._app_path = os.getenv("APP_PATH", "./app")
        self._password = os.getenv("PASSWORD", "123456")
        self._config_path = os.path.join(
            BASE_DIR, os.getenv("CONFIG_PATH", "../config.json")
        )

    def get_device_id(self) -> str:
        self._id_device = str(uuid.uuid1())
        return self._id_device

    def get_config_path(self) -> str:
        return self._config_path

    def get_app_path(self) -> str:
        return self._app_path

    def get_password(self) -> str:
        return self._password


settings = Settings(ENV_FILE)
settings.load_settings()
