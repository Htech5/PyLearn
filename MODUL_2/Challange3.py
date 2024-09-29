deposit = int(input("Masukkan nominal yang diinginkan :"))
print("Anda memasukkan nominal deposit sebesar :", deposit)
print("Pilihan lama deposit :")
print("1. Satu Tahun 5%")
print("2. Dua Tahun 10%")
print("3. Tiga Tahun 15%")
lama = int(input("Masukkan lama deposit : "))

pilihan_lama_deposit = {
    1: "Satu tahun",
    2: "Dua Tahun",
    3: "Tiga Tahun",
}

print(
    "Deposit yang Anda pilih adalah: %s"
    % pilihan_lama_deposit.setdefault(lama, "Lama deposit tidak valid")
)

if lama == 1:
    hasil = deposit + (deposit * 0.05)
    print("Nilai deposit setelah satu tahun adalah :", hasil)
elif lama == 2:
    hasil = deposit + (deposit * 0.1)
    print("Nilai deposit setelah dua tahun adalah :", hasil)
elif lama == 3:
    hasil = deposit + (deposit * 0.15)
    print("Nilai deposit setelah tiga tahun adalah :", hasil)
