#DFS    
def dfs(numbers, target, depth, total) :
    global answer
    
    if depth == len(numbers) :
        if total == target :    
            answer += 1
            return
        else :
            return
    dfs(numbers, target, depth + 1, total + numbers[depth])
    dfs(numbers, target, depth + 1, total - numbers[depth])
    
    
def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, target, 0, 0)
    
    return answer
