"""Database operations."""
from sqlalchemy.orm import Session
from typing import List

from app.schemas import WorkCompSiscCreate
from app.models import WorkCompSisc

def insert_records(db: Session, records: List[WorkCompSiscCreate]) -> None:
    """Insert WorkCompSisc entries into the database."""
    db_records = [WorkCompSisc(**record.dict()) for record in records]
    db.add_all(db_records)
    db.commit()
