class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

        self.privileges = [
            "Dapat menambahkan postingan",
            "Dapat menghapus postingan",
            "Dapat memblokir pengguna"
        ]

    def show_privileges(self):
        print("Hak akses administrator:")

        for privilege in self.privileges:
            print(f"- {privilege}")


admin = Admin("Iyan", "Ahmad")

admin.show_privileges()