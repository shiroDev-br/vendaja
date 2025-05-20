from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from http import HTTPStatus

from ..schemas.store import CreateStoreSchema
from ..models.store import StoreModel

from ..utils.security.data_processing import encrypt_fields

sensive_fields = ['document', 'picpay_client_id', 'picpay_client_secret', 'whatsapp_token']

async def create_store(store: CreateStoreSchema, session: AsyncSession):
    encrypt_fields(store, sensive_fields)
    conditions = (
        (StoreModel.email == store.email) |
        (StoreModel.phone == store.phone) |
        (StoreModel.document == store.document) |
        (StoreModel.pipcay_client_id == store.pipcay_client_id) |
        (StoreModel.picpay_client_secret == store.picpay_client_secret) |
        (StoreModel.whatsapp_token == store.whatsapp_token)
    
    )
    db_store = await session.scalar(select(StoreModel).where(conditions))
    if db_store:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='Alguma informação já consta no sistema.'
        )
    try:
        db_store = StoreModel(
            **store.model_dump()
        )
        await session.add(db_store)
        await session.commit()
        await session.refresh(db_store)
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail=f'{e}'
        )

