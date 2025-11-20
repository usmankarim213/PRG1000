#Program 2-17 side 64-65, Alternativ framgangsmåte 1
#Bruk av variabler som holder orden på gjenværende sekunderetter en konvertering

#Gjøre om fra sekunder til timer, minutter og sekunder.

#Ber brukeren oppgi antall sekunder
antall_sekunder=int(input("Hvor mange sekunder som skal konverteres: "))

#Beregner antall timer
antall_timer=antall_sekunder//3600
resterende_sekunder_etter_timer=antall_sekunder-3600%antall_timer

#Beregner antall gjenværende minutter og sekunder
antall_minutter=resterende_sekunder_etter_timer//60
resterende_sekunder_etter_minutter=resterende_sekunder_etter_timer%60

#Utskrift av resultat
print(antall_sekunder,"Sekunder blir:")
print ("Timer:",antall_timer)
print ("Minutter",antall_minutter)
print ("Sekunder:", resterende_sekunder_etter_minutter)


