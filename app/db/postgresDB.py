from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import SQLALCHEMY_DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    future=True,
    pool_size=50,  # query size (count maximum)
    max_overflow=10,
    pool_recycle=1800,
    connect_args={
        "keepalives":1,
        "keepalives_idle":60,  # 60 seconds
        "keepalives_interval":10,
        "keepalives_count":5
    }
)

# session Factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=True,
    bind=engine
)

# base class
Base = declarative_base()

def db_connection():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()