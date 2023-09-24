# 파일 입출력을 위한 sys, 제출 시 주석처리해야함
import sys
sys.stdin = open("input.txt", "r")

# 0부터 3까지 순서대로 상, 우, 하, 좌

import heapq

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

def move(p) :
    # p는 player의 번호
    # nx, ny는 플레이어의 위치
    nx, ny = p_xy[p]
    # 기존 위치는 아무도 없는 것으로 만든다.
    player_pos[nx][ny] = -1
    # player의 현재 방향을 가져온다
    nd = p_d[p]
    dx, dy = dxy[nd]
    # 격자안이라면 그대로 이동
    if in_range(nx + dx, ny + dy) :
        p_xy[p] = [nx + dx, ny + dy]
    else :
        p_d[p] = (nd + 2) % 4
        dx, dy = dxy[p_d[p]]
        p_xy[p] = [nx + dx, ny + dy]

    new_x, new_y = p_xy[p]
    if player_pos[new_x][new_y] != -1 :
        ori_player = player_pos[new_x][new_y]
        fight(p, ori_player, new_x, new_y)
    else :
        player_pos[new_x][new_y] = p
        # 격자에 총이 있다면 총을 교체
        if gido[new_x][new_y] != [] :
            new_gun = heapq.heappop(gido[new_x][new_y])
            # 기존에 들고 있던 총보다 격자안에 있던 총이 더 강력하면 총 교체
            if -new_gun > p_gun[p] :
                old_gun = p_gun[p]
                p_gun[p] = -new_gun
                heapq.heappush(gido[new_x][new_y], -old_gun)
            else :
                heapq.heappush(gido[new_x][new_y], new_gun)

def fight(p1, p2, x, y) :
    p1_power = p_s[p1] + p_gun[p1]
    p2_power = p_s[p2] + p_gun[p2]

    if p1_power > p2_power :
        score[p1] += (p1_power - p2_power)
        player_pos[x][y] = p1
        l = p2
        w = p1
    elif p1_power == p2_power :
        if p_s[p1] > p_s[p2] :
            player_pos[x][y] = p1
            l = p2
            w = p1
        else :
            player_pos[x][y] = p2
            l = p1
            w = p2
    else :
        score[p2] += (p2_power- p1_power)
        player_pos[x][y] = p2
        l = p1
        w = p2

    loser(l, x, y)
    winner(w, x, y)

def loser(p, x, y) :
    # 진 플레이어는 총을 해당 격자에 둔다
    heapq.heappush(gido[x][y], -p_gun[p])
    p_gun[p] = 0
    nd = p_d[p]
    for i in range(4) :
        next_d = (nd + i) % 4
        dx, dy = dxy[next_d]
        if in_range(x + dx, y + dy) and player_pos[x + dx][y + dy] == -1 :
            break
    # 새로운 방향과 위치 지정
    # print("loser : ", p)
    # print("x, y, dx, dy : ", x, y, dx, dy)
    p_d[p] = next_d
    p_xy[p] = [x + dx, y + dy]
    player_pos[x + dx][y + dy] = p
    # 해당 격자에 총이 있다면 총을 줍는다
    if gido[x + dx][y + dy] != [] :
        new_gun = heapq.heappop(gido[x + dx][y + dy])
        p_gun[p] = -new_gun

def winner(p, x, y) :
    if gido[x][y] != []:
        new_gun = heapq.heappop(gido[x][y])
        # 기존에 들고 있던 총보다 격자안에 있던 총이 더 강력하면 총 교체
        if -new_gun > p_gun[p]:
            old_gun = p_gun[p]
            p_gun[p] = -new_gun
            heapq.heappush(gido[x][y], -old_gun)
        else:
            heapq.heappush(gido[x][y], new_gun)
    p_xy[p] = [x, y]

# testcase 수 입력 받기
T = int(input())
# testcase 수만큼 반복
for tc in range(1, T + 1) :
    # n : 격자크기, m : 플레이어 수, k : 라운드 수
    n, m, k = map(int, input().split())
    gido = [[[] for _ in range(n)] for _ in range(n)]
    player_pos = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n) :
        temp = list(map(int, input().split()))
        for j in range(n) :
            heapq.heappush(gido[i][j], -temp[j])

    p_gun = [0 for _ in range(m)] # player의 gun 능력치
    p_xy = [[] for _ in range(m)] # player의 위치
    p_d = [0 for _ in range(m)] # player의 방향
    p_s = [0 for _ in range(m)] # player의 초기 능력치
    score = [0 for _ in range(m)]

    for i in range(m) :
        x, y, d, s = map(int, input().split())
        p_xy[i] = [x - 1, y - 1]
        player_pos[x - 1][y - 1] = i
        p_d[i] = d
        p_s[i] = s

    for _ in range(k) :
        print("player들의 위치 : ", p_xy)
        print("player들의 gun : ", p_gun)
        print("총들의 정보 : ", gido)
        for player in range(m) :
            move(player)
            print("player들의 위치 : ", p_xy)
            print("player들의 gun : ", p_gun)
            print("총들의 정보 : ", gido)


    print(*score)
