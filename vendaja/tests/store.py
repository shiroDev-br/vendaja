import pytest
from unittest.mock import AsyncMock, MagicMock
from sqlalchemy.ext.asyncio import AsyncSession

from vendaja.models.store import StoreModel
from vendaja.services.store import StoreService
from vendaja.services.exceptions import StoreAlreadyRegistered
from vendaja.schemas.store import CreateStoreSchema

@pytest.mark.asyncio
async def test_create_store_success():
    mock_session = AsyncMock(spec=AsyncSession)
    mock_session.scalar.return_value = None

    mock_session.add = MagicMock()
    mock_session.commit = AsyncMock()
    mock_session.refresh = AsyncMock()

    store_data = CreateStoreSchema(
        name='Sualoja',
        document='09827162',
        email="test@example.com",
        phone="123456789",
    )

    service = StoreService(mock_session)
    result = await service.create_store(store_data)

    mock_session.scalar.assert_awaited_once()
    mock_session.add.assert_called_once()
    mock_session.commit.assert_awaited_once()
    mock_session.refresh.assert_awaited_once()

    assert result.email == store_data.email

@pytest.mark.asyncio
async def test_create_store_already_exists():
    mock_session = AsyncMock(spec=AsyncSession)
    mock_session.scalar.return_value = StoreModel(id=1)
    
    store_data = CreateStoreSchema(
        name='Sualoja',
        document='09827162',
        email="test@example.com",
        phone="123456789",
    )
    service = StoreService(mock_session)
    with pytest.raises(StoreAlreadyRegistered):
        await service.create_store(store_data)

    mock_session.scalar.assert_awaited_once()
    mock_session.add.assert_not_called()
    mock_session.commit.assert_not_called()
    mock_session.refresh.assert_not_called()
    