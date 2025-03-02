import requests

symbol = "AAPL"
url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token=your_api_key"
data = requests.get(url).json()
print(f"{symbol} Price: ${data['c']}")
