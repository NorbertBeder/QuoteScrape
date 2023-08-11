import requests


def get_by_page(endpoint):
    return requests.get(f"https://quotes.toscrape.com/{endpoint}")
