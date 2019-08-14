import os
import sys

def main():
    # read /cat/os-release for linux
    # a simple sys.platform for windows
    os_name_full = ""
    if 'win32' in sys.platform:
        print("Your have a Windows operating system and that's all I know for now.")

    f = open("/etc/os-release", "r")
    if f.mode == "r":
        contents = f.readlines()
        for line in contents:
            if "PRETTY_NAME" in line:
                os_name_full = line
        print("Your Operating System is: " + os_name_full.split("=")[1])


if __name__ == "__main__":
    main()