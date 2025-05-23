from .database import engine
from ..database.base import Base
import asyncio


async def init_models():
    async with engine.begin() as conn:
        from ...models.store import StoreModel
        from ...models.sale import SaleModel
        from ...models.product import ProductModel
        from ...models.receipt import ReceiptModel
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(init_models())
