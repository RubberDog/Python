#!/usr/bin/python
# Syntax: Python 2.6.1
n = int(input('Fakultaet von n = '))
f = 1
for i in range(1, n + 1):
    f = f * i
print('%s! =' % n, f)
