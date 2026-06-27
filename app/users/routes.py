from app.users.service import create_user_service
from app.users.models import User
from flask import request
from flask import Blueprint
from app.users.service import list_users

# it is same like express router
user_dp = Blueprint("users", __name__, url_prefix="/api/users")


@user_dp.get("/")
def get_users_route():
    users = list_users()
    data = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
    return {
        "status": "ok",
        "data": data,
    }


@user_dp.post("/")
def create_user_route():
    # get data from body of the request
    request_data = request.get_json()
    name = request_data["name"]
    email = request_data["email"]
    # creating User type object
    user = User(name=name, email=email)
    # call the service file and return the response
    created_user = create_user_service(user)
    return {
        "status": "ok",
        "message": "User created successfully",
        "data": [
            {
                "id": created_user.id,
                "name": created_user.name,
                "email": created_user.email,
            },
        ],
    }, 201
