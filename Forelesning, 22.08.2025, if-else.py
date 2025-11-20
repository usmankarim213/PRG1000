#Beregning av bruttolønn, skattetrekk og netto utbetalt.

#Inndata fra brukeren
timelonn=float(input("Hva er din timelønn?"))
antall_timer=float(input("Hvor mange timer har du arbeidet?"))

#Beregner bruttolønn
bruttolonn=antall_timer*timelonn

#Finner riktig skattesats:

if bruttolonn<20000:
    skattesats=28
else:
    if bruttolonn<30000:
        skattesats=35
    else:
        skattesats=40

#Beregner skatt og nettolønn
skatt_i_kr=bruttolonn*skattesats/100
nettolonn=bruttolonn-skatt_i_kr

#Skriver ut lønnsberegningen.
print("Din bruttlønn er da",format (bruttolonn, ".2f"))
print ("Din skatteprosent er ", skattesats,"og skattetrekket i kr er",format(skatt_i_kr,".2f"))
print ("Du får utbetalt", format (nettolonn,"2f"),"kr")


