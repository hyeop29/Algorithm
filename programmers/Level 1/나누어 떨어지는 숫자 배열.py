def solution (arr, divisor) :
    answer = []
    for i in arr :
        if ( i  % divisor == 0) :
            answer.append(i)
            
    if answer :
        answer.sort()
        return answer
    else :
        answer.append(-1)
        return answer

print(solution([5,9,7,10],5))