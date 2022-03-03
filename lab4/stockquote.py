import requests
import json
import sys

url = "https://yfapi.net/v6/finance/quote"

querystring = {"symbols": sys.argv[1]}

headers = {
    'x-api-key': "wSeAIpzIqH6hrTCBt7mpU4aZWbXKCN83a9BHVn9j"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)
long_name = data["quoteResponse"]["result"][0]['longName']
market_price = data["quoteResponse"]["result"][0]['regularMarketPrice']

print(long_name, ":", market_price)
