from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ..schemas.store import CreateStoreSchema
from ..models.store import StoreModel

from ..utils.security.data_processing import encrypt_fields
from .exceptions import StoreAlreadyRegistered



class StoreService:
    def __init__(self, session: AsyncSession):
        self.__session = session
        self.__sensive_fields = ['document', 'picpay_client_id', 'picpay_client_secret', 'whatsapp_token']

    async def create_store(self, store: CreateStoreSchema):
        encrypt_fields(store, self.__sensive_fields)
        conditions = (
            (StoreModel.email == store.email) |
            (StoreModel.phone == store.phone) |
            (StoreModel.document == store.document) |
            (StoreModel.pipcay_client_id == store.pipcay_client_id) |
            (StoreModel.picpay_client_secret == store.picpay_client_secret) |
            (StoreModel.whatsapp_token == store.whatsapp_token)
        )

        existing_store = await self.__session.scalar(select(StoreModel).where(conditions))
        if existing_store:
            raise StoreAlreadyRegistered('Store already exists')

        new_store = StoreModel(
            **store.model_dump()
        )
        self.__session.add(new_store)
        await self.__session.commit()
        await self._session.refresh(new_store)

        return new_store