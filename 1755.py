"""
see https://cses.fi/problemset/task/1755
"""
x = str(raw_input())
cd = {}
for c in x:
    if c in cd:
        cd[c] += 1
    else:
        cd[c] = 1

odds = [] if len(x)%2 else [1]

for k in cd.keys():
    if cd[k]%2:
        odds += k,
    if len(odds) > 1:
        print("NO SOLUTION")
        exit()

mid = [""]
if len(x)%2:
    mid = [odds[-1]]
    cd[odds[-1]] -= 1
res = [k*(cd[k]//2) for k in cd.keys()]
pre = res[::-1]
print("".join(map(str, pre+mid+res)))
