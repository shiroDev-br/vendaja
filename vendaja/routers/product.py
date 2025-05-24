from typing import Annotated

from fastapi import APIRouter, Depends, status

from ..models.store import StoreModel
from ..services.product import (
    ProductService,
    get_product_service
)
from ..schemas.product import CreateProductSchema

from ..utils.security.token_manager import get_current_user

product_router = APIRouter(
    prefix='/product'
)

@product_router(
    '/register',
    status_code=status.HTTP_201_CREATED
)
async def register(
    product: CreateProductSchema,
    product_service: Annotated[ProductService, Depends(get_product_service)],
    current_user: Annotated[StoreModel, Depends(get_current_user)]
):
    new_product = product_service.create_product(product, current_user.id)

    return new_product

