from collections import deque

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_range(x, y, n, m) :
    return 0 <= x < n and 0 <= y < m

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    dis = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    
    visited[0][0] = True
    dis[0][0] = 1
    q.append((0, 0))
    
    while q :
        cx, cy = q.popleft()
        for dx, dy in dxy :
            nx, ny = dx + cx, dy + cy
            if in_range(nx, ny, n, m) and not visited[nx][ny] and maps[nx][ny] == 1 :
                visited[nx][ny] = True
                dis[nx][ny] = dis[cx][cy] + 1
                q.append((nx, ny))
    
    if visited[n - 1][m - 1] :
        return dis[n - 1][m - 1]
    
    else :
        return -1
