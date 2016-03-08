# Erzeugung
alter = {"Peter":31, "Julia":28, "Werner":35}
print(alter)

# Ersetzen enthalten?
if "Julia" in alter:
    print(alter["Julia"])

# entfernen eines Elements
del alter["Julia"]

# element enthalten?
if "Julia" not in alter:
    print("Julia ist nicht enthalten")

# anzahl elemente
print("Anzahl: ", len(alter))

# aktualisierung mit zweitem dictionary
ualter = {'Moritz': 18, 'Werner': 29}

alter.update(ualter)
print(alter)
