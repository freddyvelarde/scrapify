from modules import app


def test_foo():
    with app.test_client() as c:
        response = c.get("/")
        json_response = response.get_json()
        assert json_response == {"message": "hello world from docker and nginx"}
        assert response.status_code == 200


def test_search_products():
    with app.test_client() as c:
        response = c.get("/search/<product>")
        json_response = response.get_json()
        assert isinstance(json_response, list)
        assert response.status_code == 200


def test_categories():
    with app.test_client() as c:
        response = c.get("/categories")
        json_response = response.get_json()
        assert isinstance(json_response, list)
        assert response.status_code == 200
