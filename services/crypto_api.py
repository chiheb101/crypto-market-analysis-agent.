
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FREECRYPTO_API_KEY")

BASE_URL = "https://api.freecryptoapi.com/v1/getData"


def get_crypto_data(symbol):

    if not API_KEY:
        raise ValueError("FreeCryptoAPI key not found")

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    params = {
        "symbol": symbol.upper()
    }

    response = requests.get(
        BASE_URL,
        headers=headers,
        params=params,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    if data.get("status") != "success":
        raise ValueError(f"Crypto API error: {data}")

    return data["symbols"]
