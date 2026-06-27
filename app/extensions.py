from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate


#  This is just the base class from which all models inherit
class Base(DeclarativeBase):
    pass


# here db is not the actual database
# It just help us to interact with the database
# Example :
#   db.Model to create a table
#   db.session to save the data to the database
db = SQLAlchemy(model_class=Base)
migrate = Migrate()
