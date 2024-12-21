import os
import json

CONFIG_FILE = "../../config.json"


class Config:

    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_path = os.path.join(self.base_dir, CONFIG_FILE)

    def load(self):
        if not os.path.exists(self.config_path):
            return None

        with open(self.config_path, 'r') as f:
            return json.load(f)

    def save(self, conf: dict) -> bool:
        if not os.path.exists(self.config_path):
            return False

        with open(self.config_path, 'w') as f:
            json.dump(conf, f)

        return True
