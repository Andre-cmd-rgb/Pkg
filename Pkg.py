from importlib.resources import Package
import os

while True:
    code = input(">")
    if code == 'pkg install Python':
        os.system("Download.py https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe")
    