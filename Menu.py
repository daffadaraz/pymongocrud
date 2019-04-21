import os,sys
from time import sleep

pilihanm = 0
while pilihanm < 1 or pilihanm > 5:
    os.system('clear')

    print(' MongoDB menggunakan Python')
    print('---------Menu Utama--------')
    print('1. Create')
    print('2. Read')
    print('3. Update')
    print('4. Delete')
    print('5. Exit')
    pilihanm = int(input('Input : '))

    if pilihanm < 1 or pilihanm > 5:
        print()
        print('Input Salah')
        sleep(.5)

    if pilihanm == 1:
        exec(open("Create.py").read())
    elif pilihanm == 2:
        exec(open("Read.py").read())
    elif pilihanm == 3:
        exec(open("Update.py").read())
    elif pilihanm == 4:
        exec(open("Delete.py").read())
    elif pilihanm == 5:
        print()
        print('Bye :)')
        sys.exit()