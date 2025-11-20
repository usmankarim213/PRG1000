#Program for beregne farge på tall på ruletten
#Alternativ 3, tar utgangspunkt i hvilken farge gjelder for hvilke intervaller og tall

tall=int(input("Hva er tallet på ruletten?"))

if tall==0:
    farge="grønn"

if ((tall>=1 and tall<=10 and (tall%2)==0)
    or(tall>=11 and tall<=18 and (tall%2)!=0)):
    farge="svart"
else:
    farge="rød"


print("Tallet er",tall,"og markert",farge,"på ruletten")

