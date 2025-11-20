#Program for innføring i funkjsoner/prosedyrer/del-programmet.
def drommebolig():
    #Her kommer kode for kalkulator 1
    print("Du har valgt kalkulator 1, Drømmebolig\n")

def lanebevis():
    #Her kommer kode for kalkulator 2
    print("Du har valgt kalkulator 2, Lånebevis\n")
    
def main():
    #Her kommer koden for programmet.
    fortsette=True
    while fortsette==True:
        valgt_kalkulator=int(input("Hvilken kalkulator vil du bruke?"))
        if valgt_kalkulator==1:
            drommebolig()
        else:
            lanebevis()

        svar=input("Ønsker du å bruke et av kalkulatorene på nytt?")
        if svar=="nei":
            fortsette=False
#Her kjøres main()
main()
print("Program avsluttet.")
