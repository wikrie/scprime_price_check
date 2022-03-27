#v0.2

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import requests
from requests.structures import CaseInsensitiveDict


def get_price2():
    url = 'https://grafana.scpri.me/api/ds/query'
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    data = """{"queries":[{"refId":"A","datasourceId":2,"rawSql":"SELECT \nto_SCP(c.used_capacity_incentives) AS incent_curr,\nto_SCP(p.used_capacity_incentives) AS incent_last,\nto_SCP(pd.storageprice*4320)*1000000000000 as \"Storage Price (SCP/TB/month)\",\nto_SCP(pd.collateral*4320)*1000000000000 as \"Collateral Price (SCP/TB/month)\",\nto_SCP(pd.maxcollateral) as \"Max Collateral (SCP/contract)\", \nto_SCP(pd.downloadbandwidthprice)*1000000000000 as \"Download Bandwith (SCP/TB)\",\nto_SCP(pd.uploadbandwidthprice)*1000000000000 as \"Upload Bandwith (SCP/TB)\",\npd.maxduration*600 as maxduration\n--to_SCP(contractprice) as \"Contract Creation Fee (SCP)\"\nFROM network.provider_details pd\njoin network.current_month_incentives c on pd.publickey = c.publickey left join network.previous_month_incentives p on c.publickey = p.publickey\nWHERE pd.publickey='f530fbf042f6f74514d0453d7d183b5f584323e4731fa061d382c0231c1a850a'","format":"table","intervalMs":10800000,"maxDataPoints":229}],"range":{"from":"2022-02-25T08:47:28.504Z","to":"2022-03-27T07:47:28.504Z","raw":{"from":"now-30d","to":"now"}},"from":"1645778848504","to":"1648367248504"}"""

    r = requests.post(url, data=data, headers=headers)
    print(r, r.text)

def get_price():
    url = 'https://grafana.scpri.me/d/Cg7V28sMk/provider-detail?var-provider=f530fbf042f6f74514d0453d7d183b5f584323e4731fa061d382c0231c1a850a&kiosk=tv&orgId=1'
    xpath = '/html/body/div[1]/div/div/div[3]/div[2]/div/div[1]/div/div/div[5]/div/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/span[1]'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    service = Service('/usr/bin/chromedriver')

    with webdriver.Chrome(options=options, service=service) as driver:
        driver.get(url)
        sleep(5)
        n = 0
        while n < 5:
            try:
                price = driver.find_element(by=By.XPATH, value=xpath).text
                print(f'Reference price = {price}')
                return price
            except NoSuchElementException:
                print(f'Grafana page not loaded')
                n += 1
                sleep(5)
    print(f'Tried 5 times without luck')
    return 'no data'

if __name__ == "__main__":
    get_price2()
