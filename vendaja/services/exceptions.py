class StoreAlreadyRegistered(Exception):
    "Raised when a duplicate field tries to be recorded in the database"

class ProductAlreadyExists(Exception):
    "Raised when a duplicate name of prodcut tries to be recorded in the database"