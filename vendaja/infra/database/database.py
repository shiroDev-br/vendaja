from sqlalchemy.ext.asyncio import create_async_engine
from ...settings.settings import Settings

settings = Settings()

DATABASE_URL = settings.POSTGRES_URL
engine = create_async_engine(
    DATABASE_URL
)