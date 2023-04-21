import ast
from datetime import datetime
from flask import Blueprint, jsonify, make_response
from services.scrapper import store_scrapper
from database.db_connection import redis_client

scrapping_bp = Blueprint("scrapping", __name__)


def get_categories_data(products):
    products_most_bought = [
        "bookcases",
        "Mobile Electronics Accessories",
        "LED lights",
        "jewelry",
    ]
    for product in products_most_bought:
        products.append({"product": product, "data": store_scrapper(product)})
    redis_client.set("categories_cache", str(products))


@scrapping_bp.route("/search/<product>")
def search(product):
    try:
        products = store_scrapper(product)

        return make_response(jsonify(products), 200)
    except Exception as error:
        return make_response(
            jsonify({"message": "error getting products", "error": f"{error}"}), 500
        )


@scrapping_bp.route("/categories")
def categories():
    try:
        cached_data = redis_client.get("categories_cache")

        current_hour = datetime.now().hour
        current_minute = datetime.now().minute

        response_products = []

        if current_hour == 1 and current_minute == 15:  # 21:15 - (GMT-4)
            get_categories_data(response_products)
            return make_response(jsonify(response_products), 200)

        if cached_data is not None:
            return make_response(
                jsonify(ast.literal_eval(str(cached_data.decode()))), 200
            )
        get_categories_data(response_products)

        return make_response(jsonify(response_products), 200)

    except Exception as error:
        return make_response(
            jsonify({"message": "error getting products", "error": f"{error}"}), 500
        )


@scrapping_bp.route("/")
def index():
    return jsonify({"message": "hello world from docker and nginx"})
