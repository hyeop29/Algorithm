from itertools import combinations

def solution(nums) :
    answer = 0
    for i in (combinations(nums, 3)) :
        for j in range(2, sum(i)) :
            if sum(i) % j == 0 :
                break
            elif j == sum(i) - 1 :
                answer += 1
    return answer
