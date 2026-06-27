from app.extensions import db
from app.users.models import User


# responsible for interacting with the database to get all users
def get_users_repository():
    page = 1
    limit_per_page = 10
    skip = (page - 1) * 10
    # create a statement (query)
    statement = db.select(User).order_by(User.id).offset(skip).limit(limit_per_page)

    # execute the statement
    users = db.session.execute(statement).scalars().all()
    return list(users)


# responsible for interacting with the database to validate email exist or no
def get_user_by_email_repository(email: str):
    statement = db.select(User).where(User.email == email)
    user = db.session.execute(statement).scalars().first()
    return user


# responsible for interacting with the database to create a new user
def create_user_repository(user: User):
    db.session.add(user)
    db.session.commit()
    return user


def get_user_by_id_repository(id: int):
    statement = db.select(User).where(User.id == id)
    user = db.session.execute(statement).scalars().first()
    return user
