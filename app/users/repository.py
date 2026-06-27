from app.extensions import db
from app.users.models import User


def get_all_users():
    page = 1
    limit_per_page = 10
    skip = (page - 1) * 10
    # create a statement (query)
    statement = db.select(User).order_by(User.id).offset(skip).limit(limit_per_page)

    # execute the statement
    users = db.session.execute(statement).scalars().all()
    return list(users)


def create_user(user: User):
    db.session.add(user)
    db.session.commit()
    return user
