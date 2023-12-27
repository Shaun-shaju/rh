from time import sleep as sl
from random import randrange as rd

print(" ")
print("------ Robert Hospital -- Patient Registration ------")
print(" ")

with open("assets/about.log") as f:
    lines = f.readlines()   
with open("assets/login.log") as k:
    line = k.readlines()
lt = line[-1].split(" | ")
user = lt[-1]
user_lt = user.split("\n")
user = ''
user += user_lt[0]
pri = ''
for a in lines:
    cred = a.split(" | ")
    if cred[0] == user:
        pri += str(cred[4])
    else:
        pass

def write(text):
    with open("assets/patients.log", '+a') as k:
        k.writelines(str(text))
def wr_ab(tt):
    if lines == []:
        txt = f'rh1'
        path = f'assets/patient_record/{txt}'
        with open(path, 'w') as k:
            k.writelines(str(tt))
    else:
        elem = lines[-1]
        lt = elem.split(" | ")
        ol_id = lt[0]
        lt_id = ''
        for a in ol_id:
            if a.isdigit():
                lt_id += str(a)
            else:
                pass
        id = (int(lt_id)+1)
        txt = f'rh{id}'
        path = f'assets/patient_record/{txt}'
        with open(path, 'w') as k:
            k.writelines(str(tt))

with open("assets/patients.log") as f:
    lines = f.readlines()
if lines == []:
    if list(pri)[0] in ['A', 'a']:
        na = input("Enter patient name: ")
        age = input("Enter patient age: ")
        gen = input("Enter patient gender: ")
        pho = int(input("Enter patient phonenumber: "))
        address = input("Enter patient address: ")
        txt = f'rh1 | {na}'
        write(str(txt + '\n'))
        wr_ab(str(f'rh1 | {na} | {age} | {gen} | {pho} | {address}\n'))
    else:
        print("Permission Denied... Please login in a Admin account...")
else:
    if list(pri)[0] in ['A', 'a']:
        na = input("Enter patient name: ")
        age = input("Enter patient age: ")
        gen = input("Enter patient gender: ")
        pho = int(input("Enter patient phonenumber: "))
        address = input("Enter patient address: ")
        lt = lines[-1].split(" | ")
        ol_id = lt[0]
        lt_id = ''
        for a in ol_id:
            if a.isdigit():
                lt_id += str(a)
            else:
                pass
        id = (int(lt_id)+1)
        txt = f'rh{id} | {na}'
        write(str(txt + '\n'))
        wr_ab(str(f'{id} | {na} | {age} | {gen} | {pho} | {address}\n'))
    else:
        print("Permission Denied... Please login in a Admin account...")