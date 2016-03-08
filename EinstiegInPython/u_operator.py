# Eingaben
print("Bitte geben Sie Ihr Gehalt ein:")
rawGehalt = input()

print("Sind Sie ledig oder verheiratet? Für ledig bitte eine \"1\", für verheiratet bitte eine \"2\" eingeben:")
rawFamilienstand = input()

# Umwandeln
gehalt = int(rawGehalt)
familienstand = int(rawFamilienstand)

# Berechnung
if gehalt <= 4000:
    if familienstand == 1:
        steuersatz = 22
        steuer = (gehalt / 100) * steuersatz
    elif familienstand == 2:
        steuersatz = 18
        steuer = (gehalt / 100) * steuersatz
if gehalt > 4000:
    if familienstand == 1:
        steuersatz = 26
        steuer = (gehalt / 100) * steuersatz
    elif familienstand == 2:
        steuersatz = 22
        steuer = (gehalt / 100) * steuersatz

if familienstand == 1:
    stand = "ledige"
else:
    stand = "verheiratete"

# Ausgabe
print("Bei einem Gehalt von", rawGehalt, "und als", stand, "Person beträgt Ihre Steuer", steuer, "Euro.")
