from sqlalchemy.ext.asyncio import create_async_engine
from ...settings.settings import Settings

DATABASE_URL = Settings.POSTGRES_URL
engine = create_async_engine(
    DATABASE_URL
)