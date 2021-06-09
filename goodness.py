import math


def goodness(s, n, k):
    count = 0
    for i in range(int(n / 2)):
        if (s[i] != s[n - i - 1]):
            count += 1
    return abs(k - count)


T = int(input())
for i in range(T):
    n, k = map(int, input().rstrip().split())
    s = str(input()).upper()
    goodness(s, n, k)
    print("case #", i + 1, ":", goodness(s, n, k), sep='')