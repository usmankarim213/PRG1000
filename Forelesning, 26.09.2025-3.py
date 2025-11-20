#Program for å lese navn for navn fra fil og skrive ut de navnene som passser med "søkekriteriet"

#Åpner fila i student.txt
studentfil=open("student.txt","r")

#Generelle strukturer.
#Vi leser første linje i fila før løkka, før vi tester
#Ved å bruke readline=metoden.
student=studentfil.readline()

#tester på eof=end of file.
while student !='':
    #Muligheten for å slice
    #Ståle skrev med stor O, men siden jeg ikke har fått opp resten av filen så skriver jeg stor K for kari
    if student[0]=="O":
        print(student)
    #Leser ny linje i fila
    student=studentfil.readline()
        
    
#stenger fila
studentfil.close()
