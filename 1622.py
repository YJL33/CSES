"""
see https://cses.fi/problemset/task/1622
"""
from itertools import permutations
x = str(raw_input())
seen = {}
perm = permutations([i for i in range(len(x))])
for p in perm:
    c = ''.join([x[j] for j in p])
    if c not in seen:
        seen[c] = 1

res = seen.keys()
res.sort()

print(len(res))
for c in res:
    print(c)
