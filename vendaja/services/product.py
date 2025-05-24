from typing import Annotated

from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ..infra.database.session import get_session

from ..schemas.product import CreateProductSchema
from ..models.product import ProductModel

from .exceptions import ProductAlreadyExists

class ProductService:
    def __init__(self, session: AsyncSession):
        self.session = session
        