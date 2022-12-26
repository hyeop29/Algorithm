def solution(arr1, arr2) :
    answer = []
    for i in range(0, len(arr1)):
        answer.append([])
        for j in range(0, len(arr1[i])) :
            answer[i].append(0)
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer

    #for i in range(0, len(arr1)) :
    #    for j in range(0 ,len(arr1[i])) :
    #        answer[i][j] = arr1[i][j] + arr2[i][j]
    #return answer

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))