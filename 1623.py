"""
see https://cses.fi/problemset/task/1623
"""
# Python3
from itertools import combinations
x = int(input())
a = list(map(int, input().split()))     # use raw_input().split() for python2
s = sum(a)
res = []
for i in range(1+(x//2)):
    comb = combinations(a, i)
    res += [abs(s-2*sum(c)) for c in comb]
    
print(min(res))