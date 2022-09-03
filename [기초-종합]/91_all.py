i, j, k = map(int, input().split())
d = 1

while d % i != 0 or d % j != 0 or d % k != 0:
    d += 1
print(d)
