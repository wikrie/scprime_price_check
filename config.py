import os

class Config(object):
    # Update this values to your preferences
    # $/TB
    target_price = 3.5
    # difference must be greater than this % to change the price
    tolerance = 0.5
    # the first part of the command you use to call spc
    base_cmd = 'docker exec scprime02 spc'
