import time
from cytypes import c_double

start_time = time.time()
print("Hello World")
print(time.time() - start_time, "detik")

# tipe data integer
data_integer = 10
print("Nilai Data : ", data_integer, "Tipe Data : ", type(data_integer))

# tipe data float
data_float = 10.0
print("Nilai Data : ", data_float, "Tipe Data : ", type(data_float))

# tipe data string
data_string = "sepuluh"
print("Nilai Data : ", data_string, "Tipe Data : ", type(data_string))

# tipe data boolean
data_boolean = True
print("Nilai Data : ", data_boolean, "Tipe Data : ", type(data_boolean))
