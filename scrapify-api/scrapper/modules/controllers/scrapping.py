from flask import Blueprint, jsonify, make_response
import requests
from bs4 import BeautifulSoup
from modules.config.stores_websites import ebay_store

scrapping_bp = Blueprint("scrapping", __name__)


@scrapping_bp.route("/search/<product>")
def search(product):
    try:
        url = ebay_store(product)

        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")

        res = []
        for link in soup.find_all("li"):
            if (
                link.get("class") is not None
                and link.get("class")[0] == "s-item"
                and link.find("span").get("role") is not None
            ):
                res.append(
                    {
                        "product": f'{link.find("a").get("href")}',
                        "image": f'{link.find("img").get("src")}',
                        "title": f'{link.find("span").text}',
                        "price": f'{link.find("span", attrs={"class": "s-item__price"}).text}',
                    }
                )

        return make_response(jsonify(res), 200)
    except ValueError as error:
        return make_response(
            jsonify({"message": "error getting products", "error": f"{error}"}), 500
        )


@scrapping_bp.route("/")
def index():
    return jsonify({"message": "hello world from docker and nginx"})
