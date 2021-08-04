from flask_restx import Api

from project.api.image import images_namespace

api = Api(version="1.0", title="Images API", doc="/doc")
api.add_namespace(images_namespace, path="")
