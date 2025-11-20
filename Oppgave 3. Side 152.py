#Oppgave 3. Side.152

måneden=int(input("Skriv inn måneden her:"))

if måneden<4:
    kvarteret="1"
else:
    if måneden<7:
        kvarteret="2"
    else:
        if måneden<10:
            kvarteret="3"
        else:
            if måneden<=12:
                kvarteret="4"

print("Ved denne måneden",måneden,"så er du i dette kvarteret",kvarteret)


