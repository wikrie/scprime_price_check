#v0.5

import os

class Config(object):
    # the first part of the command you use to call spc
    base_cmd = 'docker exec scprime02 spc'

    provider_primary = 'f530fbf042f6f74514d0453d7d183b5f584323e4731fa061d382c0231c1a850a'
    provider_secondary = '8613f76f986eeac0df9a6066cd597a2b11207be3c2a81de49d8a9b7f40b78b73'
    #This provider was offline when testing the script. Usefull to check the fail logic.
    #provider_primary = 'ea6d43fbe5b092d32fa15b7be2ab8e8f93eb713479ee00ad3b7a7c22be13fafc'
    #provider_secondary = 'ea6d43fbe5b092d32fa15b7be2ab8e8f93eb713479ee00ad3b7a7c22be13fafc'
    