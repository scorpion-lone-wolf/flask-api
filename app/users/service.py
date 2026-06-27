from app.error import ConflictError
from app.users.repository import check_email_repository
from app.users.models import User
from app.users.repository import create_user_repository, get_users_repository


def get_users_service() -> list[User]:
    return get_users_repository()


def create_user_service(user: User):
    # check for existing user
    # if exist raise ConflictError("Email already exists")
    does_exist = check_email_repository(email=user.email)
    if does_exist:
        raise ConflictError("Email already exists")
    return create_user_repository(user)
