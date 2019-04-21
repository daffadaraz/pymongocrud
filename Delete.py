import pymongo,pprint,os,datetime
from pymongo import MongoClient
from time import sleep
client = MongoClient()
db = client["Data-Mahasiswa"]
collection = db["Data"]
datas = db.Data

password = "daffa"

ulangd = 'y'
pilihand = 0

while ulangd == 'y' or ulangd =='Y':
    while pilihand <1 or pilihand >5:
        os.system('clear')
        
        data = 0
        datab = 0
        a = 0

        print('     Menghapus Data')
        print('1. Menghapus 1 data berdasarkan NPM')
        print('2. Menghapus data 1 Kelas')
        print('3. Menghapus data 1 Jurusan')
        print('4. EXIT')
        print()
        print('5. Menghapus seluruh data pada db (WARNING)')
        print()
        pilihand = int(input('Input : '))

        if pilihand < 1 or pilihand > 5:
            print()
            print('Input Salah')
            sleep(.5)
        
        if pilihand == 1: #1 Data
            os.system('clear')
            print('Masukkan NPM yang akan di hapus datanya : ')
            npm = input('NPM = ')

            print()
            for data in datas.find({"_id":npm}):
                a = a + 1
                pprint.pprint(data)
                print()

            if a == 0:
                print(npm,', Tidak Ditemukan')
                break
            
            print('Apakah kamu yakin?')
            choice = input('(y/n) : ')
            print()

            if choice == 'y' or choice == 'Y':
                datas.delete_one({"_id":npm})
                print('Data telah terhapus.')
            else:
                print()
                print('Batal.')
                sleep(.5)

        elif pilihand == 2: #Kelas
            os.system('clear')
            
            for data in datas.find({},{"kelas":1,"_id":0}): #List Kelas
                if data != datab:
                    pprint.pprint(data)
                    datab = data
            
            print()
            print('Masukkan Kelas yang akan di hapus datanya : ')
            kelas = input('Kelas = ')

            print()
            for data in datas.find({"kelas":kelas}):
                a = a + 1
                print('Data ke -',a)
                pprint.pprint(data)
                print()

            if a == 0:
                print(kelas,', Tidak Ditemukan')
                break

            print('Banyak data yg akan di hapus : ',a)
            
            print()
            checkpass = input('Masukkan Password : ')
            print()

            if checkpass == password: 
                print('Password benar.')
                print()
                print('Apakah kamu yakin?')
                choice = input('(y/n) : ')
                print()

                if choice == 'y' or choice == 'Y':
                    datas.delete_many({"kelas":kelas})
                    print('Data telah terhapus.')
                    print('Banyak data yg di hapus : ',a)
                else:
                    print()
                    print('Batal.')
                    sleep(.5)
            else:
                print('Proses dibatalkan.')
                print(' Password salah')
                sleep(.5)

        elif pilihand == 3: #Jurusan
            os.system('clear')

            for data in datas.find({},{"jurusan":1,"_id":0}): #List Jurusan
                if data != datab:
                    pprint.pprint(data)
                    datab = data
            
            print()
            print('Masukkan Jurusan yang akan di hapus datanya : ')
            jurusan = input('Jurusan = ')

            print()
            for data in datas.find({"jurusan":jurusan}):
                a = a + 1
                print('Data ke -',a)
                pprint.pprint(data)
                print()

            if a == 0:
                print(jurusan,', Tidak Ditemukan')
                break
        
            print('Banyak data yg akan di hapus : ',a)
            
            print()
            checkpass = input('Masukkan Password : ')
            print()

            if checkpass == password:
                print('Password benar.')
                print() 
                print('Apakah kamu yakin?')
                choice = input('(y/n) : ')
                print()

                if choice == 'y' or choice == 'Y':
                    datas.delete_many({"jurusan":jurusan})
                    print('Data telah terhapus.')
                    print('Banyak data yg di hapus : ',a)
                    sleep(.5)
                else:
                    print()
                    print('Batal.')
                    sleep(.5)
            else:
                print('Proses dibatalkan.')
                print(' Password salah')
                sleep(.5)

        elif pilihand == 4: #Exit
            os.system('clear')
            exec(open("Menu.py").read())

        elif pilihand == 5: #All
            os.system('clear')
            
            for data in datas.find():
                a = a + 1
                print('Data ke -',a)
                pprint.pprint(data)
                print()
            print('Banyak data yg akan di hapus : ',a)

            print()
            checkpass = input('Masukkan Password : ')
            print()

            if checkpass == password:
                print('Password benar.')
                print() 
                print('Apakah kamu yakin?')
                choice = input('(y/n) : ')
                print()
                print('Apakah kamu sangat yakin?')
                print('Banyak data yg akan di hapus : ',a)
                choice2 = input('(y/n) : ')
                print()

                if choice == 'y' and choice2 == 'y': 

                        print('Database telah terhapus.')
                        print('Banyak data yg di hapus : ',a)
                        sleep(.5)
                else:
                    print()
                    print('Batal.')
                    sleep(.5)
            else:
                print('Proses dibatalkan.')
                print(' Password salah')
                sleep(.5)
    pilihand = 0

    print()
    print('Ingin menghapus lagi?')
    ulangd = str(input('  (y/n): '))

exec(open("Menu.py").read())