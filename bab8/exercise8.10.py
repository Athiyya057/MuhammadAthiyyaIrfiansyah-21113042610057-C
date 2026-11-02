def send_messages(pesan, sent_messages):
    while pesan:
        pesan_sekarang = pesan.pop()
        print(pesan_sekarang)
        sent_messages.append(pesan_sekarang)

daftar_pesan = [
    "Selamat pagi!",
    "Semangat belajar!",
    "Jangan lupa mengerjakan tugas."
]

sent_messages = []

send_messages(daftar_pesan, sent_messages)

print("\nDaftar pesan awal:", daftar_pesan)
print("Pesan terkirim:", sent_messages)