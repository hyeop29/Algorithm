def solution(n, times):
    start, end = 1, max(times) * n
    answer = 0
    
    while start <= end :
        check = 0
        mid = (start + end) // 2
        for time in times :
            check += mid // time
            if check >= n :
                break
    
        if check >= n :
            answer = mid
            end = mid - 1
        else : # check < n 
            start = mid + 1
            
    return answer
