from collections import deque

def solution(n, computers):
    answer = 0

    queue = deque()
    
    def bfs(x) :
        queue.append(x)
        
        while queue :
            nx = queue.popleft()
            for i in range(n) :
                if computers[nx][i] == 1 :
                    computers[nx][i] = 0
                    queue.append(i)
        
    for i in range(n) :
        for j in range(n) :
            if computers[i][j] == 1 :
                bfs(j)
                answer += 1

    return answer
