#Program for å lese 5 tall inn i en liste og å finne det minste tallet.

#Tallliste defineres som en tom liste

talliste=[]

#Utskrift av listeinholld før fylling

print("Lista til nå",talliste)
print()

#Så kommer det ei FOR-løkke for å lese inn 5 tall i lista talliste
for tallnr in range (1,6,1):
    print("Tall nr:",tallnr)
    tall=int(input("Oppgi tall: "))
    #Vi tar det imot og legger det in i lista/Innlest tall legges inn i lista
    talliste=talliste+[tall]
    #Utskrift av listeinnhold underveis i fyllinga av lista
    print("Lista til nå",talliste)

#Utskrift av listeinnhold og listestørrelse etter fylling
print ("Hele lista er",talliste)
liste_lengde=len(talliste)
print("Antall elementer i lista er: ",liste_lengde)




#Resten skal jeg kode.
#Prøv selv
#Utvid programet til å finne minste tallet og tallnr i lista, ikke funksjoner men g
minste_tall=talliste[0]
tallnr=1

for indeks in range (1,5,1):
    if talliste[indeks]<minste_tall:
        minste_tall=talliste[indeks]
        tallnr=indeks+1

print("Det minste tallet er",minste_tall,"og det er tall nr",tallnr,"i lista")

