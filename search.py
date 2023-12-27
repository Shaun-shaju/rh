from time import sleep as sl
from random import randrange as rd

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

if list(pri)[0] in ['A', 'a']:
    with open("assets/patients.log") as f:
        lines = f.readlines()

    if lines == []:
        print("No patient record found in the database... Please add a new one to view...")
    else:
        print('''Search way:
            1) Search by record number
            2) Search by name''')
        ch = input("Enter your choice index: ")
        if ch == '1':
            rec_no = input("Enter record number (rhxxx): ")
            flag = False
            for a in lines:
                lt = a.split(" | ")
                if lt[0] == rec_no:
                    print("Patient found...")
                    sl(rd(1,8))
                    flag = True
                    break
            else:
                print("Patient not found.... Try adding the patient to the database...")
            if flag:
                path = f'assets/patient_record/{rec_no}'
                with open(path) as k:
                    lt_info = k.readlines()
                info = lt_info[0].split(" | ")
                print(f'''
---- Robert Hospital -- Patients Record ----
                      
    Patient Record No.: {rec_no}
    Patient Name: {info[1]}
    Patient Age: {info[2]}
    Patient Gender: {info[3]}
    Patient Phone Number: {info[4]}
    Patient Address: {info[5]}''')
            else:
                pass
        elif ch == '2':
            name = input("Enter patient name: ")
            sl(rd(1,8))
            for a in lines:
                na = a.split(" | ")
                na_lt = na[1].split("\n")
                na = ''
                na += na_lt[0]
                if na == name:
                    lt = a.split(' | ')
                    rec_no = lt[0]
                    path = f'assets/patient_record/{rec_no}'
                    with open(path) as k:
                        lt_info = k.readlines()
                    info = lt_info[0].split(" | ")
                    print(f'''
---- Robert Hospital -- Patients Record ----
                          
    Patient Record No.: {rec_no}
    Patient Name: {na}
    Patient Age: {info[2]}
    Patient Gender: {info[3]}
    Patient Phone Number: {info[4]}
    Patient Address: {info[5]}''')
                else:
                    pass
        else:
            print("Option not found... Exiting...")
            sl(rd(1,8))
else:
    print("Permission Denied... Please login in a Admin account...")