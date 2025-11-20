km = True

while km:
    antall_km = int(input("Hvor mange km skal du kjøre? "))

    if antall_km > 0 and  antall_km <= 50:
        print("Gyldig")
        km = False
    else:
        print("Ugyldig")
