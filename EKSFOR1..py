#Eksamensoppgave
fortsettelse='ja'
 
while fortsettelse=='ja':
    #hvor mye koffein skal det være
    mengden_koffein_mg=float(input('Oppgi mengden koffein i mg i drikken: '))
 
    #koffein innholde skal være mellom 30 og 130 mg
    if 30 <= mengden_koffein_mg <=130:
 
        #størrelsen på drikken
        drikke_størrelse=float(input('Oppgi størrelse på drikke i dl:'))
 
        #størrelsen på drikken skal være mellom 0,3 og 5dl
        if 0.3 <=drikke_størrelse <=5:
 
            #Multiplisere drikkestørrelsen og koffeinmengden
            totalt_koffein=mengden_koffein_mg*drikke_størrelse
            print("Koffeininnholdet i kroppen etter en enhet er", totalt_koffein,"mg")
 
 
            #Beregne koffeinnivået ditt i kroppen etter en time
            koffein_nivå_etter_en_time=totalt_koffein*0.87
            print("Koffeininnholdet i kroppen etter en time er",koffein_nivå_etter_en_time,"mg")
 
            #Beregne koffeinnivået ditt i kroppen etter fem timer
            koffein_nivå_etter_fem_timer=totalt_koffein*(0.87**5)
            print("Koffeininnholdet i kroppen etter fem timer er",koffein_nivå_etter_fem_timer,"mg")
 
            #Beregne koffeinnivået etter inntak hver time i 12 timer
            koffein_nivå=0
            antall_timer=13
            for time in range(antall_timer):
                koffein_nivå *=0.87 #redusere koffeininnholdet med 13% per time
                koffein_nivå += totalt_koffein #koffeininnholdet fra den nye enheten
            print ("Koffeininnholdet i kroppen etter 12 timer er",koffein_nivå,"mg")
 
            
        else:
            print('Ugyldig drikkestørrelse. Oppgi en verdi mellom 0.3 og 5 dl.')
    else:
        print('Ugyldig mengde koffein. Oppgi en verdi mellom 30 og 130 mg.')
 
 
       #Vil brukeren fortsette eller ikke
        fortsettelse=input('Vil du kjøre programmet en gang til? (Ja/Nei): ')
    print('Program avsluttet')  

