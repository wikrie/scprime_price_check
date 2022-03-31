# scprime_price_check

---

This script will get the current price from a XA-Miner and update your host SCP/TB to 0.994x of it. This is because the max change in price in a XA is 0.05, so being 0.06 below it we guarantee to be below the new price when it changes.

Thanks to @vmvelev for his help.

## Instructions for Linux

Switch to the user that has permission to change values in spd.

To install it download from the releases page and unzip in your system.

$ cd scprime_price_check

Install de virtual environment

$ python3 -m venv .venv

$ source .venv/bin/activate

Install python dependencies

$ pip install -r requeriments.txt

Edit the config.py and change base_cmd to your needs. You need to edit it to match what you would be using to launch spc outside its directory. So something like '/var/lib/spc'. Test the script.

$ python scprime_price_check.py

You will need a cronjob to execute it periodicaly. It must be the crontab of the user who launchs spd.

$ crontab -e

And add a line similar to this one, that will execute the script every 2 minutes.

*/2 * * * * systemd-cat -t "checkprice-cron" /home/daniel/scprime_price_check/.venv/bin/python /home/daniel/scprime_price_check/scprime_price_check.py

You will be able to check the journal to see it working like this

$ sudo journalctl -n100|grep checkprice-cron

---

## Instructions for Windows

- Download Python
    - Go to https://www.python.org/downloads/release/python-379/ and download the executable installer for x64 or x86
    - Install it
    - Restart the computer
- Download the repo as a zip file
    - Extract it to your SCPrime folder
    - Rename the folder (repo) to scprime_price_check
- Edit the settings
    - Open the folder
    - Edit the file config.py with notepad
    - Enter the exact directory of your spc.exe - example base_cmd = 'D:\SCPrime\spc.exe'
- Open CMD
    - Go to the folder where the script is (for example cd D:\SCPrime\scprime_price_check)
    - Type python --version. If you get Python 3.x.x everything is ok.
    - Type the command python scprime_price_check.py (If in the previous step you got Python 2.x.x you should use python3 instead in this command)
    - If you see the script running, you are good to continue
- Create a new text file
    - Name it pricechecker.bat
    - Edit it with notepad
    - The file should contain three lines if the folder is located on a drive other than C, or two lines if it is in the C drive
        - cd - the location of the folder (for example cd D:\SCPrime\scprime_price_check)
        - If the file is located on another drive (not C), you should put in the drive letter followed by : (for example D:)
        - python scprime_price_check.py You can now add this file to the task scheduler and you are good to go!

-----------------------------------------------

Donations welcome:

SCP: 29397f5ac09162c48aeea537c4950d90a6b370899a2c8054a71e82ab4954228bb63e59c56464
