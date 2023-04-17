from flask import Blueprint, jsonify, make_response
import requests
from bs4 import BeautifulSoup
from modules.config.stores_websites import alibaba_store, ebay_store

scrapping_bp = Blueprint("scrapping", __name__)


@scrapping_bp.route("/search/<product>")
def search(product):
    try:
        #  url = ebay_store(product)

        ebay_response = requests.get(ebay_store(product))
        alibaba_response = requests.get(alibaba_store(product))

        ebay_soup = BeautifulSoup(ebay_response.content, "html.parser")
        alibaba_soup = BeautifulSoup(alibaba_response.content, "html.parser")

        res = []
        for link in ebay_soup.find_all("li"):
            if (
                link.get("class") is not None
                and link.get("class")[0] == "s-item"
                and link.find("span").get("role") is not None
            ):
                if link.find("span").text != "Shop on eBay":
                    res.append(
                        {
                            "product": f'{link.find("a").get("href")}',
                            "image": f'{link.find("img").get("src")}',
                            "title": f'{link.find("span").text}',
                            "price": f'{link.find("span", attrs={"class": "s-item__price"}).text}',
                        }
                    )
        for link in alibaba_soup.find_all(
            "div",
            attrs={"class": "product-card"},
        ):
            res.append(
                {
                    "product": f'https://{link.find("a").get("href")}',
                    "image": f'{link.find("img").get("src")}',
                    "title": f'{link.find("a", attrs={"class": "product-title"}).find_all("span")[1].text}',
                    "price": f'{link.find("div", attrs={"class": "product-price"}).find_all("span")[0].text}',
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
