import yfinance as yf

symbol = 'MSFT'

symbol_get = yf.Ticker(symbol)

# get stock info
print(symbol_get)

# get historical market data
hist = symbol_get.history(period="5d")

print(hist.head())

hist.to_csv(f'{symbol}.csv', index = True)