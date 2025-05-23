import bcrypt

def hash_password(password):
    encoded_password = str(password).encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(encoded_password, salt)

    return hashed_password


def check_password(plain_password, hashed_password):
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), hashed_password.encode("utf-8")
    )