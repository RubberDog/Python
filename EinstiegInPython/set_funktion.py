# set
s1 = set([8, 15, "x"])
print("Original:", s1)

# kopie
s2 = s1.copy()
print("Kopie:", s2)

# element hinzu
s1.add("abc")
print("Element hinzu:", s1)

# element entnehmen
s1.discard("x")
print("Element entnommen:", s1)

# leeren
s1.clear()
print("geleert:", s1)
