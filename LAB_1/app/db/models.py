from sqlalchemy import Column, Integer, String

from app.db.db import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String(127))
    second_name = Column(String(127))
    middle_name = Column(String(127))
    phone = Column(String(20))
    email = Column(String(50))
    address = Column(String, nullable=False)
