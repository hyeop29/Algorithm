import sys
sys.stdin = open("input.txt", "r")

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우

dxy2 = [(-1, -1), (0, -1), (1, -1)] # 2는 왼쪽
dxy3 = [(-1, -1), (-1, 0), (-1, 1)] # 3은 위쪽
dxy4 = [(-1, 1), (0, 1), (1, 1)] # 4는 오른쪽
dxy5 = [(1, -1), (1, 0), (1, 1)] # 5는 아래쪽

def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

def check() :
    for i in range(n) :
        for j in range(n) :
            if office[i][j] != 1 :
                continue
            if ice[i][j] < k :
                return False
    return True

def spread2(x, y, power):  # 왼쪽으로 펴지기
    global visited
    if power == 0:
        return
    for i in range(3):
        dx, dy = dxy2[i]
        nx, ny = x + dx, y + dy
        # [상, 하, 좌, 우] wall의 정보
        # [(-1, -1), (0, -1), (1, -1)] 왼쪽 위쪽 중간 아래쪽
        # 왼쪽 위쪽은 현재벽의 위쪽, 이동할 벽의 오른쪽이 열려있어야함.
        # 왼쪽 중간은 이동할 벽의 오른쪽
        # 왼쪽 아래쪽은 현재벽의 아래쪽, 이동할 벽의 오른쪽이 열려있어야함.
        if in_range(nx, ny) and not visited[nx][ny] and wall[nx][ny][3] != 1:
            if (i == 0 and wall[x][y][0] != 1) or i == 1 or (i == 2 and wall[x][y][1] != 1) :
                ice[nx][ny] += power
                visited[nx][ny] = True
                spread2(nx, ny, power - 1)

def spread3(x, y, power):  # 위쪽으로 펴지기
    global visited
    if power == 0:
        return
    for i in range(3):
        dx, dy = dxy3[i]
        nx, ny = x + dx, y + dy
        # [상, 하, 좌, 우] wall의 정보
        # [(-1, -1), (-1, 0), (-1, 1)] 위쪽 왼쪽 중간 오른쪽
        # 위쪽 왼쪽은 현재벽의 왼쪽, 이동할 벽의 아래쪽이 열려있어야함.
        # 위쪽 중간은 이동할 벽의 아래쪽
        # 위쪽 오른쪽은 현재벽의 오른쪽, 이동할 벽의 아래쪽이 열려있어야함.
        if in_range(nx, ny) and not visited[nx][ny] and wall[nx][ny][1] != 1:
            if (i == 0 and wall[x][y][2] != 1) or i == 1 or (i == 2 and wall[x][y][3] != 1) :
                ice[nx][ny] += power
                visited[nx][ny] = True
                spread3(nx, ny, power - 1)

def spread4(x, y, power) : # 오른쪽으로 펴지기
    global visited, ice
    if power == 0 :
        return
    for i in range(3) :
        dx, dy = dxy4[i]
        nx, ny = x + dx, y + dy
        # [상, 하, 좌, 우] wall의 정보
        # [(-1, 1), (0, 1), (1, 1)] 오른쪽 위 중간 아래
        # 오른쪽 위는 현재벽의 위, 이동할 벽의 왼쪽 열려있어야함.
        # 오른쪽 중간은 이동할 벽의 왼쪽만 열려있으면 됨.
        # 오른쪽 아래는 현재벽의 아래, 이동할 벽의 왼쪽 열려있어야함.
        if in_range(nx, ny) and not visited[nx][ny] and wall[nx][ny][2] != 1:
            if (i == 0 and wall[x][y][0] != 1) or i == 1 or (i == 2 and wall[x][y][1] != 1) :
                ice[nx][ny] += power
                visited[nx][ny] = True
                spread4(nx, ny, power - 1)

def spread5(x, y, power):  # 아래쪽으로 펴지기
    global visited, ice
    if power == 0:
        return
    for i in range(3):
        dx, dy = dxy5[i]
        nx, ny = x + dx, y + dy
        # [상, 하, 좌, 우] wall의 정보
        # [(1, -1), (1, 0), (1, 1)] 아래쪽 왼쪽 중간 오른쪽
        # 아래쪽 왼쪽은 현재벽의 왼쪽, 이동할 벽의 위쪽이 열려있어야함.
        # 아래쪽 중간은 이동할 벽의 위쪽
        # 아래쪽 오른쪽은 현재벽의 오른쪽, 이동할 벽의 위쪽이 열려있어야함.
        if in_range(nx, ny) and not visited[nx][ny] and wall[nx][ny][0] != 1:
            if (i == 0 and wall[x][y][2] != 1) or i == 1 or (i == 2 and wall[x][y][3] != 1) :
                ice[nx][ny] += power
                visited[nx][ny] = True
                spread5(nx, ny, power - 1)

