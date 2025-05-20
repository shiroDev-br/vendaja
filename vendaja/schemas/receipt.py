from pydantic import BaseModel, Field
from datetime import datetime
from ..enums.receipt_status import ReceiptStatus

class CreateReceiptSchema(BaseModel):
    url_pdf: str
    receipt_status: ReceiptStatus
    sent_at: datetime
    error_message: str
    created_at: datetime = Field(default_factory=datetime.now)