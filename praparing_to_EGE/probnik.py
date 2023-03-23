import time
#from openpyxl import*
from turtle import*


def Type_5_18785():
    q = 0
    while True:
        q += 1
        n = q
        n = bin(n)
        n = n[2:]
        if n[-1] == '0':
            n = '1' + n
            n += '0'
        else:
            n = '11' + n
            n += '11'
        print(n, q)
        if int(n, base=2) > 52:
             break


def Type_12_16443():
    q = '1' * 84
    while '11111' in q:
        q = q.replace('222', '1', 1)
        q = q.replace('111', '2', 1)
    print(q)


def Type_6_27403():
    q = 100000
    while True:
        s = q
        s = s // 10
        n = 1
        while s < 51:
            s = s + 5
            n = n * 2
        print(n, q, end=' ')
        q -= 1
        if n == 64:
            break


def Type_8_18558():
    count = 0
    for i in range(4):
        for b in range(4):
            for a in range(4):
                for n in range(4):
                    for q in range(4):
                        word = str(i) +str(b) +str(a) +str(n) +str(q)
                        if '1' in word:
                            count += 1
    print(count)


def Type_6_47245():
    t = Turtle()
    t1 = Turtle()
    q = 0
    w = 20
    t.left(90)
    t.speed(0)
    t1.speed(0)

    def turtelight(n, m, p=1):
        for i in range(p):
            t.forward(n * w)
            t.right(m)


    def point(x, y, size=4):
        t1.up()
        t1.goto(x, y)
        t1.dot(size, "#3ae6ca")


    turtelight(10, 60, 6)


    while True:
        for x in range(-q, q):
            point(x * w, -q * w)
        for y in range(-q, q):
            point(q * w, y * w)
        for x in range(q, -q, -1):
            point(x * w, q * w)
        for y in range(q, -q, -1):
            point(-q * w, y * w)
        q += 1


def Type_6_47246():
    t = Turtle
    t.left(90)
    t.speed(0)
    def point(x, y, p=4):
        t.goto(x, y)
        t.dot(p)
    q = 0
    s = 20
    t.forward(14 * s)
    t.right(120)
    while True:
        for x in range(-q, q):
            point(x, -q)
        for y in range(-q, q):
            point(q, y)
        for x in range(q, -q):
            point(x, q)
        for y in range(-q, q):
            point(y, -q)


def Type_14_():
    a = 3 * 4 ** 38 + 2 * 4 ** 23 + 4 ** 20 + 3 * 4 ** 5 + 2 * 4 ** 4 + 1
    n = 0
    count = 0
    while a:
        n = a % 16
        if n == 0:
            count += 1
        a //= 16
    print(count)


def Type_14_45248():
    a = 7 * 512**1912 + 6 * 64**1954 - 5 * 8**1991 - 4 * 8**1980 - 2022
    count = 0
    while a > 0:
        if 7 == a % 8:
            count += 1
        a //= 8
    print(count)


def Typy_14_40989():
    count = 0
    a = 2 * 216**8 + 4 * 36**12 + 6**15 - 1296
    while a > 0:
        if not a % 6:
            count += 1
        a //= 6
    print(count)


def Type_14_40730():
    count = 0
    a = 3 * 125**6 + 2 * 25**9 + 5**12 - 625
    while a > 0:
        if not a % 5:
            count += 1
        a //= 5
    print(count)


def Type_14_35472():
    count = 0
    a = 729**7 + 3**16 - 18
    while a > 0:
        if not a % 9:
            count += 1
        a //= 9
        print(count)


def Type_15_9804():
    for a in range(100):
        for x in range(0, 1024):
            if ((x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0))) != 1:
                break
        else:
            print(a)
            break


def Type_15_34506():
    #x&25 ≠ 0 → (x&17 = 0 → x&А ≠ 0)
    for a in range(100):
        for x in range(1000):
            if ((x & 25 != 0) <= ((x & 17 == 0) <= (x & a != 0))) != 1:
                break
        else:
            print(a)
            break


