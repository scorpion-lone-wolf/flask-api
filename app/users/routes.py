from app.users.schemas import CreateUserSchema
from app.users.service import create_user_service, get_users_service
from app.users.models import User
from flask import request
from flask import Blueprint

# it is same like express router
user_dp = Blueprint("users", __name__, url_prefix="/api/users")


@user_dp.get("/")
def get_users_route():
    users = get_users_service()
    data = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
    return {
        "status": "ok",
        "data": data,
    }


@user_dp.post("/")
def create_user_route():
    request_data = request.get_json()
    try:
        CreateUserSchema.model_validate(request_data)
    except Exception as e:
        return {"status": "error", "message": str(e)}, 400

    # get data from body of the request
    name = request_data["name"]
    email = request_data["email"]
    # creating User type object
    user = User(name=name, email=email)
    # call the service file and return the response
    try:
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
    except Exception as e:
        return {"status": "error", "message": str(e)}, 400
