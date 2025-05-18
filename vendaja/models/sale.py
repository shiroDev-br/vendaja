from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum as SqlEnum, Float
from sqlalchemy.dialects.postgresql import UUID
from ..infra.database.base import Base
from datetime import datetime
import uuid
from enum import Enum

class PaymentStatus(Enum):
    AWAITING_PAYMENT='AWAITING_PAYMENT'
    PROCESSING='PROCESSING'
    COMPLETED='COMPLETED'
    FAILED_PAYMENT='FAILED_PAYMENT'

class SaleModel(Base):
    __tablename__ = 'sale_model'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    store_id = Column(UUID(as_uuid=True), ForeignKey('store_model.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product_model.id'), nullable=False)
    customer_phone = Column(String(255), nullable=False)
    customer_name = Column(String(255), nullable=True)
    payment_id = Column(String(50), nullable=True)
    payment_url = Column(String(255), nullable=True)
    payment_status = Column(SqlEnum(PaymentStatus), nullable=False, default=PaymentStatus.AWAITING_PAYMENT)
    amount = Column(Float, nullable=False)
    tax_rate = Column(Float, nullable=False)
    created_at = Column(DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime(), nullable=True)

