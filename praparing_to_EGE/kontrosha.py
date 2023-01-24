s = ''
r = 0
a = True
for i in range(101, 3000):
    for e in range(2, i):
        if i/e == 0:
            a = False
            break
    if a:
        n = i
        w = n
        n = bin(n)[3::]
        while n != '' and n[0] == '0':
            n = n[1::]
        if n == '':
            n = '0'
        n = int(n, 2)
        n = w - int(n)
        n = str(n)
        if n not in s:
            s = s + '      ' + n
            r += 1
        print(n)
        print(s)
        print(r)
        a = True
        print('ok')

