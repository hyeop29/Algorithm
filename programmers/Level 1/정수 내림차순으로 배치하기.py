def solution(n):
    sum = 0
    n = list(str(n))
    n.sort(reverse = True)
    k = len(n) - 1

    for i in n:
        i = int(i)
        sum += i * pow(10,k)
        k -= 1

    return sum

print(solution(118372))