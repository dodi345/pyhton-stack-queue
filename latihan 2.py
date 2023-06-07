import random
import os

class Customer:
    def __init__(self, nama, jenis_transaksi):
        self.nama = nama
        self.jenis_transaksi = jenis_transaksi

class antrianTransaksi:
    def __init__(self):
        self.antrian = []

    def is_empty(self):
        return len(self.antrian) == 0

    def menambah_transaksi(self, transaksi):
        self.antrian.append(transaksi)

    def hapus_transaksi(self):
        if self.is_empty():
            return None
        return self.antrian.pop(0)

    def next_transaksi(self):
        if self.is_empty():
            return None
        return self.antrian[0]

# class program_antrian:
#     def __init__(self):
#         self.antrian_transaksi = antrianTransaksi()

def tambah_transaksi(antrian_transaksi):
    os.system("clear")
    jenis_transaksi = input("Masukan jenis transaksi : ")
    nama = input("Masukan nama anda : ")
    transaksi = Customer(nama, jenis_transaksi)
    antrian_transaksi.menambah_transaksi(transaksi)
    print(f"Transaksi {jenis_transaksi} ditambahkan kedalam antrian..")

if __name__ == "__main__":
    antrian_transaksi = antrianTransaksi()

    while True:
        print("###### Program Antrian Transaksi ######")
        print("1. Tambah transaksi")
        print("2. Tampilkan Transaksi Berikutnya")
        print("3. Keluar Program")

        pilihan = input("Pilihan anda : ")

        if pilihan == "1":
            tambah_transaksi(antrian_transaksi)
        elif pilihan == "2":
            next_transaksi = antrian_transaksi.next_transaksi()
            if next_transaksi:
                print(f"Transaksi berikutnya : {next_transaksi.jenis_transaksi}, Pelanggan : {next_transaksi.nama}")
            else:
                print("Tidak ada transaksi dalam antrian.")
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")