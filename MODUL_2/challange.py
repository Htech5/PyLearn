jam_tidur = int(input("Masukkan Jam tidur"))

if jam_tidur >= 10:
    print("Tidur berlebihan")
elif jam_tidur >= 8:
    print("Tidur Sehat")
elif jam_tidur >= 6:
    print("cukup tidur")
elif jam_tidur >= 4:
    print("kurang tidur")
else:
    print("Sangat kurang tidur")
