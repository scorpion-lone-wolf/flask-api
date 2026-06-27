from pydantic import BaseModel, EmailStr, field_validator


class CreateUserSchema(BaseModel):
    name: str
    email: EmailStr

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str):
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        return value
