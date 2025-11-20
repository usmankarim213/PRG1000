tall=int(input("Hva er tallet på ruletten"))

if tall==0:
    farge="Grønn"
else:
    if tall<=10:
        if (tall%2)==0:
            farge="Svart"
        else:
            farge="Rød"
    else:
        if tall<=18:
            if (tall%2)==0:
                farge="Rød"
            else:
                farge="Svart"
            


print("Tallet er",farge,"på ruletten")
