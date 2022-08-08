"""SQLAlchemy parts of the application.

This module creates the SQLAlchemy parts used all around the application
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config.database import sql_db_url

engine = create_engine(
        sql_db_url,
)

SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
)

Base = declarative_base()


def get_db():
    """Database dependency to inject into paths operations
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
