from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/search/<item>")
def search(item):
    url = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={item}&_sacat=0"

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

    return res


@app.route("/")
def index():
    return jsonify({"message": "hello world from docker and nginx"})