def Type_15_34508():
    #x & 29 ≠ 0 → (x & 12 = 0 → x & А ≠ 0)
    for a in range(1000):
        for x in range(1000):
            if ((x & 29 != 0) <= ((x & 12 == 0) <= (x & a != 0))) != 1:
                break
        else:
            print(a)
            break


def Type_15_34509():
    for a in range(10000):
        for x in range(10000):
            if (((x & 28 != 0) or (x & 45 != 0)) <= ((x & 17 == 0 ) <= (x & a != 0))) != 1:
                break
        else:
            print(a)
            break


def Type_15_34510():
    #x&25 ≠ 0 → (x&9 = 0 → x&А ≠ 0)
    for a in range(1, 1000):
        for x in range(1000):
            if ((x & 25 != 0) <= ((x & 9 == 0) <= (x & a != 0))) != 1:
                break

        else:
            print(a)
            break


def Type_17_37336():
    numbers = []
    max_pare = -9999999999
    count = 0
    with open('17.txt') as file:
        for number in file:
            numbers.append(int(number))
    for i in range(len(numbers) - 1):
        if numbers[i] % 3 == 0 or numbers[i+1] % 3 == 0:
            count =+ 1
            max_pare = max(max_pare, numbers[i] + numbers[i + 1])
    print(max_pare)


def Type_5_8094():
    for i in range(1, 100000):
        i = bin(i)[2:]
        print(i)
        for j in range(2):
            q = i.count('1')
            print(q)
            print()
            i = i + str(q % 2)
            print(int(i, 2))
        if (int(i, 2)) >= 43:
            print("ответ:",int(i, 2))
            break


def Type_5_15622():
    for i in range(1, 10000):
        i = bin(i)[2:]
        if i.count('1') % 2 == 0:
            i += '00'
        else:
            i += '11'
        if int(i, 2) > 114:
            print(int(i, 2))
            break


def Type_6():
    tracer(10000)
    t = Turtle()
    t.left(90)
    Q = 30
    t.color("black")
    t.begin_fill()
    for x in range(2):
        t.forward(10 * Q)
        t.right(60)
        t.forward(10 * Q)
        t.right(120)
    t.end_fill()
    t.up()
    canvas = getcanvas()
    count = 0
    for x in range(-30, 100):
        for y in range(-30, 100):
            x_1 = x * Q
            y_1 = y * Q
            s = canvas.find_overlapping(x_1, -y_1, x_1, -y_1)
            if 5 in s and 4 not in s:
                t.goto(x_1, y_1)
                count += 1
                t.dot(4, "blue")
            else:
                t.goto(x_1, y_1)
                t.dot(4, "red")
    while True:
        print(count)


def Type_12_9365():
    s = '1' * 39 + '2' * 39
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '1', 1)
    print(s)


def Type_12_14273():
    s = '7' * 85
    while '333' in s or '777' in s:
        s = s.replace('333', '7', 1)
        s = s.replace('777', '3', 1)
    print(s)


def Type_12_13517():
    s = '2' + '8' * 99 + '1'
    while '81' in s or '882' in s or '8883' in s:
        s = s.replace('81', '2', 1)
        s = s.replace('882', '3', 1)
        s = s.replace('8883', '1', 1)
    print(s)


def Type_12_11350():
    s = '8' * 69
    while '3333' in s or '8888' in s:
        s = s.replace('8888', '33', 1)
        s = s.replace('3333', '88', 1)
    print(s)


def Type_12_17378():
    s = '1' * 77
    while '111' in s or '222' in s or '333' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '3', 1)
        s = s.replace('333', '1', 1)
    print(s)


def Type_12_38946():
    s = '1' * 201
    while True:
        q = s
        while '111' in q:
            q = q.replace('111', '22', 1)
            q = q.replace('222', '1', 1)
        if '2' not in q:
            print(s.count('1'))
            break
        s = s + '1'


def Type_12_10290():
    s = '1' + '8' * 80
    while '18' in s or '288' in s or '3888' in s:
        s = s.replace('18', '2', 1)
        s = s.replace('288', '3', 1)
        s = s.replace('3888', '1', 1)
    print(s)


