"""Excel parsing utilities."""
from fastapi import UploadFile
import pandas as pd
from io import BytesIO

VALID_COLUMNS = [
    'From',
    'Through',
    'Check#',
    'Check Date',
    'Payee',
    'Amount',
    'Employee',
    'Claim Number',
    'SSN'
]

async def parse_excel(file: UploadFile) -> list[dict]:
    """Parse the uploaded Excel file and return rows where payee is 'Kern High'."""

    # Read Excel bytes
    contents = await file.read()

    # Skip first two rows to get real headers
    df = pd.read_excel(BytesIO(contents), header=3)
    df = df[VALID_COLUMNS]
    df.rename(columns={
        'From': 'from_date',
        'Through': 'through_date',
        'Check#': 'check_number',
        'Check Date': 'check_date',
        'Payee': 'payee',
        'Amount': 'amount',
        'Employee': 'employee',
        'Claim Number': 'claim_number',
        'SSN': 'ssn'
    }, inplace=True)
    # Inspect columns
    print(df.columns)

    # Filter by payee
    filtered_df = df[df['payee'].str.contains("Kern High", case=False, na=False)]

    # Dates — safe conversion
    for col in ['from_date', 'through_date', 'check_date']:
        df[col] = (
            pd.to_datetime(df[col], errors='coerce')
            .dt.strftime('%Y-%m-%d')
            .astype(str)
        )


    for col in ['check_number', 'claim_number', 'ssn']:
        df[col] = df[col].astype(str)

    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

    for col in ['employee', 'payee']:
        df[col] = df[col].astype(str)

    # Convert to list of dicts
    records = filtered_df.to_dict(orient='records')

    return records
