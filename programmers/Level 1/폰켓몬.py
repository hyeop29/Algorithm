def solution(nums) :
    answer = []
    for i in nums :
        if i not in answer :
            answer.append(i)
            if len(answer) == len(nums) // 2 :
                break
            
    return len(answer)

"""
min을 활용한 다른 사람 풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
"""
