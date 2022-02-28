import os
import requests
import json

target_price = 3.0 # $/TB
tolerance = 1.0 #difference must be greater than this to change the price

url = 'https://api.coinbase.com/v2/exchange-rates?currency=SCP'
r = requests.get(url)
data = json.loads(r.text)
print(f'$/SCP: {data['data']['rates']['USD']}')
print(f'EUR/SCP: {data['data']['rates']['EUR']}')
host_v = os.popen('docker exec scprime01 spc host -v').readlines()

n = 1
for e in host_v:
    if n == 14:
        collateral = float(e.split()[1])
        print(collateral)
    if n == 22:
        minstorageprice = float(e.split()[1])
        print(minstorageprice)
        break
    n += 1

target_scp_price = target_price / data['data']['rates']['USD']
current_scp_price = minstorageprice / data['data']['rates']['USD']

if abs((current_scp_price / target_scp_price - 1 ) * 100)) > tolerance:
    print(f'Cambiamos el precio desde {current_scp_price} a {target_scp_price}')
