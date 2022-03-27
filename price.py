#v0.3

import requests
from requests.structures import CaseInsensitiveDict
import json


def get_price():
    url = 'https://grafana.scpri.me/api/ds/query'
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    data = json.dumps({"queries":[{"refId":"A","datasourceId":2,"rawSql":"SELECT \nto_SCP(c.used_capacity_incentives) AS incent_curr,\nto_SCP(p.used_capacity_incentives) AS incent_last,\nto_SCP(pd.storageprice*4320)*1000000000000 as \"Storage Price (SCP/TB/month)\",\nto_SCP(pd.collateral*4320)*1000000000000 as \"Collateral Price (SCP/TB/month)\",\nto_SCP(pd.maxcollateral) as \"Max Collateral (SCP/contract)\", \nto_SCP(pd.downloadbandwidthprice)*1000000000000 as \"Download Bandwith (SCP/TB)\",\nto_SCP(pd.uploadbandwidthprice)*1000000000000 as \"Upload Bandwith (SCP/TB)\",\npd.maxduration*600 as maxduration\n--to_SCP(contractprice) as \"Contract Creation Fee (SCP)\"\nFROM network.provider_details pd\njoin network.current_month_incentives c on pd.publickey = c.publickey left join network.previous_month_incentives p on c.publickey = p.publickey\nWHERE pd.publickey='f530fbf042f6f74514d0453d7d183b5f584323e4731fa061d382c0231c1a850a'","format":"table","intervalMs":10800000,"maxDataPoints":229}],"range":{"raw":{"from":"now-30d","to":"now"}}})

    r = requests.post(url, data=data, headers=headers)
    r = r.json()
    price = r['results']['A']['frames'][0]['data']['values'][2][0]
    print(f'Reference price = {price}')
    return price

if __name__ == "__main__":
    get_price()
