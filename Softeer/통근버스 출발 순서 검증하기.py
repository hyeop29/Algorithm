import sys

n = int(input())
bus = list(map(int, input().split()))

temp, result = 0, 0

for i in range(n) :
    for j in range(i + 1, n) :
        if bus[i] < bus[j] :
            temp += 1
        else :
            result += temp
    temp = 0

print(result)
