import os
import sys

def findOS():
    # read /cat/os-release for linux
    # a simple sys.platform for windows
    if 'win32' in sys.platform:
        print("Your have a windows operating system")

    f = open("/etc/os-release", "r")


findOS()