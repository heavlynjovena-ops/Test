import os

siswa = {
    "1234" : {"Nama" : "Claire", "Alamat" : "Jln. Merdeka", "Nomor HP" : "083526683339"},
    "2345" : {"Nama" : "Rose", "Alamat" : "Marlin Street", "Nomor HP" : "083526683338"},
}

def tambah(): 
    while True:
        nis = ""
        nama = ""
        alamat = ""
        nomorhp = ""

        while True:
            os.system('clear')
            nis = input('NIS: ')
            nama = input('Nama: ')
            alamat = input('Alamat: ')
            nomorhp = input('Nomor HP: ')

            if nis in siswa:
                print(f'Nomor NIS {nis} ini sudah digunakan\nSilahkan gunakan nomor lain.')
                input('Tekan Enter...')
            else:
                break

        siswa[nis] = {
            "Nama":nama,
            "Alamat":alamat,
            "NomorHP":nomorhp
        }
        print('Data Siswa Berhasil Ditambahkan.')
        lagi = input("Tambah lagi y/t: ")
        if lagi == "t":
            return
    
def tambah():
    os.system('clear')
    if len(siswa) == 0:
        print("Data siswa masih kosong\nSilahkan tambah siswa terlebih dahulu...")
        input("Tekan Enter...")
        return
    print(f"Jumlah Data Siswa : {len(siswa)}")
    print("-"*66)
    print("|{:^4}|{:^20}|{:^24}|{:^13}|".format('NIS','Nama Lengkap','Alamat','Nomor HP'))
    for nis in siswa:
        print("|{:^4}|{:^20}|{:^24}|{:^13}|".format(nis,siswa[nis]['nama'],siswa[nis]["alamat"],siswa[nis]["nomorhp"]))
        print("-"*66)

def lihat():
    print("|{:^4}|{:^20}|{:^24}|{:^13}|".format('NIS','Nama Lengkap','Alamat','Nomor HP'))
    print("-"*66)
    for nis in siswa:
        print("|{:^4}|{:^20}|{:^24}|{:^13}|".format(nis,siswa[nis]['nama'],siswa[nis]["alamat"],siswa[nis]["nomorhp"]))
        print("-"*66)

def menu():
    while True:
        os.system('clear')
        pilih = int(input('1. Tambah\n2. Lihat\n3. Keluar\nPilih:'))
        if pilih == 1:
            tambah()
        elif pilih ==2:
            lihat()
        elif pilih == 3:
            print('Terima kasih, sampai jumpa lagi.')
            break
        else:
            print("Pilihan tidak ditemukan.")

        input("Tekan Enter...")

menu()