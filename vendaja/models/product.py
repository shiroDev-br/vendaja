from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Boolean
from sqlalchemy.dialects.postgresql import UUID
from ..infra.database.base import Base
from datetime import datetime

class ProductModel(Base):
    __tablename__ = 'product_model'
    id = Column(Integer, primary_key=True)
    store_id = Column(UUID(as_uuid=True), ForeignKey('store_model.id'), nullable=False)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    tax_rate = Column(Float, nullable=False)
    enabled = Column(Boolean, nullable=True)
    created_at = Column(DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime(), nullable=True)