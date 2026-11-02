sandwich_orders = [
    "tuna",
    "pastrami",
    "chicken",
    "pastrami",
    "beef",
    "pastrami",
    "cheese"
]

finished_sandwiches = []

print("Maaf, deli kehabisan pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"I made your {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

print("\nDaftar sandwich yang sudah dibuat:")

for sandwich in finished_sandwiches:
    print(sandwich)