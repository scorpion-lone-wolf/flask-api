from pydantic import ValidationError
from flask import Flask


class AppError(Exception):
    status_code = 400
    message = "Something went wrong"

    def __init__(self, message: str | None = None):
        if message:
            self.message = message


class ConflictError(AppError):
    status_code = 409
    message = "Conflict"


def register_error_handler(app: Flask):
    @app.errorhandler(AppError)
    def handle_app_error(error: AppError):
        return {"status": "fail", "message": error.message}, error.status_code

    @app.errorhandler(ValidationError)
    def handle_validation_error(error: ValidationError):
        return {"status": "fail", "message": error.errors()[0].get("msg")}, 400

    @app.errorhandler(ValueError)
    def handle_value_error(error: ValueError):
        return {"status": "fail", "message": error.errors()[0].get("msg")}, 400

    @app.errorhandler(Exception)
    def handle_general_error(error: Exception):
        return {"status": "fail", "message": "Something went wrong"}, 400
