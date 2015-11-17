import shutil, os, glob

# Status 1
print(glob.glob("le*.txt"))

# Datei kopieren
shutil.copyfile("lesen.txt","lesen_kopie.txt")

# Status 2
print(glob.glob("le*.txt"))

# Datei umbenennen
try:
    os.rename("lesen_kopie.txt","lesen.txt")
except:
    print("Fehler beim umbenennen")

# Status 3
print(glob.glob("le*.txt"))

# Datei entfernen
try:
    os.remove("lesen_kopie.txt")
except:
    print("Fehler beim entfernen")

# Status 4
print(glob.glob("le*.txt"))
