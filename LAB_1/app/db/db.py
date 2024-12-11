from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine('sqlite:///new.db', echo=True)
session = sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


Base.metadata.create_all(bind=engine)


def execute_sql_script(sql_script_path: str) -> bool:
    sql_script = ""

    with open(sql_script_path, 'r', encoding='utf-8') as file:
        sql_script = file.read()

    sql_commands = sql_script.split(';')

    for command in sql_commands:
        if command.strip():
            session.execute(command)

    session.commit()
