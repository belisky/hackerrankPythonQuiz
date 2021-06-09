def lshapes(r, c):
    for i in range(r + 1):
        for j in range(c + 1):
            return mat[i][j]
        print("\n")


t = int(input())
mat = []
r, c = map(int, input().rstrip().split())
for i in range(r):
    mat.append(int, input().rstrip().split())
for i in range(t):
    lshapes(r, c)
    print(lshapes(r, c))