import os
from os.path import join, dirname, realpath


class BaseConfig:
    """Base configuration"""

    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "my_precious"

    # This is the directory that flask-file-upload saves files to.
    # Make sure the UPLOAD_FOLDER is the same as Flasks's static_folder or a child. For example:
    UPLOAD_FOLDER = join(dirname(realpath(__file__)), "static/uploads")

    # Other FLASK config variables ...
    ALLOWED_EXTENSIONS = ["jpg", "png", "jpeg"]
    MAX_CONTENT_LENGTH = 1000 * 1024 * 1024  # 1000mb


class DevelopmentConfig(BaseConfig):
    """Development configuration"""

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestingConfig(BaseConfig):
    """Testing configuration"""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")


class ProductionConfig(BaseConfig):
    """Production configuration"""

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
