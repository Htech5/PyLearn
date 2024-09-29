class Buku:
    def __init__(self, judul, stok):
        self.judul = judul
        self.stok = stok

    def pinjam_buku(self, jumlah):
        if jumlah <= self.stok:
            self.stok -= jumlah
            return f"{jumlah} buku '{self.judul}' telah dipinjam."
        return f"Stok tidak mencukupi untuk meminjam {jumlah} buku '{self.judul}'."

    def info_buku(self):
        print(f"Judul: {self.judul}, Stok: {self.stok}")


def tampilkan_daftar_buku(daftar_buku):
    print("\nDaftar Buku:")
    for buku in daftar_buku:
        buku.info_buku()


def cari_buku(daftar_buku, judul):
    return next(
        (buku for buku in daftar_buku if buku.judul.lower() == judul.lower()), None
    )


def pinjam_buku_di_perpustakaan(daftar_buku):
    judul = input("Masukkan judul buku yang ingin dipinjam: ").strip().lower()
    buku = cari_buku(daftar_buku, judul)
    if buku:
        jumlah = int(
            input(f"Masukkan jumlah buku '{buku.judul}' yang ingin dipinjam: ")
        )
        print(buku.pinjam_buku(jumlah))
    else:
        print("Buku tidak ditemukan.")


def main():
    daftar_buku = [
        Buku("Python untuk Pemula", 5),
        Buku("Pemrograman Java", 3),
        Buku("Data Science", 2),
    ]

    while True:
        print(
            "\n=== Perpustakaan ===\n1. Tampilkan Daftar Buku\n2. Pinjam Buku\n3. Keluar"
        )
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_daftar_buku(daftar_buku)
        elif pilihan == "2":
            pinjam_buku_di_perpustakaan(daftar_buku)
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem perpustakaan.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()
