import array

var = [1, 2, 3, 4, 5]

for n in range(len(var)):
    current = var[n]
    next = n + 1

    if next < len(var):
        next_element = var[next]
    else:
        next_element = None 

    print(f"current array: {current}, next array: {next_element}")

a = [9, 6, 5, 100, 3]
left = a[0]
for b in range(len(a)):
    right = a[b]

    if right > left:
        left = right

print(left)

c = array.array("i", [1, 2, 3, 4, 5])
print(type(c))


matriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matriks)
print(type(matriks))
for row in matriks:
    print(row)
