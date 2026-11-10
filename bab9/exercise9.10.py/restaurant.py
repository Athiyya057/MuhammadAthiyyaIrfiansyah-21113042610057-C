class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} menyajikan {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.name} sedang buka.")