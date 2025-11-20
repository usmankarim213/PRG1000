#Program for å stimulere test av disjunksjon.
#Bryter med at variabelnavn bør skrives med små bokstaver

for a in range(2,6,1):
    for b in range(4,8,1):
        if a>3 or b<6:
            print(a,b,"Sann")
        else:
            print(a,b,"Usann")
    print("Da er det slutt på løkka for å øke B med 1")
    print()
    print("Da øker verdien på A med 1")
print ("Da er det slutt på løkka for å øke A med 1")

