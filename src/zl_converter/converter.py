from urllib.request import urlopen
from urllib.error import URLError
from datetime import datetime
import json


def converter(num):
    try:
        url = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur/pln.json"
        response = urlopen(url)
        data = json.loads(response.read())
        data = {
            "date": datetime.strptime(data["date"], "%Y-%m-%d").strftime(
                "%d of %B, %Y"
            ),
            "pln": float(data["pln"]),
        }
        print(
            f"Downloading recent conversion rate.\nRate from {data['date']}: 1 Euro = {data['pln']} zloty."
        )
    except URLError:
        data = {"date": "01 of January, 2022", "pln": 4.588727}
        print(
            f"No internet connection found.\nRate from {data['date']}: 1 Euro = {data['pln']} zloty."
        )
    res1 = round(num / data["pln"], 3)
    res2 = round(num * data["pln"], 3)
    print(f"-------\n{num} zloty -> {res1} Euro\n{num} Euro -> {res2} zloty\n-------")
