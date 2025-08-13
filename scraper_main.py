import requests
from fake_useragent import UserAgent
from urllib.parse import quote
from bs4 import BeautifulSoup
import json


uam = UserAgent(platforms="desktop")

headers = {
    "User-Agent": uam.random
}

def writing_file(offers):
    with open("offers.json", "w", encoding="utf-8") as file:
        json.dump(offers, file, indent=4, ensure_ascii=False)

def creating_urls(query, price_from, price_to, pages=8):
    if not price_from:
        price_from = 0
    elif not price_to:
        price_to = 100000000
    urls = []
    query = quote(str(query))
    for page in range(1,pages):
        url = f"https://olx.ua/uk/list/q-{query}/?page={page}&search%5Bfilter_float_price:from%5D={price_from}&search%5Bfilter_float_price:to%5D={price_to}"
        urls.append(url)
        print(url)
    print("[+] URL`s created successfully")
    return urls

def parse_urls(urls):
    counter = 0
    for url in urls:
        print("[DEBUG] Scraper: Scraping started")
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            src = response.text
            soup = BeautifulSoup(src, "lxml")
            all_ads = soup.find_all("div", {"data-testid": "l-card"})
            if all_ads:
                for ad in all_ads:
                    href = ad.find("a", class_="css-1tqlkj0").get("href")
                    full_href = f"https://olx.ua{href}"
                    name = ad.find("h4", class_="css-1g61gc2").text.strip()
                    price = ad.find("p", {"data-testid": "ad-price"}).contents[0].text.strip()
                    offer = {
                        "name": name,
                        "price": price,
                        "href": full_href
                    }
                    print(f"Оголошення:\n"
                        f"Назва: {name}\n"
                        f"Ціна: {price}\n"
                        f"Посилання: {full_href}")
            else:
                print("[!] No offers!")


def main(query, price_from, price_to):
    urls = creating_urls(query, price_from, price_to)
    parse_urls(urls)

if __name__ == "__main__":
    try:
        main("Ноутбук", 10, 1000000)
    except KeyboardInterrupt:
        print("[!] Scraper was forcefully stopped")
