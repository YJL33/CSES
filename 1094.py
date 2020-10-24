"""
see https://cses.fi/problemset/task/1094
"""
x = int(input())
A = list(map(int, raw_input().split()))
prev = A[0]
res = 0
for i in range(1,len(A)):
    prev = max(prev, A[i-1])
    if A[i]<prev:
        res += prev-A[i]
print(res)
