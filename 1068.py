"""
see https://cses.fi/problemset/task/1068
implementation
"""
x = int(input())
res = [x]
while x != 1:
    if x%2:
        x = 3*x+1
    else:
        x = x/2
    res += int(x),
print(" ".join(map(str,res)))
