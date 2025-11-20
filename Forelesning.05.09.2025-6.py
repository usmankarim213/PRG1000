#Program for å summere tall

summen_er=0
antall_tall=int(input("Hvor mange tall skal summeres"))

for n in range (1, antall_tall+1,1):
    print("Tall nr:",n)
    tall=int(input("Oppgi tall:"))
    summen_er=summen_er+tall
    print ()

print("Summen av de",antall_tall,"tallene er",summen_er)
