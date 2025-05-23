from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from ..infra.database.base import Base
from datetime import datetime
import uuid

class StoreModel(Base):
    __tablename__ = 'store_model'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), unique=True)
    document = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    phone = Column(String(255), nullable=False, unique=True)
    pipcay_client_id = Column(String(255), nullable=True, unique=True)
    picpay_client_secret = Column(String(255), nullable=True, unique=True)
    whatsapp_token = Column(String(255), nullable=True, unique=True)
    rate_limit = Column(Integer, nullable=False, default=60)
    created_at = Column(DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime(), nullable=True)