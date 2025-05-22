import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.store import StoreModel
from ..services.store import StoreService
from ..services.exceptions import StoreAlreadyRegistered
from ..schemas.store import CreateStoreSchema

@pytest.mark.asyncio
async def test_create_store_success():
    mock_session = AsyncMock(spec=AsyncSession)
    mock_session.scalar.return_value = None

    mock_session.add = MagicMock()
    mock_session.commit = AsyncMock()
    mock_session.refresh = AsyncMock()

    store_data = CreateStoreSchema(
        email="test@example.com",
        phone="123456789",
        document="12345678900",
        picpay_client_id="client_id",
        picpay_client_secret="client_secret",
        whatsapp_token="whatsapp_token"
    )

    service = StoreService(mock_session)
    result = await service.create_store(store_data)

    mock_session.scalar.assert_awaited_once()
    mock_session.add.assert_called_once()
    mock_session.commit.assert_awaited_once()
    mock_session.refresh.assert_awaited_once()

    assert result.email == store_data.email