

for n in range(0,501,50):
    fastpris1=750
    fastpris2=300+2*n
    fastpris3=150+4*n
    billigst=int(input("Hvilken bil skal du velge"))

if fastpris1<= fastpris2 and fastpris1<= fastpris3:
    billigst="Første prisen"
else:
    if fastpris2<=fastpris1 and fastpris2<=fastpris3:
        billigst="Andre prisen"
    else:
        billigst="Tredje prisen"

print("Den billigste prisen er",billigst)

