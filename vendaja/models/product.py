from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Boolean
from ..infra.database.base import Base
from datetime import datetime

class ProductModel(Base):
    id = Column(Integer, primary_key=True, auto_increment=True)
    store_id = Column(Integer, ForeignKey('store_model.id'), nullable=False)
    name = Column(String(255), nullable=False, unique=True)
    price = Column(Float, nullable=False)
    tax_rate = Column(Float, nullable=False)
    enabled = Column(Boolean, nullable=True)
    created_at = Column(DateTime(), default=datetime.utcnow, nullable=False)
    created_at = Column(DateTime(), nullable=True)