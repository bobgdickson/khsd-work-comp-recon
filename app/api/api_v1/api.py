"""API router."""
from fastapi import APIRouter

from app.api.api_v1.routers import excel

api_router = APIRouter()
api_router.include_router(excel.router, prefix="/excel", tags=["excel"])