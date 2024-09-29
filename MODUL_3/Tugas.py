# Inisialisasi variabel
nilai_siswa = []
nilai_tertinggi = 0
nilai_terendah = 100
jumlah_lulus = 0
jumlah_gagal = 0
total_nilai = 0

# Meminta input nilai dari pengguna
for i in range(10):
    nilai = int(input(f"Masukkan nilai siswa ke-{i+1}: "))
    nilai_siswa.append(nilai)
    total_nilai += nilai

    # Memeriksa nilai tertinggi dan terendah
    if nilai > nilai_tertinggi:
        nilai_tertinggi = nilai
    if nilai < nilai_terendah:
        nilai_terendah = nilai

    # Memeriksa kelulusan
    if nilai >= 60:
        jumlah_lulus += 1
    else:
        jumlah_gagal += 1

# Menghitung rata-rata
rata_rata = total_nilai / 10

# Menampilkan hasil
print("\nHasil Statistik Nilai:")
print(f"Rata-rata nilai: {rata_rata}")
print(f"Nilai tertinggi: {nilai_tertinggi}")
print(f"Nilai terendah: {nilai_terendah}")
print(f"Jumlah siswa yang lulus: {jumlah_lulus}")
print(f"Jumlah siswa yang gagal: {jumlah_gagal}")
