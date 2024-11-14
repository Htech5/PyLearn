# Inisialisasi stack dan variabel
fruits = []
a = 1
b = 2
c = 3

# Menambahkan nilai ke dalam stack
fruits.append(a)  # Push a (1)
fruits.append(b)  # Push b (2)
fruits.append(c)  # Push c (3)

print("Sebelum ditukar:", fruits)

# Menggunakan stack untuk menukar a dan c
a = fruits.pop()  # Pop c (3)
b = fruits.pop()  # Pop b (2)
c = fruits.pop()  # Pop a (1)

print(a, b, c)