def Type_24_27421():
    with open('24_demo(27421).txt') as file:
        line = file.readline()
    count = 1
    max_count = 0
    for i in range(0, len(line) - 1):
        if line[i] != line[i+1]:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1
    print(max_count)
    count_XY = 0
    max_count_XY = 0
    flag = False
    for i in range(0, len(line) - 1):
        if flag:
            flag = False
            continue
        if line[i] == 'X' and line[i + 1] == 'Y':
            count_XY += 1
            flag = True
        else:
            max_count_XY = max(max_count_XY, count_XY)
            count_XY = 0
    print(max_count_XY)


def Type_24_27689():
    with open('24_demo(27689).txt') as file:
        line = file.readline()
    flag = 0
    count = 0
    max_count_XYZ = 0

    for i in range(0, len(line) - 2):
        if flag:
            flag -= 1
            continue
        if line[i] + line[i + 1] + line[i + 2] == 'XYZ':
            count += 3
            flag = 2
        else:
            if line[i] + line[i + 1] == 'XY':
                count += 2
            elif line[i] == 'X':
                count += 1

            max_count_XYZ = max(max_count_XYZ, count)
            count = 0
    print(max_count_XYZ)


def Type_24_33103():
    count = 0
    with open('24_demo(33103).txt') as file:
        for line in file:
            if line.count('A') > line.count('E'):
                count += 1
    print(count)


def Type_24_33526():
    with open('24_demo(33526).txt') as file:
        line = file.readline()
    counts = {count: 0 for count in 'QWERTYUIOPLKJHGFDSAZXCVBNM'}
    for i in range(1, len(line) - 1):
        if line[i - 1] == line[i + 1]:
            counts[line[i]] += 1
    print(counts)


def Type_24_47391():
    t = Turtle()
    s = 20
    t.left(90)
    t.begin_fill()
    t.color('blue')
    for i in range(14):
        t.right(60)
        t.forward(2 * s)
        t.right(60)
        t.forward(2 * s)
        t.right(270)
    t.up()
    t.end_fill()
    canvas = getcanvas()
    for x in range(-10, 10):
        for y in range(-10, 10):
            sr = canvas.find_owerlaping(x, -y, x, -y)
            t.goto(x, y)
            t.dot(4)


def Type_6_47210():
    t = Turtle()
    tracer(0)
    s = 10
    t.left(90)
    t.begin_fill()
    for i in range(3):
        t.forward(10 * s)
        t.right(120)
    t.end_fill()
    t.up()
    count = 0
    canvas = getcanvas()
    for x in range(-50, 50):
        for y in range(-50, 50):
            x_1 = x * s
            y_1 = y * s
            q = canvas.find_overlapping(x_1, -y_1, x_1, -y_1)
            if 4 not in q and 5 in q:
                t.goto(x_1, y_1)
                t.dot(2, "red")
                count += 1
            else:
                t.goto(x_1, y_1)
                t.dot(2, "blue")
            print(q)


    tracer(1)
    while True:
        print(count)


def Type_6_47245():
    t = Turtle()
    tracer(0)
    s = 20
    t.left(90)
    t.begin_fill()
    for i in range(3):
        t.forward(9 * s)
        t.right(120)
    t.end_fill()
    t.up()
    convas = getcanvas()
    count = 0
    for x in range(-100, 100):
        x = x * s
        for y in range(-100, 100):
            y = y * s
            q = convas.find_overlapping(x, -y, x, -y)
            if 5 in q and 4 not in q:
                t.goto(x, y)
                t.dot(2, "red")
                count += 1
            else:
                t.goto(x, y)
                t.dot(2, "blue")
    tracer(1)
    while True:
        print(count)


