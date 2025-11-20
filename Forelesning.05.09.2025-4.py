#Inndatatest i begynnelsen av programmet

#Variabel til til løkke for inndatatest, bolsk variabel
nytt_tall=True

#Løkke som sikrer oss gyldig verdi
while nytt_tall:
    #Brukeren oppgir verdi på ruletten
    tall=int(input("Hva er tallet på ruletten"))

    #Tester om gyldig verdi
    if tall>=0 and tall<=10:
        print("Gyldig verdi")
        nytt_tall=False
    else:
        print("Ugyldig verdi på ruletten, skriv inn nytt tall")

print ("Da har vi fått gyldig tall på ruletten og kan fortsette programmet med å avgjøre riktig farge")


