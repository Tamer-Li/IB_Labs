import json
import os

from app.config.settings import settings, Settings

CONFIG_FILE = settings.get_config_path


def create_config(s: Settings):
    if not os.path.exists(CONFIG_FILE):
        default_config = {
            'i': 0,
            'id_device': s.get_device_id(),
            'license_number': s.get_password()
        }
        with open(CONFIG_FILE, 'w') as c:
            json.dump(default_config, c)


create_config(settings)


def load_config(config_file: str):
    with open(config_file, 'r') as f:
        return json.load(f)


def save_config(config: str):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)
