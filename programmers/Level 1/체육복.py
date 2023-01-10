def solution(n, lost, reverse) :
    answer = [1 for i in range (n)]

    for i in range(len(answer)) :
        if i + 1 in reverse :
            answer[i] += 1
        if i + 1 in lost :
            answer[i] -= 1

    for i in range(len(answer)) :
        if answer[i] == 0 :
            if i > 0 and answer[i-1] == 2:
                answer[i] += 1
                answer[i-1] -= 1
            elif i < len(answer) - 1  and answer[i+1] == 2:
                answer[i] += 1
                answer[i+1] -= 1
    return answer.count(1) + answer.count(2)
