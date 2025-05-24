from typing import Annotated

from fastapi import Depends, status
from fastapi.exceptions import HTTPException

import jwt
import datetime

from ...settings.settings import Settings
from ...services.store import (
    StoreService,
    get_store_service
)


settings = Settings()

SECRET_KEY = settings.SECRET_KEY


def create_access_token(sub: dict):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    payload = {"sub": sub, "exp": expiration_time}
    token = jwt.encode(payload, SECRET_KEY, algorithm=settings.ALGORITHM)

    return token

async def get_current_user(
    store_service: Annotated[StoreService, Depends(get_store_service)],
    token: str
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    try:
        payload: dict = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        sub = payload.get("sub")
        if sub is None:
            raise credentials_exception

        store_name = sub.get("name")
        if store_name is None:
            raise credentials_exception
    except jwt.DecodeError:
        raise credentials_exception
    
    store = await store_service.get_store_by_name(store_name)
    if store is None:
        raise credentials_exception
    
    return store

        
