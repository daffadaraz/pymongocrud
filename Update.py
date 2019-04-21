import pymongo,pprint,os,datetime
from pymongo import MongoClient
from time import sleep
client = MongoClient()
db = client["Data-Mahasiswa"]
collection = db["Data"]
datas = db.Data

ulangu = 'y'
pilihanu = 0

while ulangu == 'y' or ulangu == 'Y':
    while pilihanu < 1 or pilihanu > 5:
        os.system('clear')
        data = 0
        a = 0

        print('     Mengubah Data')
        print('1. Mengubah Seluruh data')
        print('2. Mengubah Nama')
        print('3. Mengubah kelas')
        print('4. Mengubah Jurusan')
        print('5. Kembali ke menu')
        pilihanu = int(input('Input : '))

        if pilihanu < 1 or pilihanu > 5:
            print()
            print('Input Salah')
            sleep(.5)

        if pilihanu == 1: #Seluruh
            os.system('clear')
            print('Masukkan NPM yang akan diganti datanya.')
            npm = input('NPM = ')

            for data in datas.find({"_id":npm}):
                a = a + 1
            if a == 0:
                    print()
                    print(npm,', Tidak Ditemukan')
                    break

            print()
            print('Masukkan Data baru')
            print()
            nama =  input('Masukkan Nama    : ')
            kelas=  input('Masukkan Kelas   : ')
            jurusan=input('Masukkan Jurusan : ')
            
            datas.update_one({"_id":npm}, {"$set": {"nama" : nama,"kelas" : kelas,"jurusan": jurusan,"lastMod": datetime.datetime.now()}})

            print()
            for data in datas.find({"_id":npm}):
                pprint.pprint(data)
                print()

            print('Data telah terubah.')
            print('Note : NPM Tidak dapat diubah.')

        elif pilihanu == 2: #Nama
            os.system('clear')
            print('Masukkan NPM yang akan diganti nama nya.')
            npm = input('NPM = ')

            for data in datas.find({"_id":npm}):
                a = a + 1
            if a == 0:
                    print()
                    print(npm,', Tidak Ditemukan')
                    break
            print()
            nama = input('Masukkan nama baru = ')

            datas.update_one({"_id":npm}, {"$set": {"nama" : nama,"lastMod": datetime.datetime.now()}})
            
            print()
            for data in datas.find({"_id":npm}):
                pprint.pprint(data)
                print()
                print('Data telah terubah.')

        elif pilihanu == 3: #Kelas
            os.system('clear')
            print('Masukkan NPM yang akan diganti Kelas nya.')
            npm = input('NPM = ')

            for data in datas.find({"_id":npm}):
                a = a + 1
            if a == 0:
                    print()
                    print(npm,', Tidak Ditemukan')
                    break

            print()
            nama = input('Masukkan Kelas baru = ')

            datas.update_one({"_id":npm}, {"$set": {"kelas" : nama,"lastMod": datetime.datetime.now()}})
            
            print()
            for data in datas.find({"_id":npm}):
                pprint.pprint(data)
                print()
                print('Data telah terubah.')
        
        elif pilihanu == 4: #Jurusan
            os.system('clear')
            print('Masukkan NPM yang akan diganti Jurusan nya.')
            npm = input('NPM = ')

            for data in datas.find({"_id":npm}):
                a = a + 1
            if a == 0:
                    print()
                    print(npm,', Tidak Ditemukan')
                    break

            print()
            nama = input('Masukkan jurusan baru = ')

            datas.update_one({"_id":npm}, {"$set": {"jurusan" : nama,"lastMod": datetime.datetime.now()}})
            
            print()
            for data in datas.find({"_id":npm}):
                pprint.pprint(data)
                print()
                print('Data telah terubah.')

        elif pilihanu == 5: #Exit
            os.system('clear')
            exec(open("Menu.py").read())

    pilihanu = 0

    print()
    print('Ingin mengubah lagi?')
    ulangu = str(input('  (y/n): '))

exec(open("Menu.py").read())