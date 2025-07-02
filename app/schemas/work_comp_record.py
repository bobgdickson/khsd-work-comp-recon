"""WorkCompRecord schema stub. Add actual fields as needed."""
from pydantic import BaseModel

class WorkCompRecordBase(BaseModel):
    field1: str
    field2: str

class WorkCompRecordCreate(WorkCompRecordBase):
    pass

class WorkCompRecord(WorkCompRecordBase):
    id: int

    class Config:
        orm_mode = True