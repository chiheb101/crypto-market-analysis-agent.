
from langchain_core.tools import tool
from services.news_api import get_crypto_news


@tool
def search_crypto_news(keyword: str, page_size: int = 2) -> dict:
    """
    Search for cryptocurrency-related news articles.

    Use this tool when the user asks about crypto news,
    market developments, or events affecting a cryptocurrency.

    Returns article titles, sources, dates, descriptions,
    and URLs. News availability may be delayed.
    """

    try:
        if page_size < 1 or page_size > 5:
            return {"error": "page_size must be between 1 and 5"}

        articles = get_crypto_news(keyword, page_size)

        if not articles:
            return {
                "error": f"No news articles found for {keyword}."
            }

        results = []

        for article in articles:
            results.append({
                "title": article.get("title"),
                "source": article.get("source", {}).get("name"),
                "published_at": article.get("publishedAt"),
                "description": article.get("description"),
                "url": article.get("url")
            })

        return {"articles": results}

    except Exception as e:
        return {
            "error": f"Unable to retrieve crypto news: {str(e)}"
        }
