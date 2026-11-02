sandwich_orders = [
    "tuna",
    "chicken",
    "beef",
    "cheese"
]

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"I made your {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

print("\nDaftar sandwich yang sudah dibuat:")

for sandwich in finished_sandwiches:
    print(sandwich)