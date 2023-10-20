answer, n, m, words = 99999, 0, 0, []

def dfs(now, target, cnt, visited) :
    global answer
    
    if now == target :
        if answer > cnt :
            answer = cnt
        return
    
    for i in range(n) :
        if visited[i] :
            continue
        count = 0
        for j in range(m) :
            if now[j] == words[i][j] :
                count += 1
            
        if count == m - 1 :
            visited[i] = True
            dfs(words[i], target, cnt + 1, visited)
            visited[i] = False
            
            
def solution(begin, target, _words):
    global words, n, m
    
    words = _words
    if target not in words : # O(50)
        return 0
    
    n = len(words)
    m = len(target)
    visited = [False for _ in range(n)]
    
    dfs(begin, target, 0, visited)
    
    return answer
