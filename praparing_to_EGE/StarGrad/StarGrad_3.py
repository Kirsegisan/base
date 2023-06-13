from turtle import *
from itertools import permutations


def Type_2():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    ...
                    #if not (((x <= y) or (z <= w)) and ((z == y) <= (w == x))):
    print('2) yxwz')


# def Type_5():
#     for i in range(15432098, 2448567090):
#         n = i
#         r = [int(j)for j in str(n)]
#         for j in range(3):
#             if sum(r) % 2 == 0:
#                 n *= 2
#                 r = [int(j) for j in str(n)]

def Type_6():
    t = Turtle()
    s = 10
    tracer(0)
    for i in range(3):
        t.forward(7 * s)
        t.right(90)
    t.forward(10 * s)
    for i in range(3):
        t.left(90)
        t.forward(6 * s)
    t.up()
    count = 0
    canves = getcanvas()
    for x in range(-50, 50):
        x = x * s
        for y in range(-50, 50):
            y = y * s
            if len(canves.find_overlapping(x, -y,x, -y)) >= 1:
                count += 1
            t.goto(x, y)
            t.dot(4)
    tracer(1)
    while True:
        print(count)


def Type_12():


    def f(a):
        while not "00" in a:
            if "011" in a:
                a = a.replace('011', '101', 1)
            else:
                a = a.replace('01', '40', 1)
                a = a.replace('02', '20', 1)
                a = a.replace('0222', '1401', 1)
        return a


    # q = '12'
    """
    Подбором
    """
    # while True:
    #     r = []
    #     print('ok')
    #     q += '12'
    #     w = list(permutations(q))
    #     for a in w:
    #         if r.count(a) <= 1:
    #             a = '0' + "".join(a) + '0'
    #             q = a
    #             r += a
    #             a = f(a)
    #
    #             if a.count('1') == 6 and a.count('2') == 9:
    #                 print(q, 'ok', a.count('4'))
    print(f('01112221112221112220'))


if __name__ == "__main__":
    Type_12()

