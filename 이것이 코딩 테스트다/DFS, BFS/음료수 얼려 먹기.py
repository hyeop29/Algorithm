N, M = map(int, input().split())
ice = []
result = 0
for _ in range(N) :
  ice.append(list(map(int, input())))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def count(x, y) :
  if x >= 0 and x < N and y >= 0 and y < M and ice[x][y] == 0:
    ice[x][y] = 1
    for i in range(4) :
      count(x + dx[i],y + dy[i])

for i in range(N) :
  for j in range(M) :
    if ice[i][j] == 0 :
      count(i, j)
      result += 1

print(result)
