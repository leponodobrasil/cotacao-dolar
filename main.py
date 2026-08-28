import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

ticker = "BRL=X"

# Avança um dia para compensar o comportamento exclusivo do parâmetro 'end'
end_date = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')

df = yf.download(
    tickers=ticker,
    start='2017-01-01',
    end=end_date
)

# Trata o MultiIndex caso a versão do yfinance o retorne
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.droplevel(1)
df.columns.name = None

# Transforma o índice 'Date' em uma coluna normal
df_alinhado = df.reset_index()

print(df_alinhado.tail())

# Salva o arquivo CSV
df_alinhado.to_csv('dolar.csv', index=False)
