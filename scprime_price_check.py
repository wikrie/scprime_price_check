import os
import requests
import json

target_price = 3 # $/TB

url = 'https://api.coinbase.com/v2/exchange-rates?currency=SCP'
r = requests.get(url)
data = json.loads(r.text)
print(data['data']['rates']['USD'])
print(data['data']['rates']['EUR'])
host_v = os.popen('docker exec scprime01 spc host -v').readlines()

n = 1
for e in host_v:
    if n == 14:
        collateral = e.split()[1]
        print(collateral)
    if n == 22:
        minstorageprice = e.split()[1]
        print(minstorageprice)
        break
    n += 1
