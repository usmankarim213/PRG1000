#Oppgave 2

#Inndata er antall km, beregne pris alt 1, 2 og 3. Utdata alt som er best for kunden.

antall_km=int(input("Hvor mange antall kilometer er det?"))

fastpris1=750
fastpris2=300+2*antall_km
fastpris3=150+4*antall_km

print("alternativ1",fastpris1,"kr")
print("alternativ2",fastpris2,"Kr")
print("alternativ3",fastpris3,"Kr")

beste=min(fastpris1,fastpris2,fastpris3)

if beste==fastpris1:
    print("Beste alternativ for kunden er alternativ 1.")
elif beste == fastpris2:
    print ("Beste alternativ for kunden er alternativ 2.")
else:
    print("Beste alternativ for kunden er alternativ 3.")
    

    
