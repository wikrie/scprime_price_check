# scprime_price_check

This script will get the price of SCP and update SCP/TB to a target price, defined in the script, if the difference is greater than a percentage also defined in the script.

To install it you need to clone the repository to your system, create the venv, activate it and install the dependencies.

Then edit thescprime_price_check.py and edit the target price, the tolerance ans base_cmd to your needs. I am using 3.9, 0.5. As we tril the xa-miners, if you use a value to close to the standard 4.0$, some scans you will be above the limit, so better to lose some rent than to lose the incentives.

You need to edit the base_cmd to what you would be using to launch spc outside its directory. So something like '/var/lib/spc'. This is am example as I use docker.

If you are using Windows, this article will help you to setup your environment https://programwithus.com/learn/python/pip-virtualenv-windows

Donations welcome:

SCP: 29397f5ac09162c48aeea537c4950d90a6b370899a2c8054a71e82ab4954228bb63e59c56464
