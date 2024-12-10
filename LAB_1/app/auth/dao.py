from sqlalchemy import insert

from app.db.dao import BaseDAO
from app.db.db import session
from app.auth.models import Users, UsersInfo


class UsersDao(BaseDAO):
    model = Users

    @classmethod
    def add(
        cls,
        login: str,
        hashed_password: str,
        first_name: str,
        email: str,
        address_id: int
    ):
        with session() as s:
            query = insert(cls.model).values(
                login, hashed_password, first_name, email, address_id
            )
            s.execute(query)
            return s.commit


class UsersInfoDao(BaseDAO):
    model = UsersInfo

    @classmethod
    def add(
        cls,
        user_id: int,
        second_name: str,
        middle_name: str,
        phone: str
    ):
        with session() as s:
            query = insert(cls.model)
            s.execute(query)
            return s.commit()
