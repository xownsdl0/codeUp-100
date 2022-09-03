from re import I


num = int(input())
sum = 0
i = 0
while True:
    sum = sum + i
    if sum >= num:
        break
    i = i + 1

print(sum)
