def pot(x, y):
    '"Potenzieren durch Quadrieren und Multiplizieren"'
    result = 1
    while y > 0:
        if y % 2 == 1:
            result *=x
            y -= 1
        else:
            y /= 2
            x *= x

return result
