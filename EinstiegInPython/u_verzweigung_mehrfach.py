# Eingabe
print("Bitte ihr Bruttogehalt eingeben:")
z = input()
zahl = int(z)

if zahl >= 4000:
    steuern = zahl * 0.26
elif zahl <= 2499:
    steuern = zahl * 0.18
else:
    steuern = zahl * 0.22

# Ausgabe
print("Sie müssen", steuern, "Euro an Steuern zahlen") 
