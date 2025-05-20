from typing import Any, List
from .cryptographer import encrypt_data, uncrypt_data

def process_fields(instance: Any, fields: List[str], processor: callable):
    for field in fields:
        value = getattr(instance, field, None)
        if value:
            setattr(instance, field, processor(value))

def encrypt_fields(instance: Any, fields: List[str]):
    process_fields(instance, fields, encrypt_data)

def uncrypt_fields(instance: Any, fields: List[str]):
    process_fields(instance, fields, uncrypt_data)