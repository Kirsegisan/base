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


Type_24()
