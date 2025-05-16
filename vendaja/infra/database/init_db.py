from .infra.database.base import Base
from .infra.database.database import engine
import asyncio


async def init_models():
    async with engine.begin() as conn:
        from ...models.store import StoreModel
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(init_models())
