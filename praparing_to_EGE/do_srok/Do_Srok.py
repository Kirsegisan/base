def Type_14():
    q = '0123456789ABCDE'
    for x in q:
        w = (int('97968' + x + '15', 15) + int('7' + x + '233', 15))
        if w % 14 == 0:
            print(w / 14)


def Type_17():
    with open('ИНФ_Доп.файлы/1/1_17.txt') as file:
        f = [int(line) for line in file]
    count = 0
    q = 1
    max_par = 0
    for j in range(99, 9, -1):
        if j in f:
            q = j
            print(q)
            break
    print(q)
    for i in range(len(f) - 1):
        if (len(str(f[i])) == 2) == (len(str(f[i + 1])) != 2):
            if (f[i] + f[i + 1]) % q == 0:
                count += 1
                max_par = max(max_par, f[i] + f[i + 1])
    print(count, max_par)


def Type_23():
    def f(n, r):
        if n == 15:
            return 0
        if n == r:
            return 1
        if n / 2 >= r and n / 3 >= r:
            return f(n / 3, r) + f(n / 2, r) + f(n - 1, r)
        if n / 3 >= r:
            return f(n / 3, r) + f(n - 1, r)
        if n / 2 >= r:
            return f(n / 2, r) + f(n - 1, r)
        if n - 1 >= r:
            return f(n - 1, r)
        return 0


    print(f(25, 11) * f(11, 1))


def Type_24():
    with open('ИНФ_Доп.файлы/1/1_24.txt') as file:
        f = file.read()
    abc = 'ABC'
    q = 1
    q_max = 0
    for i in range(len(f) - 1):
        if f[i] in abc and f[i + 1] in abc:
            q_max = max(q, q_max)
            q = 1
        else:
            q += 1
    print(q_max)


def Type_25():
    w = '0 1 2 3 4 5 6 7 8 9'
    q = [''] + w.split()
    w = w.split()
    for i in w:
        for j in w:
            for r in q:
                num = int('12' + i + j + '1' + r + '56')
                if num % 317 == 0:
                    print(num, num // 317)


def Type_26():
    with open('ИНФ_Доп.файлы/1/1_26.txt') as file:
        n = int(file.readline())
        r = file.readline()
        f = [line.strip().split() for line in file]
    luggage_storage = [0 for i in range(n)]
    f.sort()
    print(luggage_storage)
    print(r)
    print(f)
    count = 0
    last_box = 0
    f[0] = int(f[0][0]), int(f[0][1])
    time = f[0][0]
    for client in range(1, len(f)):
        f[client] = int(f[client][0]), int(f[client][1])
        time += f[client][0] - f[client - 1][0]
        for i in range(len(luggage_storage)):
            if luggage_storage[i] < time:
                luggage_storage[i] = 0
        if 0 in luggage_storage:
            luggage_storage[luggage_storage.index(0)] = f[client][1]
            count += 1
            last_box = luggage_storage.index(f[client][1])
    print(luggage_storage)
    print(count, last_box)


Type_26()
