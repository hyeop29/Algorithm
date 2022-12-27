def solution(n):
    k = 3
    answer_list = []
    answer = 0
    while( n > 0 ):
        answer_list.append(n % k)
        n = n // k
    
    count = len(answer_list) - 1

    for i in answer_list :
        answer += i * pow(k, count)
        count -= 1 

    return answer
