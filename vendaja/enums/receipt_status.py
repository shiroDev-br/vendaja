from enum import Enum

class ReceiptStatus(Enum):
    GENERATED='GENERATED'
    SENT='SENT'
    ERROR='ERROR'