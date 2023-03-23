from turtle import *


def  Type_2():
    #((x ∧ ¬y) ≡ (z ∨ ¬w)) → (x ∧ z)
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if (((x and not y) == (z or not w)) <= (x and z)) == 0:
                        print(y, z, w, x)



def Type_8():
    print(5 * 5 * 4 * 3 * 1)


def Type_12():
    a = '>' + '1' * 26 + '2' * 10 + '3' * 14
    while '>1' in a or '>2' in a or '>3' in a:
        if '>1' in a:
            a = a.replace('>1', '22>', 1)
        if '>2' in a:
            a = a.replace('>2', '2>', 1)
        if '>3' in a:
            a = a.replace('>3', '1>', 1)
    print(a.count('1') + a.count('2') * 2 + a.count('3') * 3)
    print(a)


def Type_14():
    valid_numbers = '0123456789AB'
    for y in valid_numbers:
        for x in valid_numbers:
            number = int(y + 'A' + 'A' + x, 12) + int(x + '0' + '2' + y, 14)
            if number % 80 == 0:
                print(number // 80)


def Type_15():

    def f(n, m):
        if n % m == 0:
            return True
        return False
    a = 1
    #ДЕЛ(120, A) ∧ (¬ДЕЛ(x, А) → (ДЕЛ(x, 18) → ¬ДЕЛ(x, 24)))
    while True:
        for x in range(100000):
            if f(120, a):
                if ((not f(x, a)) <= (f(x, 18) <= (not f(x, 24)))):
                    print(a)
        a += 1



def Type_16():
    def f(n):
        if n <= 2:
            return n
        if n > 2:
            return f(n-1) * f(n - 2)
    print(f(7))


def Type_17():
    count = 0
    max_rasnitsa = -20001
    with open('17_22_03_23.txt') as file:
        for line in file:
            f = [int(line) for line in file]
    for i in range(len(f)):
        for j in range(i + 1, len(f)):
            if (f[i] - f[j]) % 60 == 0 and (f[i] % 15 == 0 or f[j] % 15 == 0):
                count += 1
                max_rasnitsa = max(max_rasnitsa, f[i] - f[j], f[j] - f[i])
    print(count, max_rasnitsa)


if __name__ == "__main__":
    Type_17()
