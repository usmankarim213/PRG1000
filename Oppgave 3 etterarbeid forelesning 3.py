#Oppgave 3 etterarbeid forelesning 3

a_karakter=92
b_karakter=77
c_karakter=58
d_karakter=46
e_karakter=40

karakter=int(input("Skriv inn dine testpoeng."))

if karakter>=a_karakter:
    print("Karakteren din er A.")
else:
    if karakter>=b_karakter:
        print ("Karakteren din er B")
    else:
        if karakter>=c_karakter:
            print("Karakteren din er C")
        else:
            if karakter>=d_karakter:
                print("Karakteren din er D.")
            else:
                karakter>=e_karakter
                print("Karakteren din er E")
