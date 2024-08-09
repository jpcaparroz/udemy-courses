from fastapi import APIRouter

from api.v1.endpoints import product


router = APIRouter()
router.include_router(product.router, prefix='/product', tags=['Product'])