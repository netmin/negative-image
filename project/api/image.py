import pathlib
from io import BytesIO

import cv2
import numpy as np
from flask import Blueprint, request
from flask_restx import Namespace, Resource, fields
from werkzeug.datastructures import FileStorage

from project import db
from project import file_upload
from project.api.models import Image

image_blueprint = Blueprint("image", __name__)

images_namespace = Namespace("", description="Images operations")

img = images_namespace.model(
    "Image",
    {
        "id": fields.Integer(readOnly=True),
        "original_url": fields.String(),
        "negative_url": fields.String(),
        "created_date": fields.DateTime,
    },
)
parser = images_namespace.parser()
parser.add_argument("file", location="files", type=FileStorage, required=True)


def create_negative(original):
    orig_filename = f"orig_{original.filename}"
    gray_filename = f"gray_{original.filename}"

    img_as_np = np.frombuffer(original.read(), dtype=np.uint8)
    gray_img = cv2.imdecode(img_as_np, cv2.IMREAD_GRAYSCALE)
    orig_img = cv2.imdecode(img_as_np, cv2.IMREAD_COLOR)

    cv2.imwrite(gray_filename, gray_img)
    cv2.imwrite(orig_filename, orig_img)

    return orig_filename, gray_filename


def create_file_storage(filename, name, content_type):
    with open(filename, "rb") as f:
        stream = BytesIO(f.read())

    negative = FileStorage(stream, filename, name=name, content_type=content_type)
    file = pathlib.Path(filename)
    file.unlink()

    return negative


class ImageList(Resource):
    @images_namespace.response(201, "Image  was added!")
    @images_namespace.expect(parser)
    def post(self):
        image = Image()
        original = request.files["original"]
        name = f"gray_{original.name}"

        orig_filename, gray_filename = create_negative(original)
        original = create_file_storage(
            orig_filename, original.name, original.content_type
        )
        negative = create_file_storage(gray_filename, name, original.content_type)

        file_upload.save_files(
            image, files={"original": original, "negative": negative}
        )
        image.original_url = file_upload.get_file_url(image, filename="original")
        image.negative_url = file_upload.get_file_url(image, filename="negative")

        db.session.add(image)
        db.session.commit()

        response_object = {
            "status": "success",
            "message": f"Image {original.filename} was added!",
        }
        return response_object, 201

    @images_namespace.marshal_with(img, as_list=True)
    def get(self):

        last_images = Image.query.order_by(Image.id.desc()).limit(3).all()

        return last_images, 200


images_namespace.add_resource(ImageList, "/image")
