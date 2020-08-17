"""
check https://cses.fi/problemset/submit/1754/

say x and y are number of required operations

a + b = sum = 3x + 3y       # mod == 0
a - b = diff = x - y

1/3(a + b) + a - b = 2x
1/3(a + b) - (a - b) = 2y

a + b + 3a - 3b = 6x
a + b - 3a + 3b = 6y

2a - b = 3x
2b - a = 3y
"""

for x in range(int(input())):
    a, b = map(int, input().split())
    if (a + b)%3==0 and (2*a - b)>=0 and (2*b - a)>=0:
        print("YES")
    else:
        print("NO")
