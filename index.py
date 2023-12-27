## God bless the project

from time import sleep as sl
from random import randrange as rd
import subprocess as subp

def ind(name, user, pri):
    subp.call('cls', shell=True)
    print(" ")
    print("----- Admin Console -- Robert Hospital -----")
    print(" ")
    flag = True
    while flag:
        print("Connecting to server...")
        sl(rd(2,5))
        print(" ")
        print("------ Action Menu ------")
        print('''
1) Add Patient
2) Search Patient
3) Lab Report Generator
4) Account Profile
5) Exit Application''')
        ch = int(input("Enter index of your choice: "))
        if ch == 1:
            print(" ")
            print("Connecting to server...")
            print(" ")
            sl(rd(2,5))
            subp.call('start /wait python add.py', shell=True)
        elif ch == 2:
            print(" ")
            print("Connecting to server...")
            print(" ")            
            sl(rd(2,5))
            subp.call('python search.py', shell=True)
        elif ch == 3:
            print('Search')
        elif ch == 4:
            subp.call('python about.py', shell=True)
        elif ch == 5:
            print(" ")
            chh = input("Do you want to exit? (yes) or (no): ")
            if list(chh)[0] in ['Y', 'y']:
                print("Logging off... Please Wait...")
                sl(rd(1,8))
                print("Shutting Down...")
                sl(rd(10,20))
                quit()
            else:
                print("Returning to menu.... Please Wait for re-initialize procedure...")
                sl(rd(10, 20))