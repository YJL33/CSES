for _ in range(int(input())):
    a, b = sorted(map(int, input().split()))
    print("YNEOS"[(a+b)%3!=0 or 2*a<b::2])