import os
import sys

def main():
    # read /cat/os-release for linux
    # a simple sys.platform for windows
    if 'win32' in sys.platform:
        print("Your have a Windows operating system and that's all I know for now.")

    f = open("/etc/os-release", "r")
    if f.mode == "r":
        contents = f.readlines()
        print(contents[0].strip())


if __name__ == "__main__":
    main()