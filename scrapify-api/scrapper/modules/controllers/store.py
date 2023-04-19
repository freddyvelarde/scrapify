from flask import Blueprint, jsonify, make_response
from services.scrapper import store_scrapper

scrapping_bp = Blueprint("scrapping", __name__)


@scrapping_bp.route("/search/<product>")
def search(product):
    try:
        products = store_scrapper(product)

        return make_response(jsonify(products), 200)
    except ValueError as error:
        return make_response(
            jsonify({"message": "error getting products", "error": f"{error}"}), 500
        )


@scrapping_bp.route("/categories")
def categories():
    try:
        products = [
            "jewelry",
            "bookcases",
            "Mobile Electronics Accessories",
            "LED lights",
        ]
        response_products = {}
        for product in products:
            response_products[product] = store_scrapper(product)

        return make_response(jsonify(response_products), 200)

    except ValueError as error:
        return make_response(
            jsonify({"message": "error getting products", "error": f"{error}"}), 500
        )


@scrapping_bp.route("/")
def index():
    return jsonify({"message": "hello world from docker and nginx"})
