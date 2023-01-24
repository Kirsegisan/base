def n2():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if ((x and y) or (y and z)) == ((x <= w) and (w <= y)):
                        print(z, x, y, w)


def n5():
    q = 0
    while True:
        q += 1
        n = q
        n = bin(n)
        n = n[2:]
        if n[-1] == '0':
            n += '10'
        else:
            n += '01'
        print(n, int(n, base=2), q)
        if int(n, base=2) == 2018:
            break
n5()