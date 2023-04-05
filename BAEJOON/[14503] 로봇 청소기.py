n, m = map(int, input().split())
r, c, d = map(int, input().split())

room = []
for _ in range(n) :
    room.append(list(map(int, input().split())))

# 청소한 곳을 기록할 배열
record = [[0 for _ in range(m)] for _ in range(n)]

# 필요한 변수 선언
check = 0
clear = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# x, y가 범위안에 있는지 확인하는 함수
def in_range(x, y) :
    return 0 <= x and x < n and 0 <= y and y < m

while True :
    # step1
    if record[r][c] != 1 :
        record[r][c] = 1
        clear += 1
    # step2
    if check == 4 :
        nx, ny = r - dx[d], c - dy[d]
        if room[nx][ny] != 1 and in_range(nx, ny) :
            r, c = nx, ny
            check = 0
            continue
        else :
            break
    # step3
    for _ in range(4) :
        d = (d - 1) % 4
        nx, ny = r + dx[d], c + dy[d]
        if in_range(nx, ny) and record[nx][ny] != 1 and room[nx][ny] != 1 :
            r, c = nx, ny
            check = 0
            break
        else :
            check += 1

print(clear)
