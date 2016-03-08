# sets
s1 = set([8, 2, 5])
s2 = set([2, 8])
s3 = set([2, 5, 8])

print("s1:", s1)
print("s2:", s2)
print("s3:", s3)

# teilmenge, echte teilmenge
if s2 < s1:
    print("s2 ist echte teilmenge von s1")
if s3 <= s1:
    print("s3 ist teilmenge von s1")
