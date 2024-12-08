import json
import os

from app.config.settings import settings


class ConfigApp:

    def __init__(self, config_path: str, id_device: str, lic_num: str):
        self._config_file = config_path
        self._id_device = id_device
        self._license_number = lic_num

    def create_config(self):
        if not os.path.exists(self._config_file):
            default_config = {
                'i': 0,
                'id_device': self.settings.get_device_id(),
                'license_number': self.settings.get_password()
            }
            with open(self._config_file, 'w') as c:
                json.dump(default_config, c)

    def load_config(self):
        with open(self._config_file, 'r') as f:
            return json.load(f)

    def save_config(self, config: str):
        with open(self._config_file, 'w') as f:
            json.dump(config, f)

    def check_license_and_device_id(self, id_device_local: str) -> bool:
        config_values = self.load_config()
        id_device = config_values["id_device"]

        config_values["i"] += 1
        self.save_config(config_values)

        if id_device != id_device_local:
            return False

        return True


config = ConfigApp(
    settings.get_config_path,
    settings.get_device_id,
    settings.get_password
)
