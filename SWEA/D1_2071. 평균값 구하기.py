def func1(temp) :
    answer = round(sum(temp) / 10)
    return answer


T = int(input())
for i in range(1, T + 1) :
    temp_list = map(int, input().split())
    answer = func1(temp_list)

    print("#" + str(i), str(answer))
