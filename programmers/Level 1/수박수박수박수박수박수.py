def solution(n) :
    answer = []
    for i in range(1, n + 1) :
        if i % 2 == 0 :
            answer.append('박')
        else :
            answer.append('수')
    answer = ''.join(answer)
    return answer