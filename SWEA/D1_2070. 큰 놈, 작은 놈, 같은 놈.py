def func1(a, b) :
    answer = ""
    if a > b :
        answer = ">"
    elif a < b :
        answer = "<"
    else :
        answer = "="

    return answer


T = int(input())

for i in range(1, T + 1) :
    a, b = map(int, input().split())
    answer = func1(a, b)

    print("#" + str(i), answer)
