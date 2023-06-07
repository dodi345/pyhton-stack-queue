stack = {}

def tambah(buku, pengarang):
    key = len(stack)
    stack[key] = {"buku": buku, "pengarang":pengarang}
    
def hapus_buku_terakhir(stack):
    if len(stack) == 0:
        print(f"Stack kosong, tidak ada barang yang dapat dihapus.")
    else:
        key = len(stack) -1
        buku = stack[key]["buku"]
        pengarang = stack[key]["pengarang"]
        del stack[key]
        return buku,pengarang


def tampilan_buku_teratas(stack):
    if len(stack) == 0:
        print("Stack kosong, tidak ada barang yang bisa ditampilkan.")
    else:
        print("Buku teratas :")
        for buku, pengarang in stack.items():
            print("Nama buku:", buku)
            print("Pengarang:", pengarang)
        

while True:
    print("n\Gudang saat ini : ", stack)
    print("Menu")
    print("1. Tambah Buku")
    print("2. Hapus buku terakhir")
    print("3. Tampilkan buku teratas")
    print("4. Keluar")

    pilihan = input("Masukan pilihan anda (1/2/3/4) : ")

    if pilihan == "1":
        buku = input("Masukan nama buku : ")
        pengarang = input("Masukan nama pengarang : ")
        tambah(buku, pengarang)
    elif pilihan == "2":
        hapus_buku_terakhir(stack)
    elif pilihan == "3":
        tampilan_buku_teratas(stack)
    elif pilihan == "4":
        print("Terima kasih telah menggunakan program ini")
        break
    else:
        print("Pilihan tidak valid. Silahkan masukan pilihan yang benar")
