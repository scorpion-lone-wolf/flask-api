import os
from dotenv import load_dotenv

load_dotenv()

Config = {
    "FLASK_ENV": os.getenv("FLASK_ENV"),
    "SECRET_KEY": os.getenv("SECRET_KEY"),
    "SQLALCHEMY_DATABASE_URI": os.getenv("DATABASE_URL"),
    "JWT_SECRET_KEY": os.getenv("JWT_SECRET_KEY"),
    "DEBUG": True if os.getenv("DEBUG") == "true" else False,
}
