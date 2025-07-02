# khsd-work-comp-recon

This is a FastAPI project scaffold for `khsd-work-comp-recon`.

## Features

- FastAPI application structure
- Excel file upload endpoint stub
- SQLAlchemy models and session management
- Alembic migrations for database schema management

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure the database URL (defaults to SQLite at `./sql_app.db`):
   ```bash
   export DATABASE_URL="sqlite:///./sql_app.db"
   ```
3. Apply migrations:
   ```bash
   alembic upgrade head
   ```
4. Start the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints

### Upload Excel File

`POST /api/v1/excel/upload-excel`

Form data:
- `file`: Excel file to upload

Response:

- `200 OK` on success
- `501 Not Implemented` for stub functions

## Project Structure

```
. \
├── README.md
├── requirements.txt
├── alembic.ini
├── alembic/
│   ├── env.py
│   └── versions/
│       └── 0001_create_work_comp_records_table.py
└── app/
    ├── main.py
    ├── core/
    ├── db/
    ├── models/
    ├── schemas/
    ├── services/
    └── api/
```