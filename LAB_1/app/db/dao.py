from sqlalchemy import select, insert

from app.db.db import session


class BaseDAO:
    model = None

    @classmethod
    def find_by_id(cls, model_id: int):
        with session() as s:
            query = select(cls).filter_by(id=model_id)
            result = s.execute(query)
            return result.scalar_one_or_none

    @classmethod
    def find_one_or_none(cls, **filter_by):
        with session() as s:
            query = select(cls).filter_by(**filter_by)
            result = s.execute(query)
            return result.scalar_one_or_none

    @classmethod
    def find_all(cls, **filter_by):
        with session() as s:
            query = select(cls).filter_by(**filter_by)
            result = s.execute(query)
            return result.scalars().all()

    @classmethod
    def add(cls, **data):
        with session() as s:
            query = insert(cls.model).values(**data)
            s.execute(query)
            return s.commit()
