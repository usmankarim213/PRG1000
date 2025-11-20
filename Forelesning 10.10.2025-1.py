#Et program for å endre navn på student Olavia til Olivia
#Oppgave 3 i etterarbeid, arbeidsøkt forelesning 8

import os

#Åpner original fil i read
student_fil=open("student.txt","r")
#Åpner temp-fil i write
temp_fil=open("temp.txt","w")

#Bolsk variabel for om student Olavia finnes
funnet=False

#Leser første student i filen
fornavn=student_fil.readline()

while fornavn !="":
    fornavn=fornavn.rstrip("\n")

    if fornavn=="Olavia":
        temp_fil.write("Olivia\n")
        funnet=True
    else:
        temp_fil.write(fornavn+"\n")


    #Leser neste student
    fornavn=student_fil.readline()

temp_fil.close()
student_fil.close()

