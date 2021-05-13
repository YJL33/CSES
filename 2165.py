"""
see https://cses.fi/problemset/task/2165
"""
n, s, m, e = int(input()), '1', '2', '3'
def helper(x, start, end, alt):
    if x == 1:
        print(start, end)
    else:
        helper(x-1, start, alt, end)
        print(start, end)
        helper(x-1, alt, end, start)
def calc(x):
    return 2*calc(x-1)+1 if x != 1 else 1

print(calc(n))
print(helper(n,s,e,m))
