from uuid import UUID

from typing import List

from sqlalchemy import select
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from models.product_model import ProductModel


async def create_product_query(product: ProductModel, db: AsyncSession):
    async with db as session:
        session.add(product)
        await session.commit()
    
    return product


async def get_products_query(db: AsyncSession):
    async with db as session:
        query = select(ProductModel)
        result = await session.execute(query)
        products: List[ProductModel] = result.scalars().unique().all()
        
    return products


async def get_product_query(product_id: UUID, db: AsyncSession):
    async with db as session:
        query = select(ProductModel).filter(ProductModel.product_id == product_id)
        result = await session.execute(query)
        product: ProductModel = result.scalars().unique().one_or_none()
        
    return product


async def delete_product_query(product_id: UUID, db: AsyncSession):
    async with db as session:
        query = delete(ProductModel).where(ProductModel.product_id == product_id)
        await session.execute(query)
        await session.commit()
