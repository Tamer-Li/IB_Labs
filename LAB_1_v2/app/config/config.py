import json
import os
import uuid

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = "../../config.json"
CONFIG_PATH = os.path.join(BASE_DIR, CONFIG_FILE)


def load_config():
    if not os.path.exists(CONFIG_PATH):
        return None

    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)


def save_config(config: dict) -> bool:
    if not os.path.exists(CONFIG_PATH):
        return False

    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f)

    return True


def get_uuid_device() -> str:
    mac_address = str(uuid.getnode())
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, mac_address))


def check_license_and_device_id(local: str) -> bool:
    config_values = load_config()
    if config_values is None:
        return None

    id_device = config_values["id_device"]

    config_values["i"] += 1
    save_config(config_values)

    if id_device != local:
        print("id_device: ", id_device)
        print("local: ", local)
        return False

    return True
