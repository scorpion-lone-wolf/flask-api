# request schema
from pydantic import BaseModel, EmailStr, field_validator


class RegisterSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

    # custom validation
    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str):
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        return value

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value


class LoginSchema(BaseModel):
    email: EmailStr
    password: str
