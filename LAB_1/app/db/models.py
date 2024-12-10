from sqlalchemy import Column, Integer, String

from app.db.db import Base


class IdPc(Base):
    __tablename__ = 'id_pc'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    address = Column(String, nullable=False)
