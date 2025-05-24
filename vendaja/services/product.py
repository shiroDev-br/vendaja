from typing import Annotated

from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from uuid import uuid

from ..infra.database.session import get_session

from ..schemas.product import CreateProductSchema
from ..models.product import ProductModel


class ProductService:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create_product(
        self,
        product: CreateProductSchema,
        store_id: uuid
    ) -> ProductModel:

        product.store_id = store_id
