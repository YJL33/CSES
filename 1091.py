"""
https://cses.fi/problemset/task/1091
"""
import time
import collections
import bisect
start = time.time()
f = open('test5.txt', 'r')
n, m = map(int, f.readline().split())                # num of ticket, num of customer
p_tickets = list(map(int, f.readline().split()))
p_customers = list(map(int, f.readline().split()))

# n, m = map(int, input().split())                # num of ticket, num of customer
# p_tickets = list(map(int, input().split()))
# p_customers = list(map(int, input().split()))

# keep a counter and a set of seen prices
# bisect the price when there's one, and maintain the counter and set
# if not, print -1

pcounter = collections.Counter(p_tickets)
plist = list(pcounter.keys())
plist.sort()

res = []
for c in p_customers:
    i = bisect.bisect_left(plist, c)
    if i == len(plist) or plist[i] > c:
        i -= 1
    if i < 0:
        res += '-1',
    else:
        price = plist[i]
        res += str(price),
        pcounter[price] -= 1
        if pcounter[price] == 0:
            del pcounter[price]
            plist.pop(i)
print('\n'.join(res))
print(time.time()-start)