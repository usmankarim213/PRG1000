#Oppgave 2 oppgavesett 2

print("Km   Alt1  Alt2  Alt3  Beste alternativ")
print("---------------------------------------")

for km in range(0, 501, 50):
    # Beregn priser for hvert alternativ
    alt1 = 750
    alt2 = 300 + 2 * km
    alt3 = 150 + 4 * km

    # Finn billigste alternativ
    if alt1 <= alt2 and alt1 <= alt3:
        beste = "Alt1"
    elif alt2 <= alt1 and alt2 <= alt3:
        beste = "Alt2"
    else:
        beste = "Alt3"

    # Skriv ut rad i tabell
    print(f"{km:3}  {alt1:5}  {alt2:5}  {alt3:5}  {beste}")
