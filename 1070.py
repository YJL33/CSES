"""
see https://cses.fi/problemset/task/1070
"""

x = int(input())
if x == 1:
    print(x)
elif x <= 3:
    print("NO SOLUTION")
else:
    res = [b for b in range(x-1, 0, -2)] + [a for a in range(x, 0, -2)]
    # print(res)
    print(" ".join(map(str,res)))
