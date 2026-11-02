def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last

    return user_info

profil = build_profile(
    "Muhammad",
    "Athiyya",
    prodi="Teknik Industri",
    universitas="UNS",
    asal="Ponorogo"
)

print(profil)