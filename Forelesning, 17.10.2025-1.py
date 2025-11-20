#Introduksjon til GUI-programmering
#Grunnstruktur
#Med komponentene ledetekst, inndatafelt, utdatafelt og knapp.
#Så legger vi på kode for å foreta "beregningene"
#Varble må knyttes til inndatafeltene og utdatafeltene før plassering i grid
#Lage en avslutt knapp for å slippe å bruke "Lukk vindu"
from tkinter import * #Importer alt

def beregn_lan():
    if (int(egenkapital.get())/int(kjopesum.get()))>=0.35:
        lanetilsagn.set("Lån innvilges")
    else:
        lanetilsagn.set("Lån innvilges ikke")





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

#window.mainloop()

#Dette er en evigvarende løkke, helt til vi trykker på avslutt på vinduet
#Vi kjørte programmet og jeg fikk som resultat av dette, et lite vindu med tk som filnavn.
#Vi kjørte programmet en gang til etter vi skrev window.title vi fikk som svar endring på tk som filnavn og det endret seg til Lånekalkulator billån

#Vi lager inndatafelt for kjøpesum og egenkapital
kjopesum=StringVar()
ent_kjopesum=Entry(window,width=9,textvariable=kjopesum)
ent_kjopesum.grid(row=0,column=1,padx=100,pady=15)
#ent står for Entry
egenkapital=StringVar()
ent_egenkapital=Entry(window,width=9,textvariable=egenkapital)
ent_egenkapital.grid(row=1,column=1,padx=100,pady=150)

#Vi lager knapp for å beregne
btn_beregn=Button(window,text="Beregn lånetilsagn",command=beregn_lan)
btn_beregn.grid(row=2,columnspan=2,pady=15)

#og vi lager utdatafelt/visningsfelt for konklusjon på lånetilsagnet
lanetilsagn=StringVar()
ent_lanetilsagn=Entry(window,width=20,state="readonly",textvariable=lanetilsagn)
ent_lanetilsagn.grid(row=3,column=1,padx=100,pady=15)


#Knapp for å avslutte.
btn_avslutt=Button(window,text="Program Avslutt",command=window.destroy)
btn_avslutt.grid(row=5,column=0,columnspan=2,pady=15)








window.mainloop()
