n, tickets, answer = 0, [], []

def dfs(route, visited) :
    global answer
    
    if len(route) == n + 1 :
        if answer == [] :
            answer = [airport for airport in route] 
        elif route < answer :
            answer = [airport for airport in route] 
        return
    
    for i in range(n) :
        if not visited[i] and route[-1] == tickets[i][0] :
            visited[i] = True
            route.append(tickets[i][1])
            dfs(route, visited)
            visited[i] = False
            route.pop()
    return
    
def solution(_tickets):
    global n, tickets 
    
    tickets = _tickets
    n = len(tickets)
    visited = [False for _ in range(n)]
    
    dfs(["ICN"], visited)
    
    return answer
