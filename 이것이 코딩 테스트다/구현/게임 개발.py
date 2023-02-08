N, M = map(int,input().split())
x, y, d = map(int,input().split())
# 맵의 외곽은 바다로 된 것을 표현 하기 위해
record = [[0 for j in range(M + 2)] for i in range(N + 2)]
data = [ [1 for j in range(M + 2)] for i in range(N + 2)] 
result = 1 # 현재 있는 한 칸 포함
# 맵의 외곽을 바다로 표현하기 위해 2차원 행렬 사이즈를 크게 만들었으므로 설정 변경
row, col = 1, 1
x += 1
y += 1
check = 0 # 회전한 횟수 기록
record[x][y] = 1 # 자신이 이동한 칸 기록
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 맵의 정보 입력 받는 반복문
for i in range(N) :
  temp = list(map(int,input().split()))
  for j in temp :
    data[row][col] = j
    col += 1
  row += 1
  col = 1

while True : 
  d = (d - 1) % 4  # 왼쪽 방향으로 회전
  # 한 칸 전진
  temp_x = x + dx[d]
  temp_y = y + dy[d]
  check += 1
  if data[temp_x][temp_y] == 0 and record[temp_x][temp_y] == 0:
    x, y = temp_x, temp_y
    record[x][y] = 1
    result += 1
    check = 0
      
  if check == 4 :
    temp_x = x - dx[d]
    temp_y = y - dy[d]
    if data[temp_x][temp_y] == 0 :
      x, y = temp_x, temp_y
      check = 0
    else :
      break

print(result)
