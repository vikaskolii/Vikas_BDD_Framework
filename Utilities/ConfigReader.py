from configparser import ConfigParser

# This function is used to get data from the config.ini file
# You need to pass 2 parameters:
# 1. category (section name)
# 2.  key (the value name inside that section)

def read_configuration(category,key):
   cp=ConfigParser()
   cp.read("Configurations/config.ini")
   return cp.get(category,key)

