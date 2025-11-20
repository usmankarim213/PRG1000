#Program 4-14 (farts_måler)

starts_fart=60
slutts_fart=131
øke=10
konvertingsfaktor=0.6214

print("KPH\tMPH")
print("--------------")

for kph in range(starts_fart,slutts_fart,øke):
    mph=kph*konvertingsfaktor
    print(f"{kph}\t{mph:1f}")
