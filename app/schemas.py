"""WorkCompSisc schema."""
from pydantic import BaseModel
from typing import Optional, Union
from datetime import datetime

class WorkCompSiscBase(BaseModel):
    from_date: Optional[datetime]
    through_date: Optional[datetime]
    check_number: Union[int, str]
    check_date: Optional[datetime]
    payee: str
    amount: float
    employee: str
    claim_number: Union[int, str]
    ssn: Union[int, str]
    emplid: Optional[str] = None

class WorkCompSiscCreate(WorkCompSiscBase):
    pass

class WorkCompSisc(WorkCompSiscBase):
    id: int

    class Config:
        orm_mode = True