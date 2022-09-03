i, j, k, z = map(int, input().split())
r = i
for i in range(0, z-1):
    r = r * j + k

print(r)
