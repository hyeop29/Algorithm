from collections import deque
import time

N , M = map(int,input().split())

miro = []

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

queue =  deque()

def bfs(start) :
  
  x = start[0]
  y = start[1]
  queue.append((x,y))
  
  while queue :
    x1, y1 = queue.popleft()
    for i in range(len(dx)) :
      temp_x = x1 + dx[i]
      temp_y = y1 + dy[i]
  
      if temp_x >=0 and temp_x < N and temp_y >= 0 and temp_y < M and miro[temp_x][temp_y] == 1 :
        miro[temp_x][temp_y] = miro[x1][y1] + 1
        queue.append((temp_x, temp_y))

def dfs(x, y) :
  for i in range(len(dx)) :
    temp_x = x + dx[i]
    temp_y = y + dy[i]

    if temp_x >=0 and temp_x < N and temp_y >= 0 and temp_y < M and miro[temp_x][temp_y] == 1 :
      dfs(temp_x, temp_y)   




for i in range(N) :
  miro.append(list(map(int,input())))

start = time.time()
bfs((0,0))
end = time.time()
print(end - start)
print(miro[N-1][M-1])
print(miro)

start = time.time()
dfs(0,0)
end = time.time()
print(end - start)
print(miro)
