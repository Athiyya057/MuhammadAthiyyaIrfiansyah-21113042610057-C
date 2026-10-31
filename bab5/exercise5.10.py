current_users = [
    "Abi",
    "Athiyya",
    "Naufal",
    "Akbar",
    "Fayaz"
]

new_users = [
    "iyan",
    "Khairul",
    "NAUFAL",
    "SAMUEL",
    "Nafis"
]

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} is already taken.")
    else:
        print(f"{new_user} is available.")