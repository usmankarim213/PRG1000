#Oppgave 3 oppgavesett 1,med if-elif-else, tester < og starter med lavest kategori

#Kandidatens poengsum som inndata fra bruker
poengsum=int(input("Oppgi kandidatens poengsum:"))

#Tilordning av karakter
if poengsum<40:
    karakter="F"
elif poengsum<46:
    karakter="E"
elif poengsum<58:
    karakter="D"
elif poengsum<77:
    karakter="C"
elif poengsum<92:
    karakter="B"
else:
    karakter="A"

#Skriver ut resultat.
print("Ved poengsummen",poengsum,"Så får du karakteren",karakter)

