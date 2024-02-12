from fastapi import APIRouter
from app.api.v1.endpoints import bank_router

main_router = APIRouter()
main_router.include_router(
    bank_router,
    prefix='/bank',
    tags=['Bank']
)
