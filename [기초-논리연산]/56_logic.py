i, j = map(int, input().split())
i = bool(i)
j = bool(j)
print((i and (not j)) or ((not i) and j))
