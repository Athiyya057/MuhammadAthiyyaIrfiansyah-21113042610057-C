pizzas = ["Pepperoni", "Cheese", "Margherita"]

friend_pizzas = pizzas[:]

pizzas.append("Meat Lovers")
friend_pizzas.append("Hawaiian")

print("My favorite pizzas are:")

for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")

for pizza in friend_pizzas:
    print(pizza)