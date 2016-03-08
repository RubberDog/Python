print("Laenge des PW?")
x = input()

a = int(x)


print("Klein- und Grossbuchstaben? 0 = nein, 1 ja")
y = input()
m = int(y)

if m == 1:
    b = 52
else:
    b = 26

print("Zahlen verwendet? 0 = nein, 1 = ja")
z = input()
l = int(z)

if l == 1:
    b = b + 10
else:
    b = b

print("Weitere Sonderzeichen verwendet? 0 = nein, 1 = ja")
k = input()
f = int(k)

if f == 1:
	b = 128
else:
	b = b

c = a ** b

c / (7000000000 * 3600 * 24 * 365)

print(c, " Jahre")
