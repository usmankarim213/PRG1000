#Gjennomgang i Stålefag, gjennomgang av filer.
#Starting out with python kapittel 6
#Program for å skrive tre navn til en ny fil.

studentfil=open('student.txt','w')

#Skriver 3 navn til fila...
#Hver tekststreng/input slutter med \n escape sequence
#\n er linjeskift
studentfil.write('Torvald\n')
studentfil.write('Kari\n')
studentfil.write('Jens\n')

#Da gjenstår det bare å stenge fila

studentfil.close()
