from typing import Annotated

from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

import jwt
import datetime

from ...settings.settings import Settings
from ...services.store import (
    StoreService,
    get_store_service
)


settings = Settings()

SECRET_KEY = settings.SECRET_KEY

security = HTTPBearer()

def create_access_token(sub: dict):
    to_encode = sub.copy()
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    to_encode.update({'exp': expiration_time})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=settings.ALGORITHM)

    return token

async def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
    store_service: Annotated[StoreService, Depends(get_store_service)],
):
    token = credentials.credentials

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    try:
        payload: dict = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )

        store_name = payload.get("sub")
        if store_name is None:
            raise credentials_exception

    except jwt.DecodeError:
        raise credentials_exception
    except jwt.InvalidTokenError:
        raise credentials_exception
        
    store = await store_service.get_store_by_name(store_name)
    if store is None:
        raise credentials_exception
    
    return store

        
