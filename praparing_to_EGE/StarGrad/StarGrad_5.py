from turtle import *
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x or not y) <= (w == z)):
#                     if not((x or not y) == (z <= w)):
#                         print(y, z, x, w)
#

# n = 1
# while True:
#     r = bin(n)[2:]
#     if n % 5 == 0:
#         r = r + bin(5)[2:]
#     else:
#         r = r + '1'
#     if int(r, 2) % 7 == 0:
#         r = r + bin(7)[2:]
#     else:
#         r = r + '1'
#     r = int(r, 2)
#     if r < 1728404:
#         print(r, n)
#     n += 1
# t = Turtle()
# t.left(90)
# a = 1
# z = 10
# n = 0
# t.speed(0)
# while n < 400:
#     t.goto(0,0)
#     t.down()
#     t.begin_fill()
#     for i in range(4):
#         t.forward(a * z)
#         t.right(90)
#         t.forward(3 * z)
#     t.end_fill()
#     t.up()
#     for x in range(-10, 11):
#         for y in range(-10, 11):
#             t.goto(x * z, y * z)
#             t.dot(2, "Red")
#     t.clear()
#     a += 1
# with open('FileToStarGrad№5/27-B.txt') as file:
#     n = int(file.readline())
#     f = [int(line) for line in file]
# # n = f[0]
# # f = f[1:]
# first_list = [[0 for j in range(9)] for i in range(9)]
# q = 0
# count = 0
# for num in f:
#     for i in range(9):
#         for j in range(9):
#             if abs((q % 9 - i) % 9) == abs((num % 9 + j) % 9):
#                 count += first_list[i][j]
#     first_list[q % 9][num % 9] += 1
#     q += 1
# for r in range(9):
#     print(first_list[r])
# print(count)
with open('FileToStarGrad№5/26.txt') as file:
    n = file.readline()
    f = [line.strip().split() for line in file]
parking = [[True] * 80], [[True] * 20]
print(f, parking)
