# Wert
prozent = 0.18

# Eingabe
print("Bitte geben sie ihr Bruttogehalt ein:")
gehalt = input()
brutto = int(gehalt)

# Berechnung
steuer = brutto * prozent

# Ausgabe
print("Sie müssen ", steuer, "Euro an Steuern zahlen.")
