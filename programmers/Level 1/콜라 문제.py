def solution(a, b, n):
    answer = 0
    temp = 0
    while(a <= n) :
        temp = n % a
        n = (n // a) * b
        answer += n
        n = temp + n
    return answer
