q = '0123456789ABCDE'
for x in q:
    w = (int('97968' + x + '15', 15) + int('7' + x + '233', 15))
    if w % 14 == 0:
        print(w / 14)
