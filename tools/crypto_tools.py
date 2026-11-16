
from langchain_core.tools import tool
from services.crypto_api import get_crypto_data


@tool
def get_crypto_market_data(symbol: str) -> dict:
    """
    Get cryptocurrency market information using its symbol.
    Returns market data or an error message if unavailable.
    """
    try:
        data = get_crypto_data(symbol)

        if not data:
            return {
                "error": f"No market data found for {symbol.upper()}."
            }

        results = []

        for coin in data:
            results.append({
                "symbol": coin["symbol"],
                "price": coin["last"],
                "daily_change_percentage": coin["daily_change_percentage"],
                "lowest": coin["lowest"],
                "highest": coin["highest"],
                "date": coin["date"],
                "exchange": coin["source_exchange"]
            })

        return {"data": results}

    except Exception as e:
        return {"error": f"Unable to retrieve market data: {str(e)}"}
