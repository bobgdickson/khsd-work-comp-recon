"""Database operations."""
from sqlalchemy.orm import Session
from typing import List

from app.schemas.work_comp_record import WorkCompRecordCreate
from app.models.work_comp_record import WorkCompRecord

def insert_records(db: Session, records: List[WorkCompRecordCreate]) -> None:
    """Insert WorkCompRecord entries into the database."""
    raise NotImplementedError