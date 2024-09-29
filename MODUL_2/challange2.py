nama_bulan = {
    1: "Januari",
    2: "Februari",
    3: "Maret",
    4: "April",
    5: "Mei",
    6: "Juni",
    7: "Juli",
    8: "Agustus",
    9: "September",
    10: "Oktober",
    11: "November",
    12: "Desember",
}

jumlah_hari = {
    1: "31",
    2: "28/29",
    3: "31",
    4: "30",
    5: "31",
    6: "30",
    7: "31",
    8: "31",
    9: "30",
    10: "31",
    11: "30",
    12: "31",
}

hasil = int(input("Masukkan nomor bulan (1-12): "))

if hasil in nama_bulan and hasil in jumlah_hari:
    print(nama_bulan[hasil] + " memiliki " + jumlah_hari[hasil] + " hari.")
else:
    print("Nomor bulan tidak valid.")
