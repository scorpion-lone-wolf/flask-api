from app.extensions import db
from app.users.models import User


def get_users_repository():
    page = 1
    limit_per_page = 10
    skip = (page - 1) * 10
    # create a statement (query)
    statement = db.select(User).order_by(User.id).offset(skip).limit(limit_per_page)

    # execute the statement
    users = db.session.execute(statement).scalars().all()
    return list(users)


def check_email_repository(email: str):
    statement = db.select(User).where(User.email == email)
    user = db.session.execute(statement).scalars().all()
    if len(user) > 0:
        return True
    return False


def create_user_repository(user: User):
    db.session.add(user)
    db.session.commit()
    return user
