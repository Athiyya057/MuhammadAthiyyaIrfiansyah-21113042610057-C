class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
            print("Baterai berhasil ditingkatkan menjadi 100 kWh.")

    def describe_battery(self):
        print(f"Kapasitas baterai: {self.battery_size} kWh")


class ElectricCar:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.battery = Battery()

    def get_range(self):
        if self.battery.battery_size == 75:
            jarak = 260
        elif self.battery.battery_size == 100:
            jarak = 315
        else:
            jarak = 0

        print(f"Jarak tempuh: {jarak} mil")


mobil = ElectricCar("Tesla", "Model S")

mobil.battery.describe_battery()
mobil.get_range()

mobil.battery.upgrade_battery()

mobil.battery.describe_battery()
mobil.get_range()