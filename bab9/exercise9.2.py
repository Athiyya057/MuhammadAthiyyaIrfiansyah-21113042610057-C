class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            f"{self.restaurant_name} menyajikan "
            f"{self.cuisine_type}."
        )


restaurant1 = Restaurant("Warung Nusantara", "Masakan Indonesia")
restaurant2 = Restaurant("Pizza House", "Pizza")
restaurant3 = Restaurant("Sushi Jepang", "Makanan Jepang")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()