# Python 3
# Author: Samuel Anyaele - TheMobileprof.com
# scripts/help/modules/misc.py

import os
from urllib.request import urlopen

def internet_on():
    try:
        response = urlopen('https://github.com/', timeout=10)
        return True
    except:
        return False

def current_dir():
    # Get current directory
    home_dir = os.path.expanduser("~")
    current_dir = os.getcwd()           
    return "~/" + os.path.relpath(current_dir,home_dir)
