def solution (x, n):
    answer = []
    j = 0
    for i in range(n) :
        j += x
        answer.append(j)
    return answer