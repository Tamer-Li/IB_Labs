import bcrypt

from app.auth.dao import UsersDao


def get_hashed_password(password: str) -> str:
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes, salt)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    bytes = plain_password.encode('utf-8')
    return bcrypt.checkpw(bytes, hashed_password)


def authenticate_user(login: str, password: str):
    user = UsersDao.find_one_or_none(login=login)
    if not user and not verify_password(password, user.hashed_password):
        return None
    return user


def registry_user(
    login: str,
    first_name: str,
    password: str,
    email: str,
    address_id: str
):
    if UsersDao.find_one_or_none(
        login,
        first_name,
        email
    ) is None:
        hashed_password = get_hashed_password(password=password)
        result = UsersDao.add(
            login=login,
            hashed_password=hashed_password,
            first_name=first_name,
            email=email,
            address_id=address_id
        )
        return result
    return False
