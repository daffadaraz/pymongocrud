import pymongo,os,datetime
from pymongo import MongoClient
from time import sleep
client = MongoClient()
db = client["Data-Mahasiswa"]
collection = db["Data"]
datas = db.Data

ulangc = 'y'
while ulangc == 'Y' or ulangc == "y":
        os.system('clear')
        print('         Masukkan Data')
        print()
        nama =  input('Masukkan Nama    : ')
        npm  =  input('Masukkan NPM     : ')
        kelas=  input('Masukkan Kelas   : ')
        jurusan=input('Masukkan Jurusan : ')
        
        print()

        data = {"nama": nama,
                "_id": npm,
                "kelas": kelas,
                "jurusan": jurusan,
                "lastMod": datetime.datetime.now()}
        data_id = datas.insert_one(data).inserted_id
        
        print()
        print('Ingin memasukkan data lagi?')
        ulangc = str(input('(y/n): '))
exec(open("Menu.py").read())