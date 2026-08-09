import requests
from config import GOLD_API_KEY


def get_gold_rates():

    url = "https://www.goldapi.io/api/XAU/INR"

    headers = {
        "x-access-token": GOLD_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=30, verify=False
    )

    response.raise_for_status()

    data = response.json()

    price_24k = data["price_gram_24k"]

    price_20k = round(
        price_24k * (20 / 24),
        2
    )

    return {
        "timestamp": data.get("timestamp"),

        "price_gram_24k": price_24k,
        "price_gram_22k": data.get("price_gram_22k"),
        "price_gram_21k": data.get("price_gram_21k"),
        "price_gram_20k": price_20k,
        "price_gram_18k": data.get("price_gram_18k"),

        "price_10g_24k": round(price_24k * 10, 2),
        "price_10g_22k": round(data.get("price_gram_22k") * 10, 2),
        "price_10g_20k": round(price_20k * 10, 2),
        "price_10g_18k": round(data.get("price_gram_18k") * 10, 2)
    }