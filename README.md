# Scrapify

Scrapify is a reliable and efficient web scraper designed specifically for electronics. With Scrapify, you can quickly and easily extract product information, pricing data, and other relevant details from a wide range of electronics websites.

## Installation:

To run this project on your local machine, simply clone the repository and install the dependencies individually. However, if you prefer to use Docker containers, you can easily run the project with just a single command:

```sh
docker compose -f docker-compose-dev.yml up
```

## Tests:

To run the tests while your containers are running, execute the following command:

```sh
docker exec -it flask-scrapper sh -c 'pip3 install pytest && python3 -m pytest'
```

## Endpoints:

- [x] Search products: `/search/<product>` GET
- [x] Fetching the most bought categories: `/categories` GET
