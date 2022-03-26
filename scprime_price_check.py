import os
import sys
import json
from urllib.request import Request, urlopen
from urllib.error import URLError
from config import Config

url = 'https://api.coinbase.com/v2/exchange-rates?currency=SCP'
req = Request(url)
try:
    response = urlopen(req)
except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    sys.exit()

data = json.loads(response.read())
print(f"$/SCP: {data['data']['rates']['USD']}", flush=True)
print(f"EUR/SCP: {data['data']['rates']['EUR']}", flush=True)
host_v = os.popen(Config.base_cmd + ' host -v').readlines()

n = 1
for e in host_v:
    if n == 14:
        collateral = float(e.split()[1])
    if n == 22:
        minstorageprice = float(e.split()[1])
        break
    n += 1

target_scp_price = Config.target_price / float(data['data']['rates']['USD'])
current_scp_price = minstorageprice

if abs((current_scp_price / target_scp_price - 1 ) * 100) > Config.tolerance:
    print(f"Changing price from {current_scp_price} to {target_scp_price}", flush=True)
    os.system(Config.base_cmd + ' host config minstorageprice ' + str(target_scp_price) + 'SCP')
    os.system(Config.base_cmd + ' host config collateral ' + str(target_scp_price) + 'SCP')
else:
    print(f"The difference in price is less than {Config.tolerance}%", flush=True)

os.system(Config.base_cmd + ' host -v')
