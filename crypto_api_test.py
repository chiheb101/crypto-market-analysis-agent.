
import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("FREECRYPTO_API_KEY")

url = "https://api.freecryptoapi.com/v1/getData"

headers = {
    "Authorization": f"Bearer {api_key}"
}

def get_crypto_data(symbol):

    params = {
        "symbol": symbol
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    if data.get("status") != "success":
        raise ValueError(f"API returned an error: {data}")

    return data["symbols"]


# Test Bitcoin and Ethereum
cryptos = ["BTC", "ETH"]

for crypto in cryptos:

    data = get_crypto_data(crypto)

    for coin in data:
        print("\nCryptocurrency:", coin["symbol"])
        print("Price:", coin["last"])
        print("Daily change:", coin["daily_change_percentage"], "%")
        print("Exchange:", coin["source_exchange"])
