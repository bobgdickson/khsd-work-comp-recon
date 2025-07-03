from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    """Dependency to get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


ps_engine = create_engine(settings.PS_DB_URL) if settings.PS_DB_URL != "none" else None
PS_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ps_engine) if ps_engine else None