from app.users.repository import get_user_by_id_repository
from app.users.repository import create_user_repository
from app.common.security import generate_hash_password
from app.users.repository import get_user_by_email_repository
from app.users.repository import get_users_repository
from app.users.models import User


def get_users_service() -> list[User]:
    return get_users_repository()


def get_user_by_email_service(email: str):
    return get_user_by_email_repository(email=email)


def create_user_service(email: str, name: str, password: str):
    # generate password hash
    password_hash = generate_hash_password(password)
    user = User(email=email, name=name, password_hash=password_hash)
    return create_user_repository(user)


def get_user_by_id_service(id: int):
    return get_user_by_id_repository(id=id)
