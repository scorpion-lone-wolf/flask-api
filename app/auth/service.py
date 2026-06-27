from app.users.service import create_user_service
from app.users.service import get_user_by_email_service
from app.error import ConflictError
from app.users import User


def register_service(name: str, email: str, password: str) -> User:
    # validate if user already exist
    user = get_user_by_email_service(email=email)
    if user:
        raise ConflictError("User already exist")
    return create_user_service(email=email, name=name, password=password)
