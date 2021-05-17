"""
https://cses.fi/problemset/task/1090
"""
n, x = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()
cnt = 0
l, r = 0, n-1
while l <= r:
    if weight[l]+weight[r] <= x:
        l, r = l+1, r-1
    else:
        r -= 1
    cnt += 1
print(cnt)
