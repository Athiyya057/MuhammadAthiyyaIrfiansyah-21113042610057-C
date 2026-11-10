class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print("\nInformasi Pengguna:")
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Lokasi: {self.location}")

    def greet_user(self):
        print(f"Halo, selamat datang {self.username}!")


user1 = User("Iyan", "Ahmad", "iyan123", "iyan@gmail.com", "Ponorogo")
user2 = User("Budi", "Santoso", "budi456", "budi@gmail.com", "Surakarta")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()