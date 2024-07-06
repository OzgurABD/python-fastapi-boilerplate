"""Database module."""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.config import settings

Base = declarative_base()

_engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI)) #fmt:off
_session = sessionmaker(autocommit=False, autoflush=False, bind=_engine)


def createDatabase() -> None:
    Base.metadata.create_all(_engine)


def dbSession():
    db = _session()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()