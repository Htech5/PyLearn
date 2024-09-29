addition = 5 + 5
hasil = addition - 1

print(hasil)
print("")

"""

ini adalah block coding dan akan diabaikan oleh sistem python

"""


"""

bagian ini mempraktekkan print dalam bentuk multi line

"""
multi_line = """siapa yang bertanggung
jawab di bagian ini ya?"""

print(multi_line)
print("")

"""
mencetak substring
"""

bacaan = "anjay"
print(bacaan[0])
print(bacaan[1])
print(bacaan[2])
print(bacaan[3])
print(bacaan[4])
print(bacaan[1:])
print("")

"""
pembuatan list
"""

xy = [1, 1.0, "satu", True]
xy[2] = "ada deh"  # mengubah kalimat "satu" menjadi kelimat "ada deh"
print(type(xy))
print(xy[2])
print(xy[1:])
print(xy[:3])
print(xy[0:2:3])
print("")

"""
tuple sama seperti list namun tidak dapat diubah data yang berada di dalam variable tuple
"""

variable_tuple = (2, 2.0, "dua", True, False)
print(type(variable_tuple))
print(variable_tuple)
print(variable_tuple[:4])
print("")

"""
set sama seperti tuple dan list namun set tidak memiliki index, set juga dapat menghilangkan data yang sejenis dan menjadikannya hanya berupa satu data saja
contoh :
x = {1,2,3,3,4}
print(x)

output = {1,2,3,4}

set juga dapat digunakan untuk operasi himpunan matematika seperti union,intesction
"""

ab = {1, 2, 3, 3, 4, 4, 5}
ba = {2, 3, 1, 4, 5, 6, 6}
union = ab.union(ba)
intesection = ba.intersection(ab)
print(type(ab))
print(ab)
print("union =", union)
print("intersection =", intesection)
print("")

"""
Dictionary pada Python merupakan kumpulan pasangan key-value yang bersifat tidak berurutan. Dictionary dapat digunakan untuk menyimpan data kecil hingga besar. Pada Python, dictionary didefinisikan dengan kurawal dan tambahan definisi berikut.
"""
name = input("masukkan  nama :")
print(type(name))
age = int(input("masukkan umur :"))
print(type(age))
status = input("Sudah punya pacar?")
job = input("Kerja apa?")
z = {"name": name, "age": age, "Punya pacar?": status}
z["job"] = job
print(z)
print(type(z))
print("")

"""
konversi kumpulan data seperti pada list,set,dan tuple
"""

print(list("Habib"))
print(set([1, 1, 2, 3, 4]))
print(tuple({1, 1, 1, 2, 3}))
print("")

"""
konversi ke dictionary
"""

print(dict([(2, 17), (3, 44)]))
print("")

"""
upper string, mengubah kalimat di dalam string menjadi full kapital
"""

a = "habib"
kata = a.upper()
print(kata)
print("")

"""
lstrip untuk menghapus spasi di kiri
rstrip untuk menghapus spasi di kanan
strip untuk menghapus spasi di kanan dan di kiri, bisa juga untuk menghapus kata
"""
b = "    mantapanjaymantap    "
print(b.lstrip())
print(b.rstrip())
print(b.strip())
print(b.strip("mantap"))
print("")

"""
join untuk menggabungkan string
split untuk memisahkan string
"""

print(" ".join(["Habib", "Mukhlis"]))
print("")
