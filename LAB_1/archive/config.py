import os
from dotenv import set_key

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_FILE = os.path.join(BASE_DIR, "../.env")


def create_env(data: dict):
    with open(ENV_FILE, 'w') as f:
        for k, v in data.items():
            set_key(f, k, v)
