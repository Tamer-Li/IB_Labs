import sqlite3
import os


DB_FILE = "./new.db"
PULL_FILE = "./pull.sql"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, DB_FILE)
PULL_PATH = os.path.join(BASE_DIR, PULL_FILE)


def pull() -> bool:
    if not os.path.exists(PULL_PATH):
        return False

    sql_script = ""

    with open(PULL_PATH, 'r', encoding='utf-8') as file:
        sql_script = file.read()

    sql_commands = sql_script.split(';')

    if os.path.exists(DB_PATH):
        return False

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for command in sql_commands:
        if command.strip():
            cursor.execute(command)

    conn.commit()
    conn.close()

    return True
