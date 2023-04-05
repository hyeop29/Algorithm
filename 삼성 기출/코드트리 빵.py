# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque
# 입력 받기
n, m = map(int, input().split())
gido = []
for _ in range(n) :
    gido.append(list(map(int, input().split())))
store = []
for _ in range(m) :
    temp_x, temp_y = map(int, input().split())
    store.append([temp_x - 1, temp_y - 1])

# 현재 사람 위치 확인
people = [[-1, -1] for _ in range(m)]
# 이동 방향
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

visited = [[False] * n for _ in range(n)]
record = [[0] * n for _ in range(n)]

# print("n : {}, m : {}".format(n , m))
# print("gido : {}". format(gido))
# print("store : {}". format(store))

# x, y 가 행렬 범위안인지 구해지는 함수
def in_range(x, y) :
    return 0 <= x and x < n and 0 <= y and y < n

# 최단 거리를 구하기 위한 dfs
def bfs(x, y) :
    for i in range(n) :
        for j in range(n) :
            visited[i][j] = False
            record[i][j] = 0

    q = deque()
    q.append((x, y))
    # print("x : {}, y : {}".format(x, y))
    # print(visited)
    visited[x][y] = True

    while q :
        tx, ty = q.popleft()
        for i in range(4) :
            nx, ny = tx + dx[i], ty + dy[i]
            if in_range(nx, ny) and gido[nx][ny] != 2 and not visited[nx][ny] :
                visited[nx][ny] = True
                record[nx][ny] = record[tx][ty] + 1
                q.append((nx, ny))

def simulation(time) :
    # 1번 상 좌 우 하
    for i in range(m) :
        if people[i] == [-1, -1] or people[i] == store[i] :
            continue

        bfs(store[i][0], store[i][1])

        x, y = people[i]
        min_value = 999
        min_x, min_y = -1, -1
        for j in range(4) :
            nx, ny = x + dx[j], y + dy[j]
            if in_range(nx, ny) and visited[nx][ny] and min_value > record[nx][ny] :
                min_value = record[nx][ny]
                min_x, min_y = nx, ny
        # print("people : {}".format(people))
        # print("time : {}".format(time))
        people[i] = [min_x, min_y]

    # 2번 편의점 도착 편의점에 있는 칸을 지나갈 수 없다
    for i in range(m) :
        if people[i] == store[i] :
            gido[store[i][0]][store[i][1]] = 2

    # 3번 t 시간에 t <= m 을 만족하면 베이스캠프에 진입
    if time < m :
        bfs(store[time][0], store[time][1])
        min_value = 999
        min_x, min_y = -1, -1
        for i in range(n) :
            for j in range(n) :
                if gido[i][j] == 1 and visited[i][j] and min_value > record[i][j] :
                    # print(" !!!! ")
                    min_value = record[i][j]
                    min_x, min_y = i, j
        people[time] = [min_x, min_y]
        gido[min_x][min_y] = 2
        # print("record : {}".format(record))
        # print("visited : {}".format(visited))
        # print("gido : {}".format(gido))
        # print("people : {}".format(people))
        # print("time : {}".format(time))

def check() :
    for i in range(m) :
        if people[i] != store[i] :
            return False
    return True

time = 0
while True :
    if check() :
        break
    simulation(time)
    time += 1

print(time)
