#Program for å skrive 3 nye navn til en eksisterende fil
#Dette er fortsettelse fra første time 26.09.2025

#Åpner fila student.txt
studentfil=open('student.txt','a')
#Skriver 3 nye navn til fila
studentfil.write('Olavia\n')
studentfil.write('Oline\n')
studentfil.write('Petrus\n')

#Stengerfila
studentfil.close()
