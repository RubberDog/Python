# Berechnung
a = 23
b = 7.5
c = a + b

# normale ausgabe
print("Ergebnis:", a, "+", b, "=", c)

# Ausgabe ohne Zeilenende und Leerzeichen
print("Ergebnis: ", end="")
print(a, "+", b, "=", c, sep="")

# neue zeile
print()

# liste
stadt = ["Hamburg", "Berlin", "Augsburg"]
for x in stadt:
    print(x)
for x in stadt:
    print("Stadt", x, sep="=>", end=" # ")
