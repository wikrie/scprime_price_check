#v0.5

import requests
from requests.structures import CaseInsensitiveDict
import json
from config import Config

url = 'https://grafana.scpri.me/api/ds/query'

def get_price():

    status = get_status(Config.provider_primary)
    print(f'Status of Primary Provider= {status} :: 0=Offline :: 1=Online :: 2=Error', flush=True)
    if status == 1:
        price = get_storageprice(Config.provider_primary)
        print(f'Reference price on Primary Provider = {price}', flush=True)
    else:
        status = get_status(Config.provider_secondary)
        print(f'Status of Secondary Provider = {status} :: 0=Offline :: 1=Online :: 2=Error', flush=True)
        if status == 1:
            price = get_storageprice(Config.provider_secondary)
            print(f'Reference price on Secondary Provider = {price}', flush=True)
        else:
            print(f'Both providers are offline. Edit config.py and place the Id of a working XM', flush=True)
            price = 'no data'
    return price


def get_status(publickey):

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    data = json.dumps({"queries":[{"refId":"A","datasourceId":2,"rawSql":"SELECT \nverified::int,\nuptimeratio,\n--acceptingcontracts::int,\nincentives_factor,\ntotalstorage, \ntotalstorage-remainingstorage as usedstorage\n--lastscantime*1000 as timestamp\nFROM network.provider_details \nWHERE publickey='"+publickey+"'","format":"table","intervalMs":3600000,"maxDataPoints":874}],"range":{"raw":{"from":"now-30d","to":"now"}}})
    r = requests.post(url, data=data, headers=headers)
    r = r.json()
    try:
        status = r['results']['A']['frames'][0]['data']['values'][0][0]
    except:
        print("Error processing JSON", flush=True)
        status = 2

    return status

def get_storageprice(publickey):

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    data = json.dumps({"queries":[{"refId":"A","datasourceId":2,"rawSql":"SELECT \nto_SCP(c.used_capacity_incentives) AS incent_curr,\nto_SCP(p.used_capacity_incentives) AS incent_last,\nto_SCP(pd.storageprice*4320)*1000000000000 as \"Storage Price (SCP/TB/month)\",\nto_SCP(pd.collateral*4320)*1000000000000 as \"Collateral Price (SCP/TB/month)\",\nto_SCP(pd.maxcollateral) as \"Max Collateral (SCP/contract)\", \nto_SCP(pd.downloadbandwidthprice)*1000000000000 as \"Download Bandwith (SCP/TB)\",\nto_SCP(pd.uploadbandwidthprice)*1000000000000 as \"Upload Bandwith (SCP/TB)\",\npd.maxduration*600 as maxduration\n--to_SCP(contractprice) as \"Contract Creation Fee (SCP)\"\nFROM network.provider_details pd\njoin network.current_month_incentives c on pd.publickey = c.publickey left join network.previous_month_incentives p on c.publickey = p.publickey\nWHERE pd.publickey='"+publickey+"'","format":"table","intervalMs":10800000,"maxDataPoints":229}],"range":{"raw":{"from":"now-30d","to":"now"}}})
    r = requests.post(url, data=data, headers=headers)
    r = r.json()
    try:
        storageprice = r['results']['A']['frames'][0]['data']['values'][2][0]
    except:
        print("Error processing JSON", flush=True)
        storageprice = "no data"

    return storageprice


if __name__ == "__main__":
    get_price()
