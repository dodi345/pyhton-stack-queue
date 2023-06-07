# Percobaan 4

stack = []


def tambah_barang(stack, barang_baru):
    stack.append(barang_baru)
    print(f"{barang_baru} Berhasil menambahkan ke dalam stack.")


def hapus_barang_terakhir(stack):
    if len(stack) == 0:
        print(f"Stack kosong, tidak ada barang yang dapat dihapus.")
    else:
        barang_terakhir = stack.pop()
        print(f"{barang_terakhir} berhasil dihapus dari stack.")


def tampilan_barang_teratas(stack):
    if len(stack) == 0:
        print("Stack kosong, tidak ada barang yang bisa ditampilkan.")
    else:
        barang_teratas = stack[-1]
        print(f"Barang teratas di dalam stack adalah {barang_teratas}")


while True:
    print("n\Gudang saat ini : ", stack)
    print("Menu")
    print("1. Tambah Barang")
    print("2. Hapus barang terakhir")
    print("3. Tampilkan barang teratas")
    print("4. Keluar")

    pilihan = input("Masukan pilihan anda (1/2/3/4) : ")

    if pilihan == "1":
        barang_baru = input("Masukan nama barang yang akan ditambahkan : ")
        tambah_barang(stack, barang_baru)
    elif pilihan == "2":
        hapus_barang_terakhir(stack)
    elif pilihan == "3":
        tampilan_barang_teratas(stack)
    elif pilihan == "4":
        print("Terima kasih telah menggunakan program ini")
        break
    else:
        print("Pilihan tidak valid. Silahkan masukan pilihan yang benar")
