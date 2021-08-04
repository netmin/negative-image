from sqlalchemy.sql import func

from project import db
from project import file_upload


@file_upload.Model
class Image(db.Model):
    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    original = file_upload.Column()
    negative = file_upload.Column()
    original_url = db.Column(db.String)
    negative_url = db.Column(db.String)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)
