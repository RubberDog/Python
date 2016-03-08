# Inch-Wert
inch = 2.54

# Eingabe
print("Bitte einen inch-Wert eingeben:")
wertIn = input()

# Umwandlung in Zahl
wert = float(wertIn)

# Berechnung
cm = wert * inch

# Ausgabe
print(wertIn, "inch entsprechen", cm, "cm.")
