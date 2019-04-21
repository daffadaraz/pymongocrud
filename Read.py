import pymongo,pprint,os
from pymongo import MongoClient
from time import sleep
client = MongoClient()
db = client["Data-Mahasiswa"]
collection = db["Data"]
datas = db.Data

pilihanr = 0
ulangr = "Y"

while ulangr == "y" or ulangr == "Y":
    while pilihanr < 1 or pilihanr > 6:
        os.system('clear')

        print('     Mencari Data')
        print('1. Tampilkan Seluruh data')
        print('2. Cari berdasarkan NPM')
        print('3. Cari berdasarkan Nama')
        print('4. Cari berdasarkan kelas')
        print('5. Cari berdasarkan Jurusan')
        print('6. Back to main menu')
        pilihanr = int(input('Input : '))

        if pilihanr < 1 or pilihanr > 6:
            print()
            print('Input Salah')
            sleep(.5)

        data = 1
        a = 0
        datab = 0

        if pilihanr == 1: #All
            os.system('clear')
            for data in datas.find():
                print()
                a = a + 1
                print('Data ke -',a)
                pprint.pprint(data)
            print()
            print('banyak nya data = ',a)

        elif pilihanr == 2: #NPM
            os.system('clear')
            print('Mencari berdasarkan NPM')
            pil1 = str(input('NPM : '))
            print()
            for data in datas.find({"_id":pil1}):
                a = a +1
                pprint.pprint(data)
                print()

            if a == 0:
                print(pil1,', Tidak Ditemukan')
                break
            else:
                print('Data Ditemukan.')
                print('Banyak nya data : ',a)

        elif pilihanr == 3: #Nama
            os.system('clear')
            print('Mencari berdasarkan Nama')
            pil1 = str(input('Nama : '))
            print()
            for data in datas.find({"nama":pil1}):
                a = a + 1
                print('Data ke -',a)
                pprint.pprint(data)
                print()
            if a == 0:
                print(pil1,', Tidak Ditemukan')
                break
            else:
                print('Data Ditemukan.')
                print('Banyak nya data : ',a)

        elif pilihanr == 4: #Kelas
            os.system('clear')

            for data in datas.find({},{"kelas":1,"_id":0}): #List Kelas
                if data != datab:
                    pprint.pprint(data)
                    datab = data

            print('Mencari berdasarkan Kelas')
            pil1 = str(input('Kelas : '))
            print()
            for data in datas.find({"kelas":pil1}):
                a = a + 1
                print('Data ke -',a)
                pprint.pprint(data)
                print()

            if a == 0:
                print(pil1,', Tidak Ditemukan')
                break
            else:
                print('Data Ditemukan.')
                print('Banyak nya data : ',a)        

        elif pilihanr == 5: #Jurusan
            os.system('clear')
            print('Mencari berdasarkan Jurusan')

            for data in datas.find({},{"jurusan":1,"_id":0}): #List Jurusan
                if data != datab:
                    pprint.pprint(data)
                    datab = data
            pil1 = str(input('Jurusan : '))
            print()
            for data in datas.find({"jurusan":pil1}):
                a = a + 1
                print('Data ke -',a)
                pprint.pprint(data)
                print()
            if a == 0:
                print(pil1,', Tidak Ditemukan')
            else:
                print('Data Ditemukan.')
                print('Banyak nya data : ',a)

        elif pilihanr == 6: #Exit
            exec(open("Menu.py").read())
    
    pilihanr = 0

    print()
    print('Ingin  mencari lagi?')
    ulangr = str(input('  (y/n): '))
exec(open("Menu.py").read())