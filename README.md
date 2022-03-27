# scprime_price_check

---

This script will get the current price from a XA-Miner and update your host SCP/TB to 0.994x of it. This is because the max change in price in a XA is 0.05, so being 0.06 below it we guarantee to be below the price when it changes.

## Instructions for Linux

To install it donwload from the releases page and unzip in your system.

$ cd scprime_price_check

Install de virtual environment

$ python3 -m venv .venv

$ source .venv/bin/activate

Install python dependencies

$ pip install -r requeriments.txt

Install system requirements

$ sudo apt-get install chromium-chromedriver

Edit the config.py and change base_cmd to your needs. You need to edit it to match what you would be using to launch spc outside its directory. So something like '/var/lib/spc'.

Switch to the user that has permission to change values in spd and test it.

$ python scprime_price_check.py

You will need a cronjob to execute it periodicaly.

$ crontab -e

And add a line similar to this one, that will execute the script every 2 minutes.

*/2 * * * * systemd-cat -t "checkprice-cron" /home/daniel/scprime_price_check/.venv/bin/python /home/daniel/scprime_price_check/scprime_price_check.py

You will be able to check the journal to see it working like this

$ sudo journalctl -n1000|grep checkprice-cron

---

## Instructions for Windows

This release does not work in windows.

-----------------------------------------------

Donations welcome:

SCP: 29397f5ac09162c48aeea537c4950d90a6b370899a2c8054a71e82ab4954228bb63e59c56464
