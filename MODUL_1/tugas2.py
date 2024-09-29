pertama = input("masukkan nama orang pertama : ")
print("Orang pertama : " + pertama)

kedua = input("masukkan nama orang kedua : ")
print("Orang kedua : " + kedua)

ketiga = input("masukkan nama orang ketiga : ")
print("Orang ketiga : " + ketiga)

keempat = input("masukkan nama orang keempat : ")
print("Orang keempat : " + keempat)

daftar = [
    [pertama, kedua, ketiga, keempat],
    ["Rainbow 6 Siege", "Genshin Impact", "Red Dead Redemption 2", "Valorant"],
]

for row in daftar:
    print(row)

print(daftar[0][0] + " memainkan " + daftar[1][0])
print(daftar[0][1] + " memainkan " + daftar[1][1])
print(daftar[0][2] + " memainkan " + daftar[1][2])
print(daftar[0][3] + " memainkan " + daftar[1][3])
