def solution(k, m, score):
    score.sort()
    answer = 0
    for i in range(len(score) - m, -1, -m) :
        answer += score[i] * m
    return answer
