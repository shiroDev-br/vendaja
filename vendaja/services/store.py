from typing import Annotated

from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ..infra.database.session import get_session

from ..schemas.store import CreateStoreSchema
from ..models.store import StoreModel

from ..utils.security.data_processing import encrypt_fields
from ..utils.security.hasher import hash_password
from .exceptions import StoreAlreadyRegistered



class StoreService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.sensive_fields = ['document']

    async def create_store(self, store: CreateStoreSchema):
        encrypt_fields(store, self.sensive_fields)
        store.password = str(hash_password(store.password))

        conditions = (
            (StoreModel.email == store.email) |
            (StoreModel.phone == store.phone) |
            (StoreModel.document == store.document) 
        )

        existing_store = await self.session.scalar(select(StoreModel).where(conditions))
        if existing_store:
            raise StoreAlreadyRegistered('Store already exists')

        new_store = StoreModel(
            **store.model_dump()
        )
        self.session.add(new_store)
        await self.session.commit()
        await self.session.refresh(new_store)

        return new_store

def get_store_service(
    session: Annotated[AsyncSession, Depends(get_session)]
):
    return StoreService(session)
    
