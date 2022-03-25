import os
import requests
import json

# config: update this values to your preferences
target_price = 3.9 # $/TB
tolerance = 0.5 # difference must be greater than this % to change the price
base_cmd = 'docker exec scprime02 spc' # the first part of the command you use to call spc
# end config

url = 'https://api.coinbase.com/v2/exchange-rates?currency=SCP'
r = requests.get(url)
data = json.loads(r.text)
print(f"$/SCP: {data['data']['rates']['USD']}", flush=True)
print(f"EUR/SCP: {data['data']['rates']['EUR']}", flush=True)
host_v = os.popen(base_cmd + ' host -v').readlines()

n = 1
for e in host_v:
    if n == 14:
        collateral = float(e.split()[1])
    if n == 22:
        minstorageprice = float(e.split()[1])
        break
    n += 1

target_scp_price = target_price / float(data['data']['rates']['USD'])
current_scp_price = minstorageprice

if abs((current_scp_price / target_scp_price - 1 ) * 100) > tolerance:
    print(f"Changing price from {current_scp_price} to {target_scp_price}", flush=True)
    os.system(base_cmd + ' host config minstorageprice ' + str(target_scp_price) + 'SCP')
    os.system(base_cmd + ' host config collateral ' + str(target_scp_price) + 'SCP')
else:
    print(f"The difference in price is less than {tolerance}%", flush=True)

os.system(base_cmd + ' host -v')
