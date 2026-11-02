def make_sandwich(*bahan):
    print("\nSandwich yang dipesan:")
    for item in bahan:
        print(f"- {item}")

make_sandwich("Roti", "Keju")
make_sandwich("Roti", "Telur", "Selada")
make_sandwich("Roti", "Daging", "Keju", "Tomat")