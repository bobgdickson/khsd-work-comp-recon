from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session

from app.services.excel import parse_excel
from app.services.db import insert_records
from app.db import get_db
from app.schemas import WorkCompSiscCreate

router = APIRouter()

@router.post("/upload-excel")
async def upload_excel(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """Endpoint to upload an Excel file and process its records."""
    try:
        raw_records  = await parse_excel(file)
        # Validate with Pydantic
        records = [WorkCompSiscCreate(**r) for r in raw_records]
        insert_records(db, records)
    except NotImplementedError:
        raise HTTPException(status_code=501, detail="Not implemented")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
    return {"status": "success", "records_processed": len(records)}