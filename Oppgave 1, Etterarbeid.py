#Oppgave 1. Etterarbeid.

leie_av_bane=2500
tillegg_pr_deltaker=420

antall_deltakere=int(input("Hvor mange deltakere er det?"))


if antall_deltakere>=20:
    tillegg_pr_deltaker=350
else:
    if antall_deltakere>=10:
        tillegg_pr_deltaker=380




totalpris=leie_av_bane+tillegg_pr_deltaker*antall_deltakere

#Ny pris strategi


if antall_deltakere>=9:
    leie_av_bane=3500
    tillegg_pr_deltaker=350
else:
    if antall_deltakere>=10 and antall_deltakere>=19:
        leie_av_bane=2000
        tillegg_pr_deltaker=40

if antall_deltakere>=20:
    leie_av_bane=1000
    tillegg_pr_deltaker=450


totalpris=leie_av_bane+tillegg_pr_deltaker*antall_deltakere

print("Antall deltakere:", antall_deltakere)
print("Pris pr deltaker:", tillegg_pr_deltaker, "kr")
print("Totalprisen blir da", totalpris, "kr")
print("Banen koster da",leie_av_bane,"kr")
