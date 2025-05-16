from .database import engine
from ..database.base import Base
import asyncio


async def init_models():
    async with engine.begin() as conn:
        from ...models.store import StoreModel
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(init_models())
