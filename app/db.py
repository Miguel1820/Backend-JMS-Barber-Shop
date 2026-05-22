from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager

SQLALCHEMY_DATABASE_URL = "sqlite:///./barber_shop.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models
declarative_base = declarative_base()
Base = declarative_base

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Dependency for FastAPI routes
@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()