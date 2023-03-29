def Type_1():
    print('даевгбжи')


def Type_2():
    def F1(x, y, z, w):
        return (x <= y) == (w or not z)
    def F2(x, y, z, w):
        return (x <= y) and (not w == z)
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if F2(x, y, z, w) == 0 and z == 1:
                        print(x, z, y, w)
    print('xzyw')


def Type_3():
    print(6175829)


def Type_4():
    print(11101001)


def Type_5():

    def f1(n):
        n = int(n, 2)
        odd = 0
        even = 0
        for i in str(n):
            if int(i) % 2 == 0:
                odd += 1
            else:
                even += 1
        return odd, even, n % 2 == 0


    count = 0
    q = 0
    while True:
        q += 1
        n = bin(q)[2:]
        for i in range(3):
            f = f1(n)
            if f[0] > f[1]:
                n = n + '1'
            elif f[0] < f[1]:
                n = n + '0'
            else:
                if f[2]:
                    n = n + '0'
                elif not f[2]:
                    n = n + '1'
        n = int(n, 2)
        if 123455 <= n <= 987654321:
            count += 1
            print(count, end='  ')


Type_5()
