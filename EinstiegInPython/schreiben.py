import sys

# Zugriffsversuch
try:
    d = open("schreiben.txt","w")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# schreiben von einzelnen Strings, mit Zeilenende
d.write("Die erste Zeile\n")
for i in range(2,11,2):
    d.write(str(i) + " ")
d.write("\n")

# schreiben einer Liste
x = ["abc\n", str(12/7.5)+"\n", "xyz\n"]
d.writelines(x)

# schliessen der Datei
d.close()
