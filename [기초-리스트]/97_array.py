w, h = map(int, input().split())
n = int(input())

arr = [[0]*h for i in range(w)]

for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for j in range(l):
            arr[x-1][y+j - 1] = 1
    if d == 1:
        for k in range(l):
            arr[x+k-1][y-1] = 1

for i in range(0, w):
    for j in range(0, h):
        print(arr[i][j], end=' ')
    print()
