# non return function
def non_return_function(nama, nim):
    print("Selamat datang di praktikum PROGDAS 2024 {} dengan NIM {}".format(nama, nim))


# return function
def return_func(angka):
    print(f"Angka kalian adalah {angka}")
    if angka % 2 == 0:
        return print("Mengembalikan nilai genap dengan angka {}".format(angka))
    else:
        return print("Mengembalikan nilai ganjil dengan angka {}".format(angka))


# arbitrary function function
def arbitrary_func(*penutup):
    for nama in penutup:
        print(f"Terima kasih {nama}")


# anonymous function

add = lambda x, y: x + y
result = add(5, 3)

# menjalankan fungsi
non_return_function("Habib", 21120124130081)
return_func(18)
arbitrary_func("test 1", "test 2", "test 3")
print(add(2, 9))
