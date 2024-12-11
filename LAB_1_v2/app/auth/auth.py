import hashlib
import os
import sqlite3


def hash_password(password: str) -> str:
    salt = os.urandom(16)

    hashed_password = hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=salt,
        iterations=100000
    )

    return salt.hex() + hashed_password.hex()


def verify_password(password: str, hashed_password: str) -> bool:
    salt = bytes.fromhex(hashed_password[:32])
    stored_hash = bytes.fromhex(hashed_password[32:])

    new_hash = hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=salt,
        iterations=100000
    )

    return new_hash == stored_hash


def auth_user(login: str, password: str, DB_PATH) -> bool:

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT hashed_password FROM users WHERE login = ?",
        (login,)
    )
    result = cursor.fetchone()

    conn.close()

    if verify_password(password, result[0]):
        return True
    else:
        return False


def register(
        first_name: str,
        second_name: str,
        middle_name: str,
        login: str,
        email: str,
        phone: str,
        password: str,
        address: str,
        DB_PATH
) -> bool:
    hashed_password = hash_password(password)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT * FROM users WHERE login = ? OR email = ?",
            (login, email)
        )
        if cursor.fetchone():
            print("Пользователь с таким логином или email уже существует.")
            return False

        cursor.execute("""
            INSERT INTO users (
                       first_name,
                       second_name,
                       middle_name,
                       login,
                       email,
                       phone,
                       hashed_password,
                       address_registry
                    )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            first_name,
            second_name,
            middle_name,
            login, email,
            phone,
            hashed_password,
            address
        ))

        conn.commit()
        print("Пользователь успешно зарегистрирован.")

        return True

    except sqlite3.Error as e:
        print(f"Ошибка при регистрации пользователя: {e}")
    finally:
        conn.close()
