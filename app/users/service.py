from app.users.repository import create_user
from app.users.models import User
from app.users.repository import get_all_users


def list_users() -> list[User]:
    return get_all_users()


def create_user_service(user: User):
    return create_user(user)
