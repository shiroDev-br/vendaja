from typing import Annotated

from fastapi import (
    APIRouter, 
    Depends, 
    HTTPException, 
    status
)

from ..services.store import (
    StoreService,
    get_store_service
)

from ..schemas.token import TokenSchema
from ..schemas.auth import LoginSchema

from ..utils.security.hasher import check_password
from ..utils.security.token_manager import create_access_token

auth_router = APIRouter(prefix='/auth')

@auth_router.post(
    '/login',
    status_code=status.HTTP_200_OK,
    response_model=TokenSchema,
     responses={
        status.HTTP_401_UNAUTHORIZED: {
            'description': 'Incorrect name or password',
            'content': {
                'application/json': {
                    'example': {'detail': 'Incorrect username or password'}
                }
            },
        },
    },
)
async def login(
    login_data: LoginSchema,
    store_service: Annotated[StoreService, Depends(get_store_service)]
):
    store = await store_service.get_store_by_name(login_data.name)
    if not store or not check_password(login_data.password, store.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect name or password',
        )

    access_token = create_access_token({
        'name': store.name
    })

    return {"access_token": access_token, "token_type": 'Bearer'}