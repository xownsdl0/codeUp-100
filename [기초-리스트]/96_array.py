arr = [[0]*20 for k in range(20)]

for i in range(19):
    n = input().split()
    for j in range(19):
      # 0,0 -> 1,1 시작점 조정하기 위해서 +1
        arr[i+1][j+1] = int(n[j])

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(1, 20):
        if arr[j][y] == 0:
            arr[j][y] = 1
        else:
            arr[j][y] = 0

        if arr[x][j] == 0:
            arr[x][j] = 1
        else:
            arr[x][j] = 0

for i in range(1, 20):
    for j in range(1, 20):
        print(arr[i][j], end=' ')
    print()
