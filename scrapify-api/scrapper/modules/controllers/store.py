from flask import Blueprint, jsonify, make_response
from services.scrapper import store_scrapper
import redis as redis_modules

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
        response_products = []
        for product in products:
            response_products.append(
                {"product": product, "data": store_scrapper(product)}
            )

        return make_response(jsonify(response_products), 200)

    except ValueError as error:
        return make_response(
            jsonify({"message": "error getting products", "error": f"{error}"}), 500
        )


@scrapping_bp.route("/redis")
def redis():
    redis_client = redis_modules.Redis(host="cache", port=6379, db=0)
    redis_client.set("username", "fredvel59")
    return make_response(
        jsonify({"username": redis_client.get("username").decode()}), 200
    )


@scrapping_bp.route("/")
def index():
    return jsonify({"message": "hello world from docker and nginx"})
