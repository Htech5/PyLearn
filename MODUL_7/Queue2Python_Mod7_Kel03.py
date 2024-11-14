# Implementasi Queue menggunakan list
queue = []


def enqueue(item):
    queue.append(item)
    print(f"{item} ditambahkan ke dalam queue.")


def dequeue():
    if len(queue) > 0:
        item = queue.pop(0)
        print(f"{item} dihapus dari queue.")
    else:
        print("Queue kosong, tidak dapat melakukan dequeue.")


def display():
    if len(queue) > 0:
        print("Queue saat ini:", queue)
    else:
        print("Queue kosong.")


# Loop program utama
while True:
    print("\n--- Operasi Queue ---")
    print("1. Enqueue (Tambahkan Item)")
    print("2. Dequeue (Hapus Item)")
    print("3. Tampilkan Queue")
    print("4. Keluar")

    pilihan = int(input("Masukkan pilihan Anda: "))

    if pilihan == 1:
        item = input("Masukkan item yang akan ditambahkan: ")
        enqueue(item)

    elif pilihan == 2:
        dequeue()

    elif pilihan == 3:
        display()

    elif pilihan == 4:
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")
