# Eingabe
print("Bitte geben sie ihr Bruttogehalt ein:")
z = input()
zahl = int(z)

print("Bitte geben sie ihren Familienstand ein: 1 = ledig, 2 = verheiratet")
x = input()
Fstand = int(x)

# Auswertung und berechnung
if zahl > 4000 and Fstand == 1:
    steuersatz = 0.26
elif zahl > 4000 and Fstand == 2:
    steuersatz = 0.22
elif zahl <= 4000 and Fstand == 1:
    steuersatz = 0.22
elif zahl <= 4000 and Fstand == 2:
    steuersatz = 0.18

steuer = zahl * steuersatz


# Ausgabe
print("Sie muessen", steuer, "Euro an Steuern zahlen")
