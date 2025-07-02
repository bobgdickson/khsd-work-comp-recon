"""WorkCompRecord model stub. Add actual fields as needed."""
from sqlalchemy import Column, Integer, String

from app.db.base import Base

class WorkCompRecord(Base):
    __tablename__ = "work_comp_records"

    id = Column(Integer, primary_key=True, index=True)
    field1 = Column(String, nullable=True)
    field2 = Column(String, nullable=True)