def solution(n, arr1, arr2):
    answer = [None] * n
    for i in range(n):
        answer[i] = (bin(arr1[i] | arr2[i]))
        answer[i] = str(answer[i][2:]).zfill(n).replace("1","#").replace("0"," ")

    return answer
