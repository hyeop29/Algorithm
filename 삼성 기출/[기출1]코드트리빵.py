# 파입 입출력을 위한 sys / 제출 시 삭제해야함.
import sys
sys.stdin = open("input.txt", "r")

from collections import deque

dxy = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # 상, 좌, 우, 하
INF = float("inf")

gido = [] # 격자의 정보
con = {} # 편의점의 정보
people = {} # 사람의 위치
visited = []
dis = []

def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

def bfs(x, y) :
    global visited, dis
    visited = [[False for _ in range(n)] for _ in range(n)]
    dis = [[0 for _ in range(n)] for _ in range(n)]

    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        nx, ny = q.popleft()
        for dx, dy in dxy:
            tx, ty = nx + dx, ny + dy
            if in_range(tx, ty) and not visited[tx][ty] and gido[tx][ty] != -1:
                dis[tx][ty] = dis[nx][ny] + 1
                visited[tx][ty] = True
                q.append((tx, ty))

def mov() :
    for i in range(m) :
        if people[i] == (-1, -1) or people[i] == con[i] :
            continue

        cx, cy = con[i]
        bfs(cx, cy)

        px, py = people[i]
        min_dis = INF
        mx, my = -1, -1
        for dx, dy in dxy :
            new_x, new_y = px + dx, py + dy
            if in_range(new_x, new_y) and visited[new_x][new_y] and min_dis > dis[new_x][new_y] :
                min_dis = dis[new_x][new_y]
                mx, my = new_x, new_y

        people[i] = (mx, my)
        # 2. 편의점에 도착한다면 해당 칸 이동 불가 상태로 변경
        if people[i] == con[i] :
            cx, cy = con[i]
            gido[cx][cy] = -1

def baseCamp(time) :
    if time <= m :
        cx, cy = con[time - 1]
        bfs(cx, cy)

        min_dis = INF
        mx, my = -1, -1
        for i in range(n) :
            for j in range(n) :
                if gido[i][j] == 1 and visited[i][j] and min_dis > dis[i][j] :
                    min_dis = dis[i][j]
                    mx, my = i, j
        people[time - 1] = (mx, my)
        gido[mx][my] = -1

# testcase 수 입력받기
T = int(input())
# testcase만큼 반복
for tc in range(1, T + 1) :
    # n : 격자크기, m : 사람 수
    n, m = map(int, input().split())
    gido = [list(map(int, input().split())) for _ in range(n)]
    people = {}
    for p in range(m) :
        r, c = map(int, input().split())
        con[p] = (r - 1, c - 1)
        people[p] = (-1, -1)

    time = 0
    while people != con :
        time += 1
        mov()
        baseCamp(time)

    print(time)
