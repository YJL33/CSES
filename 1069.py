"""
see https://cses.fi/problemset/task/1069
"""
x = str(raw_input())
cnt, prev, maxSeen = 0, 'X', 0
for c in x:
    if c == prev:
        cnt += 1
    else:
        prev = c
        cnt = 1
    maxSeen = max(maxSeen, cnt)
print(maxSeen)
