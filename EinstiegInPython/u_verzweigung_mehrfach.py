# Eingabe
print("Bitte geben Sie Ihr Gehalt ein:")
rawIn = input()

# Umwandeln
brutto = int(rawIn)

# Berechnung

nettoSteuer = 0
steuer = 0

if brutto < 2500 and brutto > 0:
    steuer = 18
    nettoSteuer = (brutto / 100) * 18
elif brutto > 2500 and brutto < 4000:
    steuer = 22
    nettoSteuer = (brutto / 100) * 22
elif brutto > 4000:
    steuer = 26
    nettoSteuer = (brutto / 100) * 26
else:
    print("Sie erhalten kein Gehalt. Dumme Sache.")

# Ausgabe
print("Bei einem Gehalt von", brutto, "ergibt sich eine Steuer von", steuer, "Prozent, sie zahlen", nettoSteuer, "Euro an Steuern.")
