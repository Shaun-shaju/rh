import subprocess
from time import sleep as sl
from random import randrange as rd

print(" ")
print("Welcome to Robert Hospital -- Server Access")
print(" ")
print("Connecting to server...")
sl(rd(1,8))
print("Connected...")
sl(rd(2,5))
subprocess.call('start /wait python login.py', shell=True)