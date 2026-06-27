from app.users.models import User
from app.users.repository import create_user_repository, get_users_repository


def get_users_service() -> list[User]:
    return get_users_repository()


def create_user_service(user: User):
    return create_user_repository(user)
