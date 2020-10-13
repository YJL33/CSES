"""
see https://cses.fi/problemset/task/1092
"""
x = int(input())
# if sum is odd, print "NO"
if x%4 != 0 and x%4 != 3:
    print("NO")
# good case
else:
    if x%4 == 0:
        arr = range(1,x+1)
        a = arr[0::2][:x/4] + arr[1::2][x/4:]
        b = arr[1::2][:x/4] + arr[0::2][x/4:]
    elif x%4 == 3:
        arr = range(4,x+1)
        a = [1,2] + arr[0::2][:x/4] + arr[1::2][x/4:]
        b = [3] + arr[1::2][:x/4] + arr[0::2][x/4:]
    print("YES")
    print(len(a))
    print(" ".join(map(str, a)))
    print(len(b))
    print(" ".join(map(str, b)))
