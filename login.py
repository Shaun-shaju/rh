from time import sleep as sl
from stdiomask import getpass as st
from random import randrange as rd
from datetime import datetime
import subprocess as subp

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
with open("assets/user.log") as f:
    lines = f.readlines()

def login():
    flag = True
    ch = input("Do you want to signup? (yes) or (no): ")
    if list(ch)[0] in ['y', 'Y']:
        print(" ")
        print("Connecting to server...")
        sl(rd(1,8))
        sign()
    elif list(ch)[0] in ['n', 'N']:
        sl(rd(1,8))
        print(" ")
        username = input("Enter username: ")
        passcode = st(prompt="Enter passcode: ", mask='*')
        print(" ")
        print("Connecting to server...")
        sl(rd(2,5))
        for a in lines:
            cred = a.split(" | ")
            pass_lt = cred[1].split('\n')
            passc = pass_lt[0]
            if cred[0] == username and passc == passcode:
                with open("assets/login.log", '+a') as f:
                    f.writelines(f'{current_time} | {username}\n')
                print("Access Granted...")   
                print(" ")
                sl(rd(2,5))
                subp.call('start /wait python app.py', shell=True)
            if lines[-1] == a and cred[0] != username and passc != passcode:
                flag = False
        if flag == False:
            print("Access Denied... Please try again later...")
    else:
        print("Unknown parameter found... Exiting...")
        sl(rd(1,8))
        quit()

def sign():    
    name = input("Enter your full name: ")
    if name != '':
        email = input("Enter email address (Optional): ")
        priv = input("Enter account privilege (Admin) or (Standard): ")
        if list(priv)[0] in ['A', 'a', 'S', 's']:
            phone = input("Enter phone number: ")
            if phone.isdigit():
                username = input("Enter username: ")
                passcode = st(prompt="Enter passcode: ", mask='^')
                with open("assets/user.log", '+a') as f:
                    f.writelines(f'{username} | {passcode}\n')
                with open("assets/about.log", '+a') as f:
                    f.writelines(f'{username} | {name} | {email} | {phone} | {priv}')
                print("Connecting to server...")
                sl(rd(2,5))
                print("Restarting program...")
            else:
                print("Invalid phone number found... (Don't add any other extentions other than the number.)")
        else:
            print("Invalid privilege parameter found... Type (Admin) or (Standard)... Please Try again...")
    else:
        print("Invalid Name found... Please Try again...")
if lines == []:
    print("Do you want to add an admin to database?")
    ch = input("Enter (yes) or (no): ")
    if list(ch)[0] in ['Y', 'y']:
        print("Connecting to server...")
        sl(rd(2,5))
        sign()
    elif list(ch)[0] in ['N', 'n']:
        print("Connection to server...")
        sl(rd(1,8))
        print("No users found in the database... Exiting Program...")
        sl(rd(2,5))
        quit()
    else:
        print("Unknown Parameter found... Exiting Program...")
        sl(rd(1,8))
        quit()
else:
    print("Connecting to server...")
    sl(rd(2,5))
    login()