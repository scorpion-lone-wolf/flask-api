from app.extensions import jwt
from app.auth.routes import auth_bp
from app.error import register_error_handler
from app.users import user_dp
from app.extensions import db, migrate
from app.config.config import Config
from flask import Flask


def create_app():
    app = Flask(__name__)

    # load the Config (flask expect a config object to be passed inside app.config)
    app.config.update(**Config)

    # db initialization with app
    db.init_app(app)
    # migration initialization with app and db (this will help in db migrations)
    migrate.init_app(app, db)

    # jwt initialization with app
    jwt.init_app(app)

    # we import the models here so that sqlalchemy knows they exist
    # if we don't import the model files will not run and the db will not be created
    from app.users import User

    # print(db.metadata.tables.keys())

    # register the blueprint(routes)
    app.register_blueprint(user_dp)
    app.register_blueprint(auth_bp)

    # register error handlers
    register_error_handler(app)

    @app.route("/")
    def health():
        return {
            "status": "ok",
            "message": "Flask API is running",
            "environment": app.config["DEBUG"],
            "database": app.config["SQLALCHEMY_DATABASE_URI"],
        }

    return app
