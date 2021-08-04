import json
from io import BytesIO


def test_get_images(test_app, test_database):
    client = test_app.test_client()
    resp = client.get("/image")
    assert resp.status_code == 200


def test_add_image(test_app, test_database):
    client = test_app.test_client()
    with open("/app/project/tests/test.png", "rb") as f:
        data = dict(original=(BytesIO(f.read()), "test.png"))

        resp = client.post(
            "/image",
            data=data,
            content_type="multipart/form-data",
        )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert "success" in data["status"]
