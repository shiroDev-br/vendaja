from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from ..models.store import StoreModel
from ..services.store import (
    StoreService,
    get_store_service
)
from ..services.exceptions import StoreAlreadyRegistered
from ..schemas.store import CreateStoreSchema

from ..utils.security.token_manager import get_current_user

store_router = APIRouter(
    prefix='/store'
)

@store_router.post(
    '/register',
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            'description': 'Store already exists.',
            'content': {
                'application/json': {
                    'example': {'detail': 'Store already exists'}
                }
            },
        }
    }
)
async def register(
    store: CreateStoreSchema,
    store_service: Annotated[StoreService, Depends(get_store_service)]
):
    try:
        store = await store_service.create_store(store)
    except StoreAlreadyRegistered:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Store already exists',
        )
    
    return store

@store_router.get(
    '/test'
)
async def test(
    current_user: Annotated[StoreModel, Depends(get_current_user)]
):
    return current_user