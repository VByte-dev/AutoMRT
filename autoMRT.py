import datetime
import os
import pyautogui as pag
from time import sleep

os.chdir(r'C:\Users\vedhe\OneDrive\Documents')

current_datetime = datetime.datetime.now()
current_date = current_datetime.date()

with open('Scaned Records.txt', 'a') as wF:
    pass

def autoScan():
    try:
        sleep(3)
        print('[+]Program started')
        with open('Scaned Records.txt', 'r') as rF:
            rFile = rF.read()
            sFile = rFile.split()

            if str(current_date) not in sFile:
                print(f'[+]No MRT is runned on {current_date}')

                with open('Scaned Records.txt', 'a') as f:
                    file = f.write(f'{str(current_date)}\n')
                    print('[+]MRT is openning')
                    os.system('MRT.exe')

                    return
            else:
                print(f'[+]MRT is already runned on {current_date}')
                return
    except:
        print('[+]Oops something went wrong!')

scan = autoScan()