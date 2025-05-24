from typing import Annotated

from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from uuid import UUID

from ..infra.database.session import get_session

from ..schemas.product import CreateProductSchema
from ..models.product import ProductModel


class ProductService:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create_product(
        self,
        product: CreateProductSchema,
        store_id: UUID
    ) -> ProductModel:

        product.store_id = store_id

        new_product = ProductModel(
            **product.model_dump()
        )
        self.session.add(new_product)
        await self.session.commit()
        await self.session.refresh(new_product)

        return new_product


async def get_product_service(
    session: Annotated[AsyncSession, Depends(get_session)]
):
    return ProductService(session)