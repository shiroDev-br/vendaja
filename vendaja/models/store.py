from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from ..infra.database.base import Base
from datetime import datetime
import uuid

class StoreModel(Base):
    __tablename__ = 'store_model'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    document = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)
    pipcay_client_id = Column(String(255), nullable=True)
    picpay_client_secret = Column(String(255), nullable=True)
    whatsapp_token = Column(String(255), nullable=True)
    rate_limit = Column(Integer, nullable=False, default=60)
    created_at = Column(DateTime(), default=datetime.utcnow, nullable=False)
    created_at = Column(DateTime(), nullable=True)