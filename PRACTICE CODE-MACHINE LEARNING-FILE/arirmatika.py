a = 15
b = 2

# operasi pertambahan +
tambah = a + b
print(a, "+", b, "=", tambah)

# operasi pengurangan -
kurang = a - b
print(a, "-", b, "=", kurang)

# operasi perkalian *
kali = a * b
print(a, "*", b, "=", kali)

# operasi pembagian /
bagi = a / b
print(a, "/", b, "=", bagi)

# operasi (eksponen) perpangkatan **
pangkat = a**b
print(a, "**", b, "=", pangkat)

# operasi modulus %
sisa = a % b
print(a, "%", b, "=", sisa)

# operasi floor division //
floor = a // b
print(a, "//", b, "=", floor)

# prioritas operasi

#  1. ()
#  2. eksponen
#  3. perkalian, pembagian, modulus, dan floor division
#  4. pertambahan dan pengurangan

 
x = 2
y = 3
z = 4

prioritas = x**y - (y + z) - z % x / y // x
print(
    x,
    "**",
    y,
    "-",
    "(",
    y,
    "+",
    z,
    ")",
    "-",
    z,
    "%",
    x,
    "/",
    y,
    "//",
    x,
    "=",
    prioritas,
)
