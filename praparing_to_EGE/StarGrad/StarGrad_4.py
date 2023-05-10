from turtle import *


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


def Type_6():
    t = Turtle()
    t.left(90)
    z = 20
    q = 80
    t.speed(0)
    while True:
        t.down()
        count = 0
        q += 1
        t.begin_fill()
        for i in range(4):
            t.forward(q * z)
            t.right(90)
            t.forward(q * z)
            t.left(90)
            t.forward(q * z)
            t.right(90)
        t.goto(-1, -1)
        t.goto(0, 0)
        t.end_fill()
        t.up()
        convas = getcanvas()
        w = convas.find_overlapping(-1, 1, -1, 1)
        e = convas.find_overlapping(q * z * 1.5, - q * z // 2, q * z * 1.5, q * z // 2)
        w = w[1]
        for x in range(- q, q * 4 + 1):
            for y in range(- q * 2, q * 3 + 1):
                t.goto(x * z, y * z)
                s = convas.find_overlapping(x * z, -y * z, x * z, -y * z)
                t.dot(2, 'Blue')
                if (not w in s) and (e[0] in s):
                    count += 1
                    t.dot(3, "Red")
        t.clear()
        t.goto(0, 0)
        if count >= 1000:
            print(q)
            break


def Type_7():
    print(2 ** 23 / (1.5 * 2 ** 13) * 60)
    print(40960 * 2 ** 10 * 10 ** 3 * 0.2)
    print(8388608000 / (20 * 2**23))


Type_7()
