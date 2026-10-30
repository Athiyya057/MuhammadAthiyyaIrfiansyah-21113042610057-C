def hitung_parkir(jenis, jam_masuk, jam_keluar):
    tarif_masuk = [1000, 2000, 4000, 10000]
    tarif_progresif = [0, 1000, 2000, 5000]
    tarif_maksimal = [1000, 10000, 15000, 0]
    tarif_inap = [1000, 15000, 20000, 0]

    indeks = jenis - 1
    lama_parkir = jam_keluar - jam_masuk

    if lama_parkir < 0:
        lama_parkir += 24

    dasar = tarif_masuk[indeks]
    progresif = 0
    inap = 0

    if jenis == 1:
        total = 1000

    elif lama_parkir < 2:
        total = dasar

    elif lama_parkir < 24:
        progresif = (lama_parkir - 2) * tarif_progresif[indeks]
        total = dasar + progresif

        if jenis == 2:
            total = min(total, tarif_maksimal[indeks])
        elif jenis == 3:
            total = min(total, tarif_maksimal[indeks])

    else:
        inap = tarif_inap[indeks]
        total = inap

    return dasar, progresif, inap, total, lama_parkir