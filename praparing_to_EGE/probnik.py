import time
#from openpyxl import*
from turtle import*
from typing import List


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


def Type_25_27422():
    for number in range(174457, 174506):
        flag = 1
        for i in range(2, int((number // 2) ** 0.5) + 1):
            if number % i == 0:
                flag -= 1
                result = (i, number // i)
        if not flag:
            print(result)


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
    with open("Type_17/17_40733.txt") as file:
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


def Type_2_29109():
    #((z → w) ∨ (y ≡ w))∧((x∨z) ≡ y)
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if (((z <= w) or (y == w)) and ((x or z) == y)) == 1:
                        print(z, y, x, w)


def Type_2_12604558():
    #¬(y→x)∨(z→w)∨¬z
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if not ((not(y <= x)) or (z <= w) or not z):
                        print(y, x, z, w)


def Type_5_12604558():
    a = 0
    q = 0
    while not q > 115:
        a += 1
        q = bin(a)[2:]
        if q[-1] == '0':
            q = q + '00'
        else:
            q = q + '11'
        q = int(q, 2)
        print(a, q)


def Type_6_12604558():
    t = Turtle()
    count = 0
    z = 10
    tracer(0)
    t.left(90)
    t.begin_fill()
    for i in range(6):
        t.right(36)
        t.forward(10 * z)
        t.right(36)
    t.end_fill()
    t.up()

    convas = getcanvas()

    for x in range(-1000, 1000):
        for y in range(-1000, 1000):
            s = convas.find_overlapping(x*z, y*z, x*z, y*z)
            if len(s) == 1:
                count += 1

    tracer(1)
    while True:
        t.forward(1000)
        print(count)


def Type_7_12604558():
    #?
    print((2 * 2**23 // 2048 - (640 * 2**13)) // (1024 * 768))


def Type_8_12604558():
    print(6*5*4*8 + 6*5*16)


def Type_12_12604558():
    a = '7' * 40 + '9' * 40 + '4' * 50
    while '49' in a or '97' in a or '47' in a:
        if '47' in a:
            a = a.replace('47', '74', 1)
        if '97' in a:
            a = a.replace('97', '79', 1)
        if '49' in a:
            a = a.replace('49', '94', 1)
    print(a[25], a[71], a[105])


def Type_14_12604558():
    a = 3 * 216**4 + 2 * 36**6 - 648
    count = 0
    while a:
        if a % 6 == 5:
            count += 1
        a = a // 6
    print(count)


def Type_16_12604558():
    def f(n):
        if n == 1:
            return 1
        return f(n-1) * f(n-1) - f(n-1) * n + 2 * n
    print(f(4))


def Type_17_12604558():
    with open("Type_17/17 (12604558).txt") as file:
        f = [int(f) for f in file]
    count = 0
    max_number = -20001
    for i in range(len(f) - 1):
        if f[i] % 3 == 0 or f[i + 1] % 3 == 0:
            count += 1
            max_number = max(max_number, abs(f[i] - f[i + 1]))
    print(count, max_number)


def Type_23_12604558():
    def f(n):
        if n == 5 or n == 10:
            return 0
        if n == 2:
            return 1
        if n % 2 == 0:
            return f(n // 2) + f(n - 3) + f(n - 1)
        if n - 3 >= 2:
            return f(n - 3) + f(n - 1)
        return 0
    print(f(14))


def Type_24_12604558():
    vivod = 0
    with open("Type_24/24(12604558).txt") as file:
        f = [str(f)[:-2] for f in file]

    for line in f:
        if line.count('A') < 25:
            count = 0
            for i in range(len(line) - 1):
                for j in range(i, len(line)):
                    if line[i] == line[j]:
                        count = max(count, j - i)
            vivod = max(count, vivod)
    print(vivod)


def Type_25_12604558():
    for number in range(2000000, 3000000 + 1):
        s = list()
        flag = 0
        for i in range(1, int(number ** 0.5)):
            if number % i == 0:
                q = number // i - i
                if q <= 115:
                    flag += 1
                s.append(q)
        if flag > 2:
            print(number)


def Type_17_37358():
    with open("Type_17/17 (37358).txt") as file:
        f = [int(line) for line in file]
    count = 0
    max_par = -20001
    for i in range(len(f) - 1):
        for j in range(i + 1, len(f)):
            number = f[i] + f[j]
            if number % 10 == 0:
                count += 1
                max_par = max(max_par, number)
    print(count, max_par)


def Type_17_37369():
    with open("Type_17/17 (37369).txt") as file:
        f = [int(line) for line in file]
    count = 0
    max_ras = 0
    for i in range(len(f) - 1):
        for j in range(i + 1, len(f)):
            numbers = abs(f[i] - f[j])
            if numbers % 80 == 0:
                count += 1
                max_ras = max(max_ras, numbers)
    print(count, max_ras)


def Type_17_46975():
    with open("Type_17/17 (46975).txt") as file:
        f = [int(l) for l in file]
    count_add = 0
    count = 0
    max_summ = -20001
    q = 0

    for number in f:
        if number % 2 == 0:
            count_add += 1
            q += number

    srzna = q / count_add

    for i in range(len(f) - 1):
        if f[i] % 3 == 0 and f[i + 1] < srzna:
            count += 1
            max_summ = max(max_summ, abs(f[i] + f[i + 1]))
        elif f[i + 1] % 3 == 0 and f[i] < srzna:
            count += 1
            max_summ = max(max_summ, abs(f[i] + f[i + 1]))
    print(count, max_summ)


def Type_17_39246():
    with open("Type_17/17 (39246).txt") as file:
        f = [int(l) for l in file]
    count = 0
    max_p = -20001
    for i in range(len(f) - 1):
        if (f[i] + f[i + 1]) % 7 == 0 and (f[i] % 5 == 0 or f[i + 1] % 5 == 0):
            count += 1
            max_p = max(max_p, f[i] + f[i + 1])
    print(count, max_p)


def Type_17_40733():
    with open("Type_17/17 (40733).txt") as file:
        f = [int(l) for l in file]
    count = 0
    max_p = -20001
    count_q = 0
    q = 0
    for numsber in f:
        if numsber % 2 == 0:
            count_q += 1
            q += numsber
    q = q / count_q
    for i in range(len(f) - 1):
        if f[i] % 3 == 0 or f[i + 1] % 3 == 0:
            if f[i] < q or f[i + 1] < q:
                count += 1
                max_p = max(max_p, f[i] + f[ i + 1])
    print(count, max_p)


def Type_17_37354():
    with open("Type_17/17 (37354).txt") as file:
        f = [int(line) for line in file]
    count = 0
    max_par = 0
    for i in range(len(f) - 1):
        for j in range(i + 1, len(f)):
            if (f[i] + f[j]) % 2 == 1 and f[i] * f[j] % 5 == 0:
                count += 1
                max_par = max(max_par, f[i] + f[j])
    print(count, max_par)


def Type_17_37357():
    with open("Type_17/17 (37357).txt") as file:
        f = [int(line) for line in file]
    max_par = 0
    count = 0
    for i in range(len(f) - 1):
        for j in range(i + 1, len(f)):
            if (f[i] + f[j]) % 8 == 0:
                count += 1
                max_par = max(max_par, f[i] + f[j])
    print(count, max_par)


def Type_17_37350():
    with open("Type_17/17 (37350).txt") as file:
        f = [int(line) for line in file]
    count = 0
    max_par = 0
    for i in range(len(f) - 1):
        for j in range(i + 1, len(f)):
            if (f[i] + f[j]) % 2 == 1 and f[i] * f[j] % 3 == 0:
                count += 1
                max_par = max(max_par, f[i] + f[j])
    print(count, max_par)


def Type_27_35916():
    with open("Type_27/27_35916.txt") as file:
        f: list[int] = [int(line) for line in file]
    f.sort()
    q = list()
    q.append(f[0])
    q.append(f[1])
    q.append(f[2])
    count = 3
    min_par = 10**9 * 3
    flag = False
    while True:
        for i in range(len(q) - 2):
            for o in range(i + 1, len(q) - 1):
                for p in range(o + 1, len(q)):
                    number = f[i] + f[o] + f[p]
                    if number % 3 == 0:
                        min_par = min(min_par, number)
                        flag = True
        if flag:
            print(min_par)
        q.append(f[count])
        count += 1


def Type_27_46985():
    with open("Type_27/27-A (46985).txt") as file:
        f = [int(line) for line in file]
    #В душе не ебу что такое непрерывная подпоследовательность


def Type_2_12862437():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if (((not x) or y or z) == ((not y) and z and w)) == 1:
                        print(y, w, z, x)


def Type_5_12862437():
    q = 1
    while True:
        n = bin(q)[2:]
        for i in range(2):
            a = n.count('1')
            n = n + f'{a % 2}'
        if int(n, 2) > 85:
            print(q, n)
            break
        q += 1


def Type_6_12862437():
    t = Turtle()
    t.left(90)
    count = 0
    z = 30
    tracer(0)
    t.begin_fill()
    for i in range(4):
        t.forward(6 * z)
        t.right(150)
        t.forward(6 * z)
        t.right(30)
    t.end_fill()
    t.up()
    convas = getcanvas()
    for x in range(-10, 10):
        for y in range(-10, 10):
            s = convas.find_overlapping(x * z, -y * z, x * z, -y * z)
            t.goto(x * z, y * z)
            t.dot(2, 'Red')
            print(s)
            if not (4 in s) and 3 in s:
                t.dot(6, 'Blue')
    tracer(1)
    while True:
        pass


def Type_12_12862437():
    a = '1' * 85
    while '11111' in a:
        a = a.replace('111', '2', 1)
        a = a.replace('222', '1', 1)
    print(a)


def Type_14_12862437():
    a = 7 * 512**1912 + 6 * 64**1954 - 5 * 8**1991 - 4 * 8**1980 - 2022
    count = 0
    while a:
        if a % 8 == 7:
            count += 1
        a = a // 8
    print(count)


def Type_16_12862437():
    def f(n):
        if n == 2 or n == 1:
            return 1
        if n > 2:
            return f(n - 2) * n
    print(f(7))


def Type_17_12862437():
    with open("Type_17/17 (12862437).txt") as file:
        f = [int(line) for line in file]
    count = 0
    max_par = -1
    for i in range(len(f) - 1):
        for j in range(i + 1, len(f)):
            number = f[i] + f[j]
            if f[i] * f[j] % 26 == 0:
                count += 1
                max_par = max(max_par, number)
    print(count, max_par)


def Type_23_12862437():
    def f(n):
        if n == 1:
            return 1
        if n / 2 >= 1 and n - 2 >= 1:
            return f(n / 2) + f(n - 2)
        if n - 2 >= 1:
            return f(n - 2)
        if n / 2 >= 1:
            return f(n / 2)
        return 0
    print(f(16))


def Type_24_12862437():
    with open("Type_24/24(12862437).txt") as file:
        file = file.readline()
        count = 1
        max_count = 0
        for i in range(len(file) - 1):
            if file[i] != file[i + 1]:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
    print(max_count)


def Type_25_12862437():
    for m in range(0, 1000, 2):
        for n in range(1, 1000, 2):
            N = 2 ** m * 3 ** n
            if 400_000_000 <= N <= 600_000_000:
                print(N)


def Type_26_12862437():
    with open("Type_26/26_12862437.txt") as file:
        f = [line for line in file]
    s = 9537
    q = []
    w = 0
    for i in range(1, len(f)):
        q.append(int(f[i]))
    q.sort()
    print(q)
    for l in range(len(q)):
        if w + q[l] <= s:
            w += q[l]
        else:
            print(w, q[l], l)
            break


def Type_27_12862437():
    with open("Type_27/27-B (12862437).txt") as file:
        f = [int(line) for line in file]
    n = f[0]
    f = f[1:]
    count = 0
    q = 0
    mas = [1] + [0] * 29
    for i in range(n):
        q += f[i]
        count += mas[q % 30]
        mas[q % 30] += 1

    print(count)


if __name__ == '__main__':
    Type_17_12862437()
