def func1(a, b) :
    return a // b, a % b

T = int(input())
for i in range(1, T + 1) :
    a, b = map(int, input().split())
    answer1, answer2 = func1(a, b)

    print("#" + str(i), answer1, answer2)
