# Membuat array 2 dimensi (list of lists)
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]

# Menampilkan matriks
print("Matriks 3x3:")
for row in matrix:
    print(row)

# Mengakses elemen tertentu, misalnya elemen di baris 1 kolom 2
print("\nElemen di baris 1, kolom 2:", matrix[0][1])

# Mengubah elemen tertentu, misalnya mengubah elemen di baris 2 kolom 3 menjadi 10
matrix[1][2] = 10

# Menampilkan matriks setelah diubah
print("\nMatriks setelah perubahan:")
for row in matrix:
    print(row)
