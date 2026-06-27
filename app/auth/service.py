from flask_jwt_extended import create_access_token
from app.common.security import validate_password
from app.users.service import create_user_service, get_user_by_email_service
from app.error import ConflictError
from app.users import User
from datetime import timedelta


def register_service(name: str, email: str, password: str) -> User:
    # validate if user already exist
    user = get_user_by_email_service(email=email)
    if user:
        raise ConflictError("User already exist")
    return create_user_service(email=email, name=name, password=password)


def login_service(email: str, password: str):
    # validate if user already exist
    user = get_user_by_email_service(email=email)
    if not user:
        raise Exception("User does not exist")
    if not validate_password(user.password_hash, password):
        raise Exception("Invalid password")
    # create access token
    token = create_access_token(
        identity=str(user.id),
        additional_claims={"role": user.role, "email": user.email},
        expires_delta=timedelta(minutes=1),
    )
    return token
