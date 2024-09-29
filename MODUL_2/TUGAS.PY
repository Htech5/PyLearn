uang = int(input("Masukkan jumlah uang yang Anda miliki: "))

if uang >= 900_000_000:
    kategori = "Mobil Mewah"
    print(f"Anda dapat membeli kategori: {kategori}")
    print("Pilihan merk mobil: ")
    print("1. BMW (Rp800.000.000)")
    print("2. Mercedes (Rp900.000.000)")
elif uang >= 250_000_000:
    kategori = "Mobil Menengah"
    print(f"Anda dapat membeli kategori: {kategori}")
    print("Pilihan merk mobil: ")
    print("1. Civic (Rp250.000.000)")
    print("2. Corolla (Rp230.000.00)")
elif uang >= 200_000_000:
    kategori = "Mobil Ekonomis"
    print(f"Anda dapat membeli kategori: {kategori}")
    print("Pilihan merk mobil: ")
    print("1. Avanza (Rp200.000.000)")
    print("2. Xenia (Rp180.000.000)")
else:
    print("Jumlah uang yang dimasukkan tidak valid.")
    exit()

pilihan = int(input("Masukkan pilihan merk mobil (1 atau 2): "))

if kategori == "Mobil Ekonomis":
    if pilihan == 1:
        merk = "Avanza"
        harga = 200_000_000
    elif pilihan == 2:
        merk = "Xenia"
        harga = 180_000_000
    else:
        print("Pilihan tidak valid.")
        exit()
elif kategori == "Mobil Menengah":
    if pilihan == 1:
        merk = "Civic"
        harga = 250_000_000
    elif pilihan == 2:
        merk = "Corolla"
        harga = 230_000_000
    else:
        print("Pilihan tidak valid.")
        exit()
elif kategori == "Mobil Mewah":
    if pilihan == 1:
        merk = "BMW"
        harga = 800_000_000
    elif pilihan == 2:
        merk = "Mercedes"
        harga = 900_000_000
    else:
        print("Pilihan tidak valid.")
        exit()

print(f"Anda telah memilih mobil {merk} dengan harga Rp{harga:,}.")
