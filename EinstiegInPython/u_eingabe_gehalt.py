# Steuer
steuer = 18

# Eingabe
print("Bitte geben Sie Ihr Gehalt ein:")
rawGehalt = input()

# Umwandlung
gehalt = float(rawGehalt)

# Berechnung
steuerbetrag = (gehalt / 100) * 18

# Ausgabe
print("Bei einem Gehalt von", rawGehalt, "Euro und einer Steuer von 18% zahlen Sie", steuerbetrag, "Euro an Steuern.")