def Type_23_3623():
    def find_paths(n):
        if n == 3:
            return 1
        elif n % 3 == 0:
            return find_paths(n // 3) + find_paths(n - 3)
        return 0
    print(find_paths(93))


def Type_23_7315():
    def find_paths(n):
        if n == 1:
            return 1
        if n % 2 == 1:
            return find_paths((n - 1) // 2) + find_paths(n - 1)
        return find_paths(n // 2) + find_paths(n - 1)

    print(find_paths(15))


def Type_23_47227():
    def find_paths(n):
        if n == 1:
            return 1
        if n % 2 == 0:
            return find_paths(n / 2) + find_paths(n - 1)
        if n - 1 >= 1:
            return find_paths(n - 1)
        return 0
    print(find_paths(35))


def Type_23_39252():
    def find_paths(n):
        if n == 2:
            return 1
        if n / 3 >= 2:
            return find_paths(n / 3) + find_paths(n - 1)
        return 0
    print(find_paths(87))


def Type_23_13471():
    def find_paths(n):
        if n == 24:
            return 0
        if n == 1:
            return 1
        if n // 2 >= 1:
            return find_paths(n // 2) + find_paths(n - 1)
        return 0
    print(find_paths(25))


def Type_23_5977():

    def find_paths(n):
        if n == 10:
            return 1
        if n - 10 >= 10:
            return find_paths(n - 10) + find_paths(n - 1)
        return 0
    print(find_paths(33))


# def Type_25_27422():
#     for number in range(174457, 174506):
#         flag = False
#         result = None
#         for i in range(2, (number // 2) ** 0.5):
#             if number % i == 0:
#                 flag = True
#                 result = (i, number // i)
#
#             if flag:
#                 break
#             flag = True
#         else:
#             print(result)


def Type_2_39231():
    #(¬z ≡ y) → ((w ∧ ¬x) ≡ (y ∧ x)) == 0
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if not (not z == y) <= ((w and not x) == (y and x)):
                        print(z, w, x, y)


def Type_2_16377 ():
    # ((x → y) ≡ (y → z)) ∧ (y ∨ w) == 1
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if ((x <= y) == (y <= z)) and (y or w):
                        print(x, z, w, y)


def Type_2_28538():
    # ((x ∧ y) → (¬z ∨ w)) ∧ ((¬w → x) ∨ ¬y) == 0
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if not ((( x and y) <= (not z or w)) and (( not w <= x) or not y)):
                        print(x, y, w, z)


def Type_2_17320():
    #((x ∧ y) ∨ (y ∧ z)) ≡ ((x → w) ∧ (w → z)) == 1
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if ((x and y) or (y and z)) == ((x <= w) and (w <= z)):
                        print(x, w, z, y)


def Type_2_29109():
    #((z → w) ∨ (y ≡ w)) ∧ ((x ∨ z) ≡ y) == 1
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if ((z <= w) or (z == w)) and ((x or z) == y):
                        print(z, y, x, w)


def Type_2_46960():
    #(¬y → (z ≡ w)) ∧ ((z → x) ≡ w) == 1
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if ((not y) <= (z == w)) and ((z <= x) == w):
                        print(z, w, y, x)


def Type_2_15912():
    # ((x → y ) ≡ (z → w)) ∨ (x ∧ w) == 0
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if not (((x <= y) == (z <= w)) or (x and w)):
                        print(z, y, x, w)


def Type_17_40733():
    f = []
    even = 0
    even_count = 0
    with open("17_40733.txt") as file:
        for line in file:
            f += [line]
            if int(line) % 2 == 0:
                even += int(line)
                even_count += 1
    even_count_srar = even // even_count
    count = 0
    max_sum = - 99999
    for i in range(len(f) - 1):
        if int(f[i]) * int(f[i + 1]) % 3 == 0 and (int(f[i]) < even_count_srar or int(f[i + 1]) < even_count_srar):
            count += 1
            max_sum = max(max_sum, int(f[i]) + int(f[i + 1]))
    print(count)
    print(max_sum)

def Type_16_6990():
    def F(n):
        if n == 1:
            return 1
        if n > 1:
            return F(n- 1) + n
        return 0
    print(F(40))


if __name__ == '__main__':
    Type_17_40733()
