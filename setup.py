import sys
import os

print("Installing the python modules required for the ShadowNuker Tool:")
if sys.platform.startswith("win"):
    "WINDOWS"
    os.system("pip install --upgrade pip")
    os.system("pip install --upgrade pip setuptools wheel")
    os.system("pip install dnspython")
    os.system("pip install time")
    os.system("pip install selenium")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install json")
    os.system("pip install random")
    os.system("pip install string")
    os.system("pip install ctypes")
    os.system("pip install base64")
    os.system("pip install threading")
    os.system("pip install psutil")
    os.system("pip install bs4")
    os.system("pip install webbrowser")
    os.system("pip install itertools")
    os.system("pip install phonenumbers")
    os.system("pip install discord")
    os.system("pip install discord.py")
    os.system("pip install PyQt5")
    os.system("pip install PyQtWebEngine")
    os.system("pip install pytube")
    os.system("pip install cryptography")
    os.system("pip install pycryptodome")
    os.system("pip install pywin32")
    print("Finish.")
    os.system("python ShadowNuker.py")

elif sys.platform.startswith("linux"):
    "LINUX"
    os.system("pip3 install --upgrade pip")
    os.system("pip3 install --upgrade pip setuptools wheel")
    os.system("pip3 install dnspython")
    os.system("pip3 install time")
    os.system("pip3 install selenium")
    os.system("pip3 install colorama")
    os.system("pip3 install requests")
    os.system("pip3 install json")
    os.system("pip3 install random")
    os.system("pip3 install string")
    os.system("pip3 install ctypes")
    os.system("pip3 install base64")
    os.system("pip3 install threading")
    os.system("pip3 install psutil")
    os.system("pip3 install bs4")
    os.system("pip3 install webbrowser")
    os.system("pip3 install itertools")
    os.system("pip3 install phonenumbers")
    os.system("pip3 install discord")
    os.system("pip3 install discord.py")
    os.system("pip3 install PyQt5")
    os.system("pip3 install PyQtWebEngine")
    os.system("pip3 install pytube")
    os.system("pip3 install cryptography")
    os.system("pip3 install pycryptodome")
    os.system("pip3 install pywin32")
    print("Finish.")
    os.system("python3 ShadowNuker.py")
