from sqlalchemy import Column, String, DateTime, ForeignKey, Enum as SqlEnum
from sqlalchemy.dialects.postgresql import UUID
from ..infra.database.base import Base
from datetime import datetime
import uuid
from ..enums.receipt_status import ReceiptStatus

class ReceiptModel(Base):
    __tablename__='receipt_model'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    store_id = Column(UUID(as_uuid=True), ForeignKey('store_model.id'), nullable=False)
    url_pdf = Column(String(255), nullable=True)
    receipt_status = Column(SqlEnum(ReceiptStatus), nullable=True)
    sent_at = Column(DateTime, nullable=True)
    error_message = Column(String(255), nullable=True)
    created_at = Column(DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime(), nullable=True)
