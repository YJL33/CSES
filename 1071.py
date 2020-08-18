"""
see https://cses.fi/problemset/task/1071

by observation we can tell there's different "layers"
layer 1: 1
layer 2: 2-4
layer 3: 5-9 .... so on and so forth
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    if max(a, b)%2:
        if a >= b:
            print((a-1)*(a-1) + b)
        else:
            print(b*b - (a-1))
    else:
        if a >= b:
            print(a*a - (b-1))
        else:
            print((b-1)*(b-1) + a)