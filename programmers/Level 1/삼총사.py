def solution(number) :
    L = []
    answer = 0
    for i in range(len(number) - 2) :
        for j in range(i + 1, len(number) - 1) :
            for q in range(j + 1, len(number)) :
                L.append([number[i], number[j], number[q]])
    
    for i in L :
        if sum(i) == 0 :
            answer += 1
    return answer
