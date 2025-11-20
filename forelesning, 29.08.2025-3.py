#Oppgace 3 oppgavesett 1
#Uavhengige if-tester med intervaller

#Kandidatens poengsum som inndata fra bruker
poengsum=int(input("Oppgi kandidatens poengsum: "))

#Tilordning av karakter ved uavhengige if-tester og intervall
if poengsum>=0 and poengsum<40:
    karakter="F"
if poengsum>=40 and poengsum<46:
    karakter="E"
if poengsum>=46 and poengsum<58:
    karakter="D"
if poengsum>=58 and poengsum<77:
    karakter="C"
if poengsum>=77 and poengsum<92:
    karakter=b
if poengsum>=92 and poengsum<100:
    karakter="A"

#Skriver ut resultat
print("Ved poengsum",poengsum,"Så får du karakteren",karakter)

    
