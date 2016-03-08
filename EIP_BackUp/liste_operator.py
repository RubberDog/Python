# zwei Listen
fr = ["Paris","Lyon","Marseille"]
it = ["Rom","Pisa"]

# listen zusammensetzen
stadtliste = fr + it * 2
print(stadtliste)

# liste teilweise durchlaufen
for stadt in stadtliste[3:6]:
    print(stadt)
