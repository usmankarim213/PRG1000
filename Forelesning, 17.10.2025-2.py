#Introduksjon til GUI-programmering
#Grunnstruktur
#Med komponentene ledetekst, inndatafelt, utdatafelt og knapp.


from tkinter import * #Importer alt
#Så lager vi oss et vindu
#Det er av typen Tk
window=Tk()
#Vi gir vinduet et navn
window.title("Lånekalkulator billån")

#Vi lager ledetekster for kjøpesum, egenkapital og lånetilsagn
lbl_kjopesum=Label(window,text="Kjøpesum:")
lbl_kjopesum.grid(row=0,column=0,padx=100,pady=15)

lbl_egenkapital=Label(window,text="Egenkapital:")
lbl_egenkapital.grid(row=1,column=0,padx=100,pady=15)

lbl_lanetilsagn=Label(window,text="Lånetilsagn:")
lbl_lanetilsagn.grid(row=3,column=0,padx=100,pady=15)
#lbl er forkortelse for Label


#Windows løkka:
window.mainloop()
#Dette er en evigvarende løkke, helt til vi trykker på avslutt på vinduet
#Vi kjørte programmet og jeg fikk som resultat av dette, et lite vindu med tk som filnavn.
#Vi kjørte programmet en gang til etter vi skrev window.title vi fikk som svar endring på tk som filnavn og det endret seg til Lånekalkulator billån

