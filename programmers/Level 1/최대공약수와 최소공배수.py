def solution(n, m) :
    answer = []
    n_count = 1
    m_count = 1
    for i in range(max(m,n), 0, -1) :
        if n % i == 0 and m % i == 0 :
            answer.append(i)
            break
    new_n = n
    new_m = m
    while (new_n != new_m) :
        if (new_n < new_m) :
            n_count += 1
            new_n = n * n_count               
        else :
            m_count += 1
            new_m = m * m_count
    answer.append(new_n)        
        
    return answer
    
print(solution(2,5))
