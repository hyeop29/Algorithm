# 파일 입출력을 위한 것 // 제출 시 삭제할 것
# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우

def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

def dfs(x, y) :
    global length
    team_info[x][y] = cnt
    team[cnt].append((x, y))

    if 1 <= gido[x][y] < 3 :
        length += 1
        for dx, dy in dxy :
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and ((gido[x][y] == 1 and gido[nx][ny] == 2) or (gido[x][y] == 2 and 1 < gido[nx][ny] < 4)) :
                visited[nx][ny] = True
                dfs(nx, ny)
    else :
        if gido[x][y] == 3 :
            team_len[cnt] = length
        for dx, dy in dxy :
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and gido[nx][ny] == 4 :
                visited[nx][ny] = True
                dfs(nx, ny)

def mov() :
    global pos_member
    for i in range(m) :
        team[i].appendleft(team[i].pop())

    pos_member = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m) :
        for j in range(team_len[i]) :
            x, y = team[i][j]
            pos_member[x][y] = 1

def change(num) :
    temp_list = []
    # 기존 머리부터 temp_list에 보관한다.
    for _ in range(team_len[num]) :
        temp_list.append(team[num].popleft())
    team[num].reverse()
    for i, j in temp_list :
        team[num].appendleft((i, j))

def point(x, y) :
    global score
    team_num = team_info[x][y]
    team_length = team_len[team_num]

    for i in range(team_length) :
        if team[team_num][i] == (x, y) :
            score += pow(i + 1, 2)
            # 머리와 꼬리사람 변환
            change(team_num)
            return

def throw_ball(r) :
    check = r % (4 * n)
    r = r % n

    # 좌 -> 우
    if check < n :
        for j in range(n) :
            if pos_member[r][j] == 1 :
                point(r, j)
                return
    # 하 -> 상
    elif check < 2 * n :
        for i in range(n - 1, -1, -1) :
            if pos_member[i][r] == 1 :
                point(i, r)
                return
    # 우 -> 좌 :
    elif check < 3 * n :
        for j in range(n - 1, -1, -1) :
            if pos_member[n - r - 1][j] == 1 :
                point(n - r - 1, j)
                return
    # 상 -> 하
    else :
        for i in range(n) :
            if pos_member[i][n - r - 1] == 1 :
                point(i, n - r - 1)
                return

# testcase 수 입력 받기
# T = int(input())
T = 1
for tc in range(1, T + 1) :
    # n : 격자 크기, m : 팀의 개수, k : 라운드 수
    n, m, k = map(int, input().split())
    gido = [list(map(int, input().split())) for _ in range(n)]

    pos_member = [[0 for _ in range(n)] for _ in range(n)]
    team_info = [[-1 for _ in range(n)] for _ in range(n)] # 좌표에 따른 팀 정보를 기록
    team = [deque() for _ in range(m)] # 각 팀별 머리부터 ~ 머리 전까지의 좌표 기록
    team_len = [0 for _ in range(m)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    score = 0

    cnt, length = 0, 1
    for i in range(n) :
        for j in range(n) :
            if gido[i][j] == 1 :
                visited[i][j] = True
                dfs(i, j) # cnt는 팀 번호
                length = 1
                cnt += 1

    # print("gido : ", gido)
    # print("team : ", team)
    # print("team_len : ", team_len)
    # print("team_info : ", team_info)
    # print()

    for round in range(k) :
        # print("##############")
        # print("round : ", round)
        # print("##############")
        # 1. 각 팀은 머리사람을 따라서 한 칸 이동
        mov()
        # 2. 각 라운드마다 공이 정해진 선을 따라 던진다.
        throw_ball(round)

        # print("team : ", team)
        # print("pos_member : ", pos_member)
        # print("team_len : ", team_len)
        # print("team_info : ", team_info)
        # print("score : ", score)
        # print()

    print(score)
