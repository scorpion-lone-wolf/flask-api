from flask_jwt_extended import jwt_required
from app.error import AppError
from pydantic import ValidationError
from app.users.schemas import CreateUserSchema
from app.users.service import create_user_service, get_users_service
from app.users.models import User
from flask import request
from flask import Blueprint

# it is same like express router
user_dp = Blueprint("users", __name__, url_prefix="/api/users")


@user_dp.get("/")
@jwt_required()
def get_users_route():
    users = get_users_service()
    data = [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "is_active": user.is_active,
        }
        for user in users
    ]
    return {
        "status": "ok",
        "data": data,
    }
