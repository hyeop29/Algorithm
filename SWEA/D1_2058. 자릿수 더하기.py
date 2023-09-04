T = int(input())

answer = 0
while(T != 0) :
    answer += T % 10
    T = T // 10

print(answer)
