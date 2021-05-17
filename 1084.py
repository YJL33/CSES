"""
https://cses.fi/problemset/task/1084
"""
n, m, k = map(int, input().split())
applicants = list(map(int, input().split()))
apartments = list(map(int, input().split()))
applicants.sort()
apartments.sort()

i, j, cnt = 0, 0, 0
while i < m and j < n:
    # apartment too small, i+1
    if applicants[j]-apartments[i] > k:
        i += 1
    # good apartment, skip the applicant, j+1
    elif apartments[i]-applicants[j] > k:
        j += 1
    # assign the apartment, i and j both +1
    else:
        cnt += 1
        i, j = i+1, j+1
print(cnt)
