print("Sammenligning av bilutleiealternativer\n")

for km in range(0, 501, 50):
    input(f"Trykk Enter for å sjekke km: {km}...")  # Vent på bruker

    # Beregn pris for hvert alternativ
    pris1 = 750
    pris2 = 300 + 2 * km
    pris3 = 150 + 4 * km

    # Finn billigste alternativ
    minstpris = pris1
    alternativ = 1

    if pris2 < minstpris:
        minstpris = pris2
        alternativ = 2
    if pris3 < minstpris:
        minstpris = pris3
        alternativ = 3

    print("Km:", km)
    print("Billigste alternativ er:", alternativ, "med pris", minstpris, "kr\n")

