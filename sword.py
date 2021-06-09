import math

import math
def boring(a, b):
    e = (b - a) / 2
    #print(list(str(a))[len(str(a))-1])
    if (list(str(a))[len(str(a))-1]=="9"):
        return math.ceil(e)
    elif ((b%2)&(a%2)==1):
        return math.ceil(e)+1

    return math.ceil(e)


T = int(input())
for i in range(T):
    f, d, = map(int, input().rstrip().split())
    print("case #", i + 1, ":", boring(f, d), sep='')