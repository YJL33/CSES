"""
see https://cses.fi/problemset/task/1618

simply count the number of 5s
"""
# import math

x = int(input())
# print(math.factorial(x))

res = 0
while x//5:
    res += x//5
    x = x//5
# print(x)

print(res)