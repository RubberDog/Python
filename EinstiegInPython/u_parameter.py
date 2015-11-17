# Definition der Funktion
def steuer(x):
    if x > 2500:
        prozent = 0.22
    else:
        prozent = 0.18
    print("Sie werden", x * prozent, "Euro an Steuern zahlen")

# Hauptprogramm
steuer(1800)
steuer(2200)
steuer(2500)
steuer(2900)
