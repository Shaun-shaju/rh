from time import sleep as sl
from stdiomask import getpass as st
from random import randrange as rd
from datetime import datetime
import subprocess as subp

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
with open("assets/about.log") as f:
    lines = f.readlines()
with open("assets/user.log") as f:
    line = f.readlines() 
with open("assets/login.log") as f:
    li = f.readlines() 
lt = li[-1].split(" | ")
user = lt[-1]
user_lt = user.split("\n")
user = ''
user += user_lt[0]
pri = ''
name = ''
email = ''
phone = ''
for a in lines:
    cred = a.split(" | ")
    if cred[0] == user:
        name += str(cred[1])
        email += str(cred[2])
        phone += str(cred[3])
        pri += str(cred[4])
    else:
        pass
print(f"Authentication Needed for the account: {user}")
print(" ")
flag = False
username = user
passcode = st(prompt="Enter passcode: ", mask='*')
print(" ")
print("Connecting to server...")
sl(rd(2,5))
for a in line:
    cred = a.split(" | ")
    pass_lt = cred[1].split('\n')
    passc = pass_lt[0]
    if passc == passcode:
        print("Access Granted...")   
        print(" ")
        sl(rd(2,5))
        break
    else:
        flag = True
if flag == True:
    print("Access Denied... Please try again later...")
    quit()
print(f'''
---- Robert Hospital -- Admin User Profile ----
                      
    Profile Username: {user}
    Profile Name: {name}
    Profile Email: {email}
    Profile Phone Number: {phone}
    Profile Privilege: {pri}''')

print(" ")
print('''Account Settings
      1) Change username
      2) Change name
      3) Change email
      4) Change phone number
      5) Change account privilege      
      6) Add Account from database
      7) Delete Account from database
      8) Return to main menu''')
ch = input("Enter your choice index: ")
if ch == '1':
    print(" ")
    print("Initialzing...")
    sl(rd(1,8))
    print(" ")
    na = input("Enter existing username: ")
    na_user = input("Enter new username: ")
    if na == user:
        if na != na_user:
            with open("assets/about.log", 'r') as f:
                data = f.read()
                data = data.replace(na, na_user)
            with open("assets/about.log", 'w') as f:
                f.write(data)
            with open("assets/user.log", 'r') as f:
                data = f.read()
                data = data.replace(na, na_user)
            with open("assets/user.log", 'w') as f:
                f.write(data)
            with open("assets/login.log", 'r') as f:
                data = f.read()
                data = data.replace(na, na_user)
            with open("assets/login.log", 'w') as f:
                f.write(data)
            print("")
            print("Writing changes to database... Please wait...")
            sl(rd(1,8))
            print("Completed...")
            print(" ")
        else:
            print("The existing and the new username are exactly the same... Exiting...")
            print(" ")
            sl(rd(1,8))
    else:
        print("Looks like you're changing the username of another user...")
        chh = input("Do you want to continue? (yes) or (no): ")
        if list(chh)[0] in ['y', 'Y']:
            passc = st(prompt= f"Enter {na} account passphrase to continue: ", mask='*')
            for a in lines:
                user_cred = a.split(' | ')                
                pass_lt = user_cred[1].split('\n')
                passc = pass_lt[0]
                if user_cred[0] == na and pass_lt[0] == passc:
                    print("Changing Username...")
                    with open("assets/about.log", 'r') as f:
                        data = f.read()
                        data = data.replace(na, na_user)
                    with open("assets/about.log", 'w') as f:
                        f.write(data)
                    with open("assets/user.log", 'r') as f:
                        data = f.read()
                        data = data.replace(na, na_user)
                    with open("assets/user.log", 'w') as f:
                        f.write(data)
                    with open("assets/login.log", 'r') as f:
                        data = f.read()
                        data = data.replace(na, na_user)
                    with open("assets/login.log", 'w') as f:
                        f.write(data)
                    print("")
                    print("Writing changes to database... Please wait...")
                    sl(rd(1,8))
                    print("Completed...")
                    print(" ")
                    break
                else:
                    pass
            else:                
                print("You are not authorized to change the username of this account...")
                print(" ")
                sl(rd(1,8)) 
        elif list(chh)[0] in ['n', 'N']:
            print("Returning to menu...")
            sl(rd(1,8))
        else:
            print("Unknown parameter found... Returning to menu...")
            sl(rd(1,8))
