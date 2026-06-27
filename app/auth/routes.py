from app.auth.service import login_service
from app.auth.service import register_service
from app.auth.schemas import RegisterSchema, LoginSchema
from flask import Blueprint, request

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_bp.post("/register")
def register_user_route():
    # get data from body
    body = request.get_json()
    # validation of the data
    data = RegisterSchema.model_validate(body)
    user = register_service(name=data.name, email=data.email, password=data.password)
    return {
        "status": "ok",
        "data": {"id": user.id, "name": user.name, "email": user.email},
    }


@auth_bp.post("/login")
def login_user_route():
    # get data from body
    body = request.get_json()
    # validation of the data
    data = LoginSchema.model_validate(body)
    token = login_service(email=data.email, password=data.password)
    return {
        "status": "ok",
        "data": {
            "message": "Login successful",
            "access_token": token,
        },
    }
