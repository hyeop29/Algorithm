def solution(clothes) :
    closet = {}
    for cloth in clothes :
        num = hash(cloth[1])
        closet[num] = 0
    for cloth in clothes :
        num = hash(cloth[1])
        closet[num] += 1
    answer = 1
    for _, i in closet.items() :
        answer *= (i + 1)
    return answer - 1
