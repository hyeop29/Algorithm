def solution(arr) :
    arr.remove(min(arr))
    if not arr :
        arr.append(-1)
    
    return arr

print(solution([4,3,2,1]))