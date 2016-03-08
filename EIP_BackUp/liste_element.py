# Originalliste
fr = ["Paris","Lyon","Marseille","Bordeaux"]
print("Original:")
print(fr)

# Ersetzen eines Elementes durch ein Element
fr[2] = "Lens"
print("Element ersetzt:")
print(fr)

# ersetzen eines teilbereiches durch eine liste
fr[1:3] = ["Nancy","Metz","Gap"]
print("Teil ersetzt:")
print(fr)

# entnehmen eines teilbereiches
del fr[3:]
print("Teil entnommen:")
print(fr)

# ersetzen eines Elementes durch eine Liste
fr[0] = ["Paris-Nord","Paris-Sued"]
print("Element durch Liste ersetzt:")
print(fr)
