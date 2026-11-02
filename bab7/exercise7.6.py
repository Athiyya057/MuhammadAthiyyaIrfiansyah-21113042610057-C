topping = ""

while topping != "quit":
    topping = input("Masukkan topping (quit untuk berhenti): ")

    if topping != "quit":
        print(f"Menambahkan {topping} ke pizza.")

aktif = True

while aktif:
    topping = input("Masukkan topping (quit untuk berhenti): ")

    if topping == "quit":
        aktif = False
    else:
        print(f"Menambahkan {topping} ke pizza.")

while True:
    topping = input("Masukkan topping (quit untuk berhenti): ")

    if topping == "quit":
        break

    print(f"Menambahkan {topping} ke pizza.")