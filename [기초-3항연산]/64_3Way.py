i, j, z = map(int, input().split())
print((i if i < j else j) if ((i if i < j else j) < z) else z)
