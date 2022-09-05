arr = [[0]*20 for i in range(20)]

i = int(input())
for i in range(i):
    x, y = input().split()
    arr[int(x)][int(y)] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(arr[i][j], end=' ')
    print()
