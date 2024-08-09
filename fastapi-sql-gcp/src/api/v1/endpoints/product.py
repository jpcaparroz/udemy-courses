from uuid import UUID

from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends
from fastapi import status

from sqlalchemy.ext.asyncio import AsyncSession

from models.product_model import ProductModel
from schemas.product_schema import BaseProductSchema
from schemas.product_schema import GetProductSchema
from schemas.generic_schema import HttpDetail
from core.deps import get_session
from api.v1.data.crud import product_crud as crud
from api.v1.data.template.product_template import CreateProductBody


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=GetProductSchema)
async def create_product(product: BaseProductSchema = CreateProductBody, 
                         db: AsyncSession = Depends(get_session)):
    new_product: ProductModel = ProductModel(**product.model_dump())
    try:
        response = await crud.create_product_query(new_product, db)
        return response
    
    except Exception as e:
        raise HTTPException(status.HTTP_409_CONFLICT, str(e))


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[GetProductSchema])
async def get_products(db: AsyncSession = Depends(get_session)):
    return await crud.get_products_query(db)


@router.delete("/{product_id}", status_code=status.HTTP_200_OK, response_model=HttpDetail)
async def delete_user(product_id: UUID, db: AsyncSession = Depends(get_session)):
    check_user = await crud.get_product_query(product_id, db)
    if not check_user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'Product not found')
    
    await crud.delete_product_query(product_id, db)
    
    return HttpDetail(detail= 'Product deleted successfully')