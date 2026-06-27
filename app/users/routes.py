from flask import Blueprint

# it is same like express router
user_dp = Blueprint("users", __name__, url_prefix="/api/users")


@user_dp.route("/")
def list_users():
    return {
        "status": "ok",
        "data": [],
    }
