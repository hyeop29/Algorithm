# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T + 1) :
    temp_list = map(int, input().split())
    answer = 0
    for temp in temp_list :
        if temp % 2 != 0 :
            answer += temp

    print("#" + str(i), str(answer))
