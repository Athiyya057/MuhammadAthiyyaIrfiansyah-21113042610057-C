while True:
    umur = input("Masukkan umur Anda (ketik quit untuk berhenti): ")

    if umur == "quit":
        break

    umur = int(umur)

    if umur < 3:
        print("Tiket gratis.")
    elif umur <= 12:
        print("Harga tiket adalah $10.")
    else:
        print("Harga tiket adalah $15.")