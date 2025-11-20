#Oppgave 11, side 154

kjøpt_bøker=int(input("Hvor mange bøker har du kjøpt"))


if kjøpt_bøker<2:
    antall_poeng="0"
else:
    if kjøpt_bøker<4:
        antall_poeng="5"
    else:
        if kjøpt_bøker<6:
            antall_poeng="15"
        else:
            if kjøpt_bøker<8:
                antall_poeng="30"
            else:
                antall_poeng="60"

print("Ved kjøp bøker av",kjøpt_bøker,"så har du,",antall_poeng)


    
