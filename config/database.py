'''Database config package'''
import os
from typing import Any
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


load_dotenv()


db: dict[str, Any] = dict(
    name=os.getenv('NAME_DB')
)


def build_db_url(params: dict[str, Any]) -> str:
    '''build db url'''
    return f'sqlite:///./{params["name"]}.db'


db['url'] = build_db_url(db)

engine = create_engine(db['url'], pool_size=5, echo=False, pool_pre_ping=True)
Session = sessionmaker(bind=engine, autocommit=False)


def get_session():
    '''Função para geração da session.'''
    session = Session()
    try:
        yield session
    except Exception:
        session.rollback()
    else:
        session.commit()
    finally:
        session.close()
