import requests
from bs4 import BeautifulSoup


def get_cars():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:151.0) Gecko/20100101 Firefox/151.0"
    }

    url = "https://www.finn.no/mobility/search/car?fuel=4&registration_class=1"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    cards = soup.find_all("article")

    cars = []

    for card in cards:
        name_tag = card.find("h2", class_="h4 mb-0 undefined sf-line-clamp-1")
        price_tag = card.find("span", class_="t3 font-bold")
        info_tag = card.find("span", class_="text-caption font-bold inline-block mb-8")
        img_tag = card.find("img", class_="sf-ad-carousel-desktop-item")

        if not name_tag:
            continue

        info_text = info_tag.get_text(strip=True).replace("\xa0", "") if info_tag else ""
        parts = [part.strip() for part in info_text.split("∙")]

        year = ""
        mileage = ""
        rekkevidde = ""

        for part in parts:
            if part.isdigit() and len(part) == 4:
                year = part
            elif "km rekkevidde" in part:
                rekkevidde = part.replace("km rekkevidde", "").strip()
            elif "km" in part:
                mileage = part.replace("km", "").strip()

        car = {
            "name": name_tag.get_text(strip=True),
            "cost": price_tag.get_text(strip=True).replace("\xa0", "") if price_tag else "",
            "year": year,
            "mileage": mileage,
            "rekkevidde": rekkevidde,
            "img": img_tag.get("src", "") if img_tag else ""
        }

        cars.append(car)

    return cars

