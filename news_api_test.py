
import os
import requests
from dotenv import load_dotenv

# Load API key
load_dotenv()

api_key = os.getenv("NEWS_API_KEY")

if not api_key:
    raise ValueError("NewsAPI key not found in .env")

# API endpoint
url = "https://newsapi.org/v2/everything"

# Request parameters
params = {
    "q": "bitcoin",
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 5
}

# Request headers
headers = {
    "X-Api-Key": api_key
}

try:
    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    if data.get("status") != "ok":
        raise ValueError(data.get("message", "NewsAPI error"))

    print("\nBitcoin News")
    print("Total results:", data["totalResults"])

    for article in data["articles"]:

        print("\nTitle:", article["title"])
        print("Source:", article["source"]["name"])
        print("Published:", article["publishedAt"])
        print("Description:", article["description"])
        print("URL:", article["url"])

except requests.exceptions.RequestException as e:
    print("API request failed:", e)

except ValueError as e:
    print("Error:", e)
