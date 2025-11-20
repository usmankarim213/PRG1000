#Oppgavesett 3 lister/tabeller oppgave 1

fornavn=[]



navn=input("Skriv inn minst et fornavn: ")
fornavn=fornavn+[navn]

nyttnavn=input("Skriv inn nytt navn, Ja/Nei")

while nyttnavn=="Ja":
    navn=input("Skriv inn et fornavn: ")
    fornavn=fornavn+[navn]
    nyttnavn=input("Skriv inn nytt navn, Ja/Nei")

print(fornavn)


#i=len(fornavn)-1
#while i>=0:
#    print(fornavn[i])
#    i=i-1

fornavn.reverse()
for n in fornavn:
    print (n)
