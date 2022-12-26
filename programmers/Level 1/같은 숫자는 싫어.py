def solution(arr) :
    new = arr[0]
    answer = [arr[0]]
    for i in range(1, len(arr)) :
        if arr[i] != new :
            answer.append(arr[i])
            new = arr[i]
    return answer            

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))