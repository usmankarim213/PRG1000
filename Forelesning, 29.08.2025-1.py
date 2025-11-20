#Oppgave 3, oppgavesett 1, med nøsta hvis-setninger, tester < og starter med lavest kategori

#Kandidatens poengsum som inndata fra bruker
poengsum=int(input("Oppgi kandidatens poengsum:"))

#Tilordning av karakter ved nøsta if
if poengsum<40:
    karakter="F"
else:
    if poengsum<46:
        karakter="E"
    else:
        if poengsum<58:
            karakter="D"
        else:
            if poengsum<77:
                karakter="C"
            else:
                if poengsum<92:
                    karakter="B"
                else:
                    karakter="A"
#Skriver ut resultat.
print ("Ved poengsum", poengsum, "får kandidaten karakteren",karakter)

                