elif ch == '2':
    print(" ")
    print("Initialzing...")
    sl(rd(1,8))
    print(" ")
    na = input("Enter existing name: ")
    us_na = input("Enter associated username: ")
    na_user = input("Enter new name: ")
    if na == name:
        if na != na_user:
            with open("assets/about.log", 'r') as f:
                data = f.read()
                data = data.replace(na, na_user)
            with open("assets/about.log", 'w') as f:
                f.write(data)
            print("")
            print("Writing changes to database... Please wait...")
            sl(rd(1,8))
            print("Completed...")
            print(" ")
        else:
            print("The existing and the new name are exactly the same... Exiting...")
            print(" ")
            sl(rd(1,8))
    else:
        print("Looks like you're changing the name of another user...")
        chh = input("Do you want to continue? (yes) or (no): ")
        if list(chh)[0] in ['y', 'Y']:
            passc = st(prompt= f"Enter {na} account passphrase to continue: ", mask='*')
            for a in lines:
                user_cred = a.split(' | ')                
                pass_lt = user_cred[1].split('\n')
                passc = pass_lt[0]
                if user_cred[0] == us_na and pass_lt[0] == passc:
                    print("Changing Username...")
                    with open("assets/about.log", 'r') as f:
                        data = f.read()
                        data = data.replace(na, na_user)
                    with open("assets/about.log", 'w') as f:
                        f.write(data)
                    with open("assets/user.log", 'r') as f:
                        data = f.read()
                        data = data.replace(na, na_user)
                    with open("assets/user.log", 'w') as f:
                        f.write(data)
                    with open("assets/login.log", 'r') as f:
                        data = f.read()
                        data = data.replace(na, na_user)
                    with open("assets/login.log", 'w') as f:
                        f.write(data)
                    print("")
                    print("Writing changes to database... Please wait...")
                    sl(rd(1,8))
                    print("Completed...")
                    print(" ")
                    break
                else:
                    pass
            else:                
                print("You are not authorized to change the username of this account...")
                print(" ")
                sl(rd(1,8)) 
        elif list(chh)[0] in ['n', 'N']:
            print("Returning to menu...")
            sl(rd(1,8))
        else:
            print("Unknown parameter found... Returning to menu...")
            sl(rd(1,8))
elif ch == '3':
    print(" ")
    print("Initialzing...")
    sl(rd(1,8))
    print(" ")
    na = input("Enter existing email: ")
    us_na = input("Enter associated username: ")
    na_user = input("Enter new email: ")
    if na == email:
        if na != na_user:
            with open("assets/about.log", 'r') as f:
                data = f.read()
                data = data.replace(na, na_user)
            with open("assets/about.log", 'w') as f:
                f.write(data)
            print("")
            print("Writing changes to database... Please wait...")
            sl(rd(1,8))
            print("Completed...")
            print(" ")
        else:
            print("The existing and the new name are exactly the same... Exiting...")
            print(" ")
            sl(rd(1,8))
    else:
        print("Looks like you're changing the name of another user...")
        chh = input("Do you want to continue? (yes) or (no): ")
        if list(chh)[0] in ['y', 'Y']:
            passc = st(prompt= f"Enter {na} account passphrase to continue: ", mask='*')
            for a in lines:
                user_cred = a.split(' | ')                
                pass_lt = user_cred[1].split('\n')
                passc = pass_lt[0]
                if user_cred[0] == us_na and pass_lt[0] == passc:
                    print("Changing Username...")
                    with open("assets/about.log", 'r') as f:
                        data = f.read()
                        data = data.replace(na, na_user)
                    with open("assets/about.log", 'w') as f:
                        f.write(data)
                    print("")
                    print("Writing changes to database... Please wait...")
                    sl(rd(1,8))
                    print("Completed...")
                    print(" ")
                    break
                else:
                    pass
            else:                
                print("You are not authorized to change the username of this account...")
                print(" ")
                sl(rd(1,8)) 
        elif list(chh)[0] in ['n', 'N']:
            print("Returning to menu...")
            sl(rd(1,8))
        else:
            print("Unknown parameter found... Returning to menu...")
            sl(rd(1,8))
if ch == '4':
    print("phone")
if ch == '5':
    print("priv")
if ch == '6':
    print("delete")