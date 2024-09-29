# Diketahui Benda bermassa 2 kg bergerak secara beraturan dalam lintasan
# melingkar berjari - jari 0,5 m dengan kecepatan 4m/s. Hitunglah :
# Gaya sentripetal (ac)
# Percepatan sentripetal (Fc)
# Kecepatan sudut (w)

# Dari soal tersebut dapat diketahui sebagai berikut :
massa = 2  # kg
r = 0.5  # m
kecepatan_linear = 4  # m/s

# Menghitung percepatan sentripetal (ac)
percepatan_sentripetal = (kecepatan_linear**2) / r

# Menghitung gaya sentripetal (Fc)
gaya_sentripetal = massa * percepatan_sentripetal  # dalam N (Newton)

# Menghitung kecepatan sudut (ω)
kecepatan_sudut = kecepatan_linear / r  # dalam rad/s

# Menampilkan hasil
print("Percepatan sentripetal: ", str(percepatan_sentripetal) + " m/s²")
print("Gaya sentripetal: ", str(gaya_sentripetal) + " N")
print("Kecepatan sudut: ", str(kecepatan_sudut) + " rad/s")
