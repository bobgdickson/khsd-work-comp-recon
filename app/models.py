"""WorkCompSisc model — all fields."""
from sqlalchemy import Column, Integer, String, Float, Date
from app.db import Base

class WorkCompSisc(Base):
    __tablename__ = "work_comp_sisc"

    id = Column(Integer, primary_key=True, index=True)
    from_date = Column("FROM_DATE", String, nullable=True)
    through_date = Column("THROUGH_DATE", String, nullable=True)
    check_number = Column("CHECK_NUMBER", String, nullable=True)
    check_date = Column("CHECK_DATE", String, nullable=True)
    payee = Column("PAYEE", String, nullable=True)
    amount = Column("AMOUNT", Float, nullable=True)
    employee = Column("EMPLOYEE", String, nullable=True)
    claim_number = Column("CLAIM_NUMBER", String, nullable=True)
    ssn = Column("SSN", String, nullable=True)
    emplid = Column("EMPLID", String, nullable=True)