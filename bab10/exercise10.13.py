from pathlib import Path
import json


def get_stored_user_info(path):
    if path.exists():
        isi = path.read_text()
        data_pengguna = json.loads(isi)
        return data_pengguna

    else:
        return None


def get_new_user_info(path):
    nama = input("Siapa nama Anda? ")
    game = input("Apa game favorit Anda? ")
    hewan = input("Apa hewan favorit Anda? ")

    data_pengguna = {
        "nama": nama,
        "game": game,
        "hewan": hewan
    }

    isi = json.dumps(data_pengguna)

    path.write_text(isi)

    return data_pengguna


def greet_user():
    path = Path("user_info.json")

    data_pengguna = get_stored_user_info(path)

    if data_pengguna:
        print(f"Selamat datang kembali, {data_pengguna['nama']}!")
        print(f"Semoga Anda masih bermain {data_pengguna['game']}.")
        print(f"Apakah Anda masih menyukai {data_pengguna['hewan']}?")

    else:
        data_pengguna = get_new_user_info(path)

        print(
            f"Kami akan mengingat Anda ketika kembali, "
            f"{data_pengguna['nama']}!"
        )


greet_user()