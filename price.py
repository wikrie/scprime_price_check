#v0.2

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


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
    get_price()
