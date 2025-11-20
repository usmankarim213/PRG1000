#Oppgave 4, s 153

vanlig_tall=int(input("Skriv inn et nummer mellom 1-10"))

if vanlig_tall==1:
    romerske_tall="I"
else:
    if vanlig_tall==2:
        romerske_tall="II"
    else:
        if vanlig_tall==3:
            romerske_tall="III"
        else:
            if vanlig_tall==4:
                romerske_tall="IV"
            else:
                if vanlig_tall==5:
                    romerske_tall="V"
                else:
                    if vanlig_tall==6:
                        romerske_tall="VI"
                    else:
                        if vanlig_tall==7:
                            romerske_tall="VII"
                        else:
                            if vanlig_tall==8:
                                romerske_tall="VIII"
                            else:
                                if vanlig_tall==9:
                                    romerske_tall="IX"
                                else:
                                    if vanlig_tall==10:
                                        romerske_tall="X"

print("Dette er",vanlig_tall,"i romerske nummer:",romerske_tall)
