#BFS    
def solution(numbers, target):
    child = [0]
    answer = 0
    for num in numbers :
        temp = []
        for c in child :
            temp.append(c + num)
            temp.append(c - num)
        child = temp
    
    for i in child :
        if i == target :
            answer += 1
            
    return answer
