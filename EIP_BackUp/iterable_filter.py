# funktion, die true oder false liefert
def test(a):
    if a>3:
        return True
    else:
        return False

# Funktion mehrfach aufrufen
z = filter(test, [5, 6, -2, 0, 12, 3, -5])

# ausgabe der werte, die true ergeben
for element in z:
    print("True:", element)
