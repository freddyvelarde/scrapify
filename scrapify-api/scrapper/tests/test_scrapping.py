from modules import app


def test_foo():
    with app.test_client() as c:
        response = c.get("/")
        json_response = response.get_json()
        assert json_response == {"message": "hello world from docker and nginx"}
        assert response.status_code == 200


def test_scrapping():
    with app.test_client() as c:
        response = c.get("/search/<product>")
        json_response = response.get_json()
        assert isinstance(json_response, list)
        assert all("name" in item and "price" in item for item in json_response)
        assert response.status_code == 200
