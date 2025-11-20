#Forelesning 19.09.2025 nummer 2.

#første og siste element/verdi i lista skal bytte plass
talliste=[6,3,1,2,4]
print("Lista før bytte er",talliste)
#Talliste av 4 er lik talliste av 0, hva skjer med verdien da? 4 ble overskrevet
#Dette går ikke uten en byttevariabel
#Vi må ta vare på den
print("Første og siste element/verdi i lista skal bytte plass")
#Ståle la på en setning
#bytte er byttevariabelen vi bruker for å ta vare på første verdi
#Nå starter vi andre ende
bytte=talliste[0]
#Dette er første posisjon i lista begrunnet indeksen

#talliste av 0 får verdien til talliste av 4
talliste[0]=talliste[4]

#talliste av 4 får verdien som vi tok vare på i byttevariabelen.
talliste[4]=bytte
#Bytte har jo fått variabelen talliste [0] så lista etter bytte er
print ("Lista etter bytte er",talliste)

største_indeks=0

for indeks in range(len(talliste)):
    if talliste[indeks]>talliste[største_indeks]:
        største_indeks=indeks

print ("Støste verdi er",talliste[største_indeks],"på indeks",største_indeks)

bytte=talliste[største_indeks]
talliste[største_indeks]=talliste[-1]
talliste[-1]=bytte
print("Lista etter at største verdi er flyttet bakerst:", talliste)
