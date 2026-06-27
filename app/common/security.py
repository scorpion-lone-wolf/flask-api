from werkzeug.security import generate_password_hash, check_password_hash


def generate_hash_password(password: str):
    return generate_password_hash(password)


def validate_password(hash_password: str, password: str):
    return check_password_hash(hash_password, password)
