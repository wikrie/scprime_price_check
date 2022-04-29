# v0.6

import os
import sys
import requests
from requests.structures import CaseInsensitiveDict
import json
from config import Config


def get_storageprice():

    url = 'https://grafana.scpri.me/api/ds/query'
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    data = json.dumps({"queries":[{"refId":"A","datasourceId":2,"rawSql":"select to_scp(network.current_xm_maxstorageprice()*4320*1000000000000) as maxprice,\ncase \nwhen round(storageprice.storage_price*10^15/usd_scp_rate/4320/10000000000) > round(scp.storage_price/10000000000) then\n'⇧'\nwhen round(storageprice.storage_price*10^15/usd_scp_rate/4320/10000000000) < round(scp.storage_price/10000000000) then\n'⇩'\nelse '⬄'\nend as expectation,\nto_char(storageprice.storage_price,'990.00')||' USD ⇝ '||\nto_char(to_scp((storageprice.storage_price*10^15/usd_scp_rate/4320)::numeric(38,0)*1000000000000*4320),'990.00')\n||' SCP' as goal\nfrom markets.target_storage_price_scp scp\ncross join \n(select storage_price from markets.storage_price_usd spu\n where valid_since<=unix_now()\n  order by valid_since desc limit 1\n) storageprice\ncross join (select usd as usd_scp_rate from markets.coingecko_simple cs order by last_updated_at desc limit 1) cs1\nwhere valid_since <= unix_now()\norder by valid_since desc limit 1\n;\n","format":"table","intervalMs":1800000,"maxDataPoints":1129}],"range":{"from":"2022-03-30T17:33:34.857Z","to":"2022-04-29T17:33:34.857Z","raw":{"from":"now-30d","to":"now"}},"from":"1648661614857","to":"1651253614857"})
    r = requests.post(url, data=data, headers=headers)
    r = r.json()
    try:
        storageprice = r['results']['A']['frames'][0]['data']['values'][0][0]
    except:
        print("Error processing JSON", flush=True)
        storageprice = "no data"

    return storageprice

def main():
    host_v = os.popen(Config.base_cmd + ' host -v').readlines()
    n = 1
    for e in host_v:
        if n == 22:
            minstorageprice = e.split()[1]
            break
        n += 1
    reference_price = get_storageprice()
    if reference_price == 'no data':
        sys.exit()
    target_scp_price = str(round(float(reference_price) * 0.994, 3))
    print(f'Target price {target_scp_price}', flush=True)
    print(f'Current price {minstorageprice}', flush=True)

    if minstorageprice == target_scp_price:
        print(f'No change', flush=True)
    else:
        print(f"Changing price to {target_scp_price}", flush=True)
        os.system(Config.base_cmd + ' host config minstorageprice ' + str(target_scp_price) + 'SCP')
        os.system(Config.base_cmd + ' host config collateral ' + str(target_scp_price) + 'SCP')
        # os.system(Config.base_cmd + ' host -v')

if __name__ == '__main__':
    main()
