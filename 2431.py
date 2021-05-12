"""
see https://cses.fi/problemset/task/2431
"""
x = int(input())
def helper(n):
    d, num = 0, n           # digit
    while num-9*(d+1)*10**(d) > 0:
        # print('befor:',num, d)
        num -= 9*(d+1)*10**(d)
        d += 1
        # print('after:',num, d)
    # say d = 2, the number lies between 100-999
    # say d = 3, the number lies between 1000-9999
    # print('num, d:',num, d)
    num2 = 10**d + (num-1)//(d+1)
    index = num%(d+1)-1
    # print('n, i', num2, index)
    return str(num2)[index]

for _ in range(x):
    a = int(input())
    print(helper(a))

