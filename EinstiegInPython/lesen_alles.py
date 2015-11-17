import sys

# Zugriffsversuch
try:
    d = open("lesen.txt")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Lesen des gesamten Textes
gesamtertext = d.read()

# Schliessen der Datei
d.close()

# Umwandeln in eine liste
zeilenliste = gesamtertext.split(chr(10))

# summieren und ausgeben
summe = 0
for zeile in zeilenliste:
    if zeile:
        summe += float(zeile)
    print(zeile)

# summe ausgeben
print("Summe:", summe)
