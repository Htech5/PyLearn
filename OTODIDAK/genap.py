def genap(n):
    return [i for i in range(n + 1) if i % 2 == 0]


bilangan = int(input("Masukkan Bilangan = "))
print(genap(bilangan))
