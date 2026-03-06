import numpy as np
import pandas as pd
import yfinance as yf


data = yf.download('AAPL', start='2024-01-01', end='2024-12-31')

df = pd.DataFrame(data)

df = data.xs('AAPL', axis=1, level=1)

df['Daily Return'] = df['Close'].pct_change()

df['MA50'] = df['Close'].rolling(50).mean()

df['MA200'] = df['Close'].rolling(200).mean()

df['signal'] = np.where(df['MA50'] > df['MA200'], 'BUY', 'SELL')

best_day = df['Daily Return'].idxmax()
worst_day = df['Daily Return'].idxmin()

df[['Close', 'MA50', 'MA200', 'Daily Return', 'signal']].to_csv('apple_analysis.csv')

print('=== APPLE STOCK 2024 SUMMARY ===')
print('Total trading days:', len(df))
print('Start price: $', round(df['Close'].iloc[0], 2))
print('End price: $', round(df['Close'].iloc[-1], 2))
print('Total return:', round((df['Close'].iloc[-1] / df['Close'].iloc[0] - 1) * 100, 2), '%')
print('Best day:', best_day.date(), round(df['Daily Return'].max() * 100, 2), '%')
print('Worst day:', worst_day.date(), round(df['Daily Return'].min() * 100, 2), '%')