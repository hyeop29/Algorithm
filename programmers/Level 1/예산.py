def solution(d, budget):
    answer = 0
    d.sort()
    print(d)
    for i in d:
        budget = budget - i
        if budget < 0 :
            break
        answer += 1
    
    return answer
