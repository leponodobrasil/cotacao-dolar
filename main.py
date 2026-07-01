import pandas as pd
import yfinance as yf
from datetime import datetime

# Busca o histórico do dólar
ticker = "BRL=X"

df = yf.download(
    tickers=ticker,
    start='2017-01-01',
    end=datetime.today().strftime('%Y-%m-%d')
)
df.to_csv('dolar.csv')