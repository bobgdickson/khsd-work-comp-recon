"""Excel parsing utilities."""
from fastapi import UploadFile

async def parse_excel(file: UploadFile) -> list[dict]:
    """Parse the uploaded Excel file and return a list of record dictionaries."""
    raise NotImplementedError