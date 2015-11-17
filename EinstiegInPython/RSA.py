def multi(x, y):
    '''Multiplizieren durch Addieren und Verdoppeln'''
    result = 0
    while y > 0:
        if y % 2 == 1:
            #bei ungeraden Werten für die 2. Zahl wird
            #das Zwischenergebnis der 1.Zahl summiert
            result += x
            #die Reduzierung um 1 macht die 2. Zahl
            #wieder gerade und verhindert einen Rest
            #bei der Division durch 2, wobei es hier
            #nur darum geht, in den else-Zweig zu wechseln
            y -= 1
        else:
            x *= 2
            y /= 2
    return result
