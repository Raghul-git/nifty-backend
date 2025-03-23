from fastapi import FastAPI
import yfinance as yf
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/history")
def get_history(symbol: str, period: Optional[str] = "max", interval: Optional[str] = "1d"):
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period=period, interval=interval)
        return hist.reset_index().to_dict(orient="records")
    except Exception as e:
        return { "error": str(e) }
