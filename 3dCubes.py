A=[[1,3,4],[2,2,3],[1,2,4]]

def surfaceArea(A):
    # Write your code here
    # Pad the grid width a layer of 0
    # for easier calculation
    a = [[0] * (len(A[0]) + 2)]
    print(a)
    for row in A:
        a.append([0] + row + [0])
    a.append([0] * (len(A[0]) + 2))
    print(a)

    # Bottom and top area
    ans = len(A) * len(A[0]) * 2
    print('this is top & bottom',ans)

    # Side area is just the sum of differences
    # between adjacent cells. Be careful not to
    # count a side twice.
    c=b=0
    for i in range(1, len(a)):
        for j in range(1, len(a[i])):
            c+=abs(a[i][j] - a[i - 1][j])
            print('this is a',i,j,c)
            b+=abs(a[i][j] - a[i][j - 1])
            print('this is a', i, j, b)
    print(c,b,ans)
surfaceArea(A)