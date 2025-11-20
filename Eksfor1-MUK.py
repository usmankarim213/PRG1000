fortsettelse='Ja'
while fortsettelse=='Ja':
    #Hvor mye koffein skal det være
    koffein_mengde=float(input('Oppgi mengden koffein i mg i drikken: '))
    
    #Koffeininnholdet skal være mellom 30 og 130 mg
    if 30<=koffein_mengde<=130:
        
        #Størrelsen på drikken
        desiliter=float(input('Oppgi størrelse på drikke i dl: '))
        
        #Størrelsen på drikken skal være mellom 0,3 og 5 dl
        if 0.3<=desiliter<=5:
            
            #Multiplisere drikkestørrelsen og koffeinmengden
            totalt_koffein=koffein_mengde*desiliter
        
            print("Koffeininnholdet i kroppen etter en enhet er",format(totalt_koffein,".1f"))
            #Beregne koffeinnivået ditt i kroppen etter en time
            koffein_etter_1_time=totalt_koffein*0.87
            print("Koffeininnholdet i kroppen etter en time er",format(koffein_etter_1_time,".1f"))
            #Beregne koffeinnivået ditt i kroppen etter fem timer
            koffein_etter_5_timer=totalt_koffein*(0.87**5)
            print("Koffeininnholdet i kroppen etter fem timer er",format(koffein_etter_5_timer,".1f"))
            #Beregne koffeinnivået etter inntak hver time i 12 timer
            koffein_nivå=0
            antall_timer=13
            for time in range(antall_timer):
                koffein_nivå*=0.87 #Redusere koffeininnholdet med 13% per time
                koffein_nivå+=totalt_koffein   
            print("Koffeininnholdet i kroppen etter 12 timer er",format(koffein_nivå,".1f"))

        else:
            print('Ugyldig drikkestørrelse. Oppgi en verdi mellom 0.3 og 5 dl.')
    else:
        print('Ugyldig mengde koffein. Oppgi en verdi mellom 30 og 130 mg.')

    fortsettelse=input("Vil du fortsette? (Ja/Nei): ")
    print("Program avsluttet")
