# import sys
# sys.stdin = open("input.txt", "r")

# 인접한 4방향
dxy1 = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우
# 대각선 4방향
dxy2 = [(-1, -1), (-1, 1), (1, -1), (1, 1)] # 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래

INF = float("inf")

def grow() : # o(n*n) 최대 400
    global temp
    temp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n) :
        for j in range(n) :
            cnt = 0
            if gido[i][j] > 0 :
                for dx, dy in dxy1 :
                    nx, ny = i + dx, j + dy
                    if in_range(nx, ny) and gido[nx][ny] > 0 :
                        cnt += 1
                gido[i][j] += cnt
                temp[i][j] = gido[i][j]

def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

def spread() :
    # 먼저 주변에 번식 가능한 칸을 확인한다.
    # o(n*n*4*2) 최대 3,200
    for i in range(n) :
        for j in range(n) :
            cnt = 0
            if gido[i][j] > 0 :
                for dx, dy in dxy1 :
                    nx, ny = i + dx, j + dy
                    # 격자 범위 안이고, 나무나 벽이 없다면 count 한다.
                    if in_range(nx, ny) and gido[nx][ny] == 0 and herbicide[nx][ny] == 0 :
                        cnt += 1

                for dx, dy in dxy1 :
                    nx, ny = i + dx, j + dy
                    if in_range(nx, ny) and gido[nx][ny] == 0 and herbicide[nx][ny] == 0 :
                        temp[nx][ny] += (gido[i][j] // cnt)

    # 임시 배열을 원래 배열로 복사한다.
    for i in range(n) :
        for j in range(n) :
            if temp[i][j] > 0 :
                gido[i][j] = temp[i][j]

def die() :
    global die_tree
    max_die = -INF
    mx, my = -1, -1
    # 가장 많이 박멸되는 칸을 찾는다.
    for i in range(n) :
        for j in range(n) :
            # 제초제 기록도 줄여준다
            if herbicide[i][j] > 0 :
                herbicide[i][j] -= 1
            if gido[i][j] <= 0 :
                continue

            die_count = gido[i][j]
            for dx, dy in dxy2 :
                for q in range(1, k + 1) :
                    nx, ny = i + dx * q, j + dy * q
                    if in_range(nx, ny) and gido[nx][ny] > 0 :
                        die_count += gido[nx][ny]
                    elif in_range(nx, ny) and gido[nx][ny] <= 0 :
                        break

            if max_die < die_count :
                max_die = die_count
                mx, my = i, j

    # c년을 기록
    gido[mx][my] = 0
    herbicide[mx][my] = c
    for dx, dy in dxy2:
        for q in range(1, k + 1):
            nx, ny = mx + dx * q, my + dy * q
            if in_range(nx, ny) and gido[nx][ny] >= 0:
                if gido[nx][ny] == 0 :
                    herbicide[nx][ny] = c
                    break
                gido[nx][ny] = 0
                herbicide[nx][ny] = c
            elif in_range(nx, ny) and gido[nx][ny] < 0:
                break

    if max_die != -INF :
        die_tree += max_die

# T = int(input())
T = 1
for tc in range(1, T + 1) :
    # n : 격자 크기, m : 년 수, k : 제초제 확산 범위, c : 제초제 남아 있는 년수
    n, m, k, c = map(int, input().split())
    gido = [list(map(int, input().split())) for _ in range(n)]
    herbicide = [[0 for _ in range(n)] for _ in range(n)]
    # 번식을 하려면, 임시의 gido가 필요하다.
    temp = [[0 for _ in range(n)] for _ in range(n)]

    die_tree = 0  # 박멸한 나무의 수
    for _ in range(m) :
        # 나무 성장
        grow()
        # 번식 진행
        spread()
        # 박멸 진행
        die()

    print(die_tree)
