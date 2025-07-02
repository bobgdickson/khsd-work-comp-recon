from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session

from app.services.excel import parse_excel
from app.services.db import insert_records
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload-excel")
async def upload_excel(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """Endpoint to upload an Excel file and process its records."""
    try:
        records = await parse_excel(file)
        insert_records(db, records)
    except NotImplementedError:
        raise HTTPException(status_code=501, detail="Not implemented")
    return {"status": "success", "records_processed": len(records)}