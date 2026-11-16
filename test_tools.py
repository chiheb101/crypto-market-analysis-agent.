
from tools.crypto_tools import get_crypto_market_data
from tools.news_tools import search_crypto_news


# Test cryptocurrency tool
print("\n===== CRYPTO TOOL =====")

crypto_result = get_crypto_market_data.invoke({
    "symbol": "BTC"
})

print(crypto_result)


# Test news tool
print("\n===== NEWS TOOL =====")

news_result = search_crypto_news.invoke({
    "keyword": "Bitcoin",
    "page_size": 3
})

print(news_result)
