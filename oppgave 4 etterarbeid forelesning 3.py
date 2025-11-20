tall1=int(input("Skriv inn tall nr 1:"))
tall2=int(input("Skriv inn tall nr 2:"))
tall3=int(input("Skriv inn tall nr 3:"))
tall4=int(input("Skriv inn tall nr 4:"))
tall5=int(input("Skriv inn tall nr 5:"))



if tall2<minste:
    minste=tall2
    tallnr=2
else:
    if tall3<minste:
    minste=tall3
    tallnr=3
else:
    if tall4<minste:
    minste=tall4
    tallnr=4
else:
    if tall5<minste:
    minste=tall5
    tallnr=5

print ("Det minste tallet er",minste,"(tallnr",tallnr,")")
