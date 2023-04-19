import requests
from bs4 import BeautifulSoup


def alibaba_scrapper(product):
    try:
        alibaba_response = requests.get(
            f"https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&tab=all&SearchText={product}&isPremium=y&secondFlag=true"
        )

        alibaba_soup = BeautifulSoup(alibaba_response.content, "html.parser")

        products = []

        for link in alibaba_soup.find_all(
            "div",
            attrs={"class": "product-card"},
        ):
            products.append(
                {
                    "product": f'https://{link.find("a").get("href")}',
                    "image": f'{link.find("img").get("src")}',
                    "title": f'{link.find("a", attrs={"class": "product-title"}).find_all("span")[1].text}',
                    "price": f'{link.find("div", attrs={"class": "product-price"}).find_all("span")[0].text}',
                    "store": "https://www.alibaba.com",
                }
            )
        return products
    except ValueError as error:
        print(error)


def ebay_scrapper(product):
    try:
        ebay_response = requests.get(
            f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={product}&_sacat=0"
        )

        ebay_soup = BeautifulSoup(ebay_response.content, "html.parser")

        products = []

        for link in ebay_soup.find_all("li"):
            if (
                link.get("class") is not None
                and link.get("class")[0] == "s-item"
                and link.find("span").get("role") is not None
            ):
                if link.find("span").text != "Shop on eBay":
                    products.append(
                        {
                            "product": f'{link.find("a").get("href")}',
                            "image": f'{link.find("img").get("src")}',
                            "title": f'{link.find("span").text}',
                            "price": f'{link.find("span", attrs={"class": "s-item__price"}).text}',
                            "store": "https://www.ebay.com",
                        }
                    )
        return products

    except ValueError as error:
        print(error)


def store_scrapper(product):
    return ebay_scrapper(product) + alibaba_scrapper(product)
