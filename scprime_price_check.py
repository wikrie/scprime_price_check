import requests
import json

target_price = 3 # $/TB

url = 'https://api.coinbase.com/v2/exchange-rates?currency=SCP'
r = requests.get(url)
data = json.loads(r.text)
print(data['data']['rates']['USD'])
print(data['data']['rates']['EUR'])
