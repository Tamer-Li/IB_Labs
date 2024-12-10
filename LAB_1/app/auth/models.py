from sqlalchemy import Column, Integer, String, ForeignKey

from app.db.db import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    login = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    address_id = Column(String, ForeignKey('id_pc.id'), nullable=False)


class UsersInfo(Base):
    __tablename__ = 'users_info'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    second_name = Column(String)
    middle_name = Column(String)
    phone = Column(String)
