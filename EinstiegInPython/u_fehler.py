# Inch-Wert
inch = 2.54
fehler = 1

while fehler==1:
    # Eingabe
    print("Bitte einen inch-Wert eingeben:")
    wertIn = input()

    try:
        # Versuch Umwandlung
        wert = float(wertIn)
        fehler = 0

        # Berechnung
        cm = wert * inch

        # Ausgabe
        print(wertIn, "inch entsprechen", cm, "cm.")

    except:
        print("Fehlerhafte Eingabe, bitte erneut versuchen.")