def shot() :
    global visited
    power = 5
    for i in range(n) :
        for j in range(n) :
            if 2 <= office[i][j] <= 5 :
                visited = [[False for _ in range(n)] for _ in range(n)]
                if office[i][j] == 2:  # 2는 왼쪽
                    ice[i][j - 1] += power
                    visited[i][j - 1] = True
                    spread2(i, j - 1, power - 1)
                elif office[i][j] == 3:  # 3은 위쪽
                    ice[i - 1][j] += power
                    visited[i - 1][j] = True
                    spread3(i - 1, j, power - 1)
                elif office[i][j] == 4 : # 4는 오른쪽
                    ice[i][j + 1] += power
                    visited[i][j + 1] = True
                    spread4(i, j + 1, power - 1)
                else : # 5는 아래쪽
                    ice[i + 1][j] += power
                    visited[i + 1][j] = True
                    spread5(i + 1, j, power - 1)
                # print("에어컨 번호 : ", office[i][j])
                # print("i, j : ", i, j)
                # print("ice : ")
                # for k in range(n):
                #     print(ice[k])

def mix() :
    global temp_ice, ice
    for i in range(n) :
        for j in range(n) :
            for d in range(4) :
                dx, dy = dxy[d]
                nx, ny = i + dx, j + dy
                if in_range(nx, ny) and wall[i][j][d] != 1 and ice[i][j] < ice[nx][ny] :
                    temp_ice[i][j] += (ice[nx][ny] - ice[i][j]) // 4
                    temp_ice[nx][ny] -= (ice[nx][ny] - ice[i][j]) // 4

    for i in range(n) :
        for j in range(n) :
            if temp_ice[i][j] == 0 :
                continue
            ice[i][j] += temp_ice[i][j]
            temp_ice[i][j] = 0

def minus() :
    for j in range(n) :
        if ice[0][j] > 0 :
            ice[0][j] -= 1
        if ice[n - 1][j] > 0 :
            ice[n - 1][j] -= 1

    for i in range(1, n - 1) :
        if ice[i][0] > 0 :
            ice[i][0] -= 1
        if ice[i][n - 1] > 0 :
            ice[i][n - 1] -= 1


T = int(input())
for tc in range(1, T + 1):
    # n : 격자 크기, m : 벽의 개수, k : 사무실의 시원함 정도
    n, m, k = map(int, input().split())
    office = [list(map(int, input().split())) for _ in range(n)]

    wall = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]
    # [상, 하, 좌, 우]
    for _ in range(m) :
        x, y, s = map(int, input().split())
        if s == 0 : # 0은 해당 위치의 위의 벽
            wall[x - 1][y - 1][0] += 1
            wall[x - 2][y - 1][1] += 1
        else : # 1이면 해당 위치의 왼쪽 벽
            wall[x - 1][y - 1][2] += 1
            wall[x - 1][y - 2][3] += 1

    ice = [[0 for _ in range(n)] for _ in range(n)]
    temp_ice = [[0 for _ in range(n)] for _ in range(n)]
    visited = []

    # print("office : ")
    # for i in range(n) :
    #     print(office[i])
    # print("ice : ")
    # for i in range(n) :
    #     print(ice[i])
    # print("wall : ")
    # for i in range(n) :
    #     print(wall[i])
    # print()

    answer = 0
    while not check() :
        if answer == 100 :
            answer = -1
            break
        # 1. 에어컨 바람 쏘기
        shot()
        # print("After ice : ")
        # print("ice : ")
        # for i in range(n) :
        #     print(ice[i])
        # print()
        # 2. 시원한 공기들이 섞인다.
        mix()
        # print("After mix : ")
        # print("ice : ")
        # for i in range(n):
        #     print(ice[i])
        # print()
        # 3. 외벽에 있는 칸 1씩 감소
        minus()
        # print("After minus : ")
        # print("ice : ")
        # for i in range(n):
        #     print(ice[i])
        # print()
        answer += 1


    print(answer)
