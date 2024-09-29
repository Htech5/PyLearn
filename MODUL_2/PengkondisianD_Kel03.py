# Tipe Data Dictionary = Dictionary dalam Python adalah tipe data koleksi yang digunakan untuk menyimpan data dalam pasangan key-value (kunci-nilai). Setiap item dalam dictionary terdiri dari sebuah
# key yang unik dan value yang terkait dengan key tersebut. Dictionary sangat mirip dengan kamus di dunia nyata, di mana kata-kata (key) dipetakan ke definisinya (value).
hari_dalam_seminggu = {
    1: "Senin",
    2: "Selasa",
    3: "Rabu",
    4: "Kamis",
    5: "Jumat",
    6: "Sabtu",
    7: "Minggu",
}

# Meminta input dari pengguna
kasus = float(input("Masukkan nomor hari dalam seminggu (1-7): "))

# Menggunakan dictionary untuk mencetak nama hari
# %s adalah sebagai placeholder
print(
    "Hari yang Anda pilih adalah: %s"
    % hari_dalam_seminggu.setdefault(kasus, "Nomor hari tidak valid")
)
