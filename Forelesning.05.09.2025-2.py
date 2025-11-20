#Program for å beregne farge på tall på ruletten
#Alternativ 2, uavhengige if-tester, tester på intervaller og "talltyper"
#and-setning

tall=int(input("Hva er tallet på ruletten?"))

if tall==0:
    farge="Grønn"

if tall>=1 and tall<=10 and (tall%2)==0:
    farge="svart"
else:
    farge="rød"
    if tall>=11 and tall<=18 and (tall%2)==0:
        farge="svart"
    else:
        farge="rød"
        #Fortsetter på kodingen som jeg har gjort.

print("Tallet er",tall,"og markert",farge,"på ruletten")

