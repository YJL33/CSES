"""
see https://cses.fi/problemset/task/1083
"""
x = int(input())
a = list(map(int, raw_input().split()))     # use input().split() for python3
s = sum(a)
print((x*(x+1)//2)-s)