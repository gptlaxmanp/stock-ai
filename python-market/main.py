from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="Stock AI Market Service",
    version="0.1.0"
)


@app.get("/health")
def health():
    return {
        "status": "UP",
        "service": "python-market",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.get("/market/{symbol}")
def market(symbol: str):
    symbol = symbol.upper()

    return {
        "symbol": symbol,
        "price": 0.0,
        "currency": "INR",
        "source": "DEMO",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }