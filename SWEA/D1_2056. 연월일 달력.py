check_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def func1(temp_list) :
    answer = ""

    year = int(temp_list[:4])
    month = int(temp_list[4:6])
    day = int(temp_list[6:])

    if 0 < month < 13 and 0 < day < check_day[month - 1] + 1 :
        answer += temp_list[:4] + "/" + temp_list[4:6] + "/" + temp_list[6:]
    else :
        answer = "-1"

    return answer


T = int(input())
for i in range(1, T + 1) :
    temp_list = input()
    answer = func1(temp_list)

    print("#" + str(i), answer)
