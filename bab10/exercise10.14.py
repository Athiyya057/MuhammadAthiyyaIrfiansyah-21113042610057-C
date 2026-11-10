from pathlib import Path
import json


def get_stored_username(path):
    if path.exists():
        isi = path.read_text()
        username = json.loads(isi)
        return username

    else:
        return None


def get_new_username(path):
    username = input("Siapa nama Anda? ")

    isi = json.dumps(username)

    path.write_text(isi)

    return username


def greet_user():
    path = Path("username.json")

    username = get_stored_username(path)

    if username:
        benar = input(f"Apakah Anda {username}? (y/n): ")

        if benar == "y":
            print(f"Selamat datang kembali, {username}!")

        else:
            username = get_new_username(path)

            print(
                f"Kami akan mengingat Anda ketika kembali, {username}!"
            )

    else:
        username = get_new_username(path)

        print(
            f"Kami akan mengingat Anda ketika kembali, {username}!"
        )


greet_user()