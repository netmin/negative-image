import os

from flask import Flask
from flask_cors import CORS
from flask_file_upload import FileUpload
from flask_sqlalchemy import SQLAlchemy

# instantiate the db
db = SQLAlchemy()
cors = CORS()
file_upload = FileUpload()


def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__, static_folder="static")

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    cors.init_app(app)
    file_upload.init_app(app, db)

    # register blueprints
    from project.api.image import image_blueprint

    app.register_blueprint(image_blueprint)

    # register api
    from project.api import api

    api.init_app(app)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
