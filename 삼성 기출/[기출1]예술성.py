# 파일 입출력을 위한 sys / 제출 시 삭제할 것
# import sys
# sys.stdin = open("input.txt", "r")

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우

def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

def dfs(x, y, visited, team_num) :
    global cnt
    for dx, dy in dxy :
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not visited[nx][ny] and arr[x][y] == arr[nx][ny] :
            cnt += 1
            visited[nx][ny] = True
            arr_group[nx][ny] = team_num
            dfs(nx, ny, visited, team_num)

def init() :
    global cnt
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt, team_num = 0, 0

    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] :
                cnt += 1
                visited[i][j] = True
                real_num.append(arr[i][j])
                arr_group[i][j] = team_num
                dfs(i, j, visited, team_num)
                team_num += 1
                # 각 group의 속한 칸의 개수 기록
                group_num.append(cnt)
                cnt = 0
    return team_num

def adj_dfs(x, y, visited) :
    for dx, dy in dxy :
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) :
            if not visited[nx][ny] and arr_group[x][y] == arr_group[nx][ny] :
                visited[nx][ny] = True
                adj_dfs(nx, ny, visited)
            elif arr_group[x][y] != arr_group[nx][ny] :
                adj[arr_group[x][y]][arr_group[nx][ny]] += 1

def adj_record() :
    visited = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] :
                visited[i][j] = True
                adj_dfs(i, j, visited)

def get_point() :
    global score

    for i in range(team_num) :
        for j in range(team_num) :
            if adj[i][j] > 0 :
                score += (group_num[i] + group_num[j]) * real_num[i] * real_num[j] * adj[i][j]
                adj[i][j] = 0
                adj[j][i] = 0

def rotation() :
    temp = [[0 for _ in range(n)] for _ in range(n)]

    # 십자가 회전
    for i in range(n) :
        temp[n - 1 - (n // 2)][i] = arr[i][(n // 2)]

    for j in range(n) :
        if j == n // 2 :
            continue
        temp[n - 1 - j][(n // 2)] = arr[(n // 2)][j]

    # 왼쪽 위 회전
    for i in range(n // 2) :
        for j in range(n // 2) :
            temp[j][n // 2 - 1 - i] = arr[i][j]

    # 오른쪽 위 회전
    for i in range(n // 2) :
        for j in range(n // 2 + 1, n) :
            ox, oy = i, j - (n // 2  + 1)
            temp[oy][n // 2 - 1 - ox + (n // 2 + 1)] = arr[i][j]

    # 왼쪽 아래 회전
    for i in range(n // 2 + 1, n) :
        for j in range(n // 2) :
            ox, oy = i - (n // 2 + 1), j
            temp[oy + (n // 2 + 1)][n // 2 - 1 - ox] = arr[i][j]

    # 오른쪽 아래 회전
    for i in range(n // 2 + 1,  n) :
        for j in range(n // 2 + 1, n) :
            ox, oy = i - (n // 2 + 1), j - (n // 2 + 1)
            temp[oy + (n // 2 + 1)][n // 2 - 1 - ox + (n // 2 + 1)] = arr[i][j]

    for i in range(n) :
        for j in range(n) :
            arr[i][j] = temp[i][j]

# TestCase 수 입력 받는다.
# T = int(input())
T = 1
for tc in range(1, T + 1) :
    # n : 격자의 크기
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    score = 0

    arr_group = [[-1 for _ in range(n)] for _ in range(n)]
    group_num = []
    real_num = []
    cnt = 0

    # 초기화
    team_num = init()
    adj = [[0 for _ in range(team_num)] for _ in range(team_num)]
    # group 별 인접한 개수 기록
    adj_record()

    # 초기 점수를 더 한다.
    get_point()
    # print("score : ", score)
    for _ in range(3) :
        # 회전한다.
        rotation()
        # print("arr : ", arr)
        # 점수를 더 한다
        arr_group = [[-1 for _ in range(n)] for _ in range(n)]
        group_num = []
        real_num = []
        cnt = 0
        team_num = init()
        adj = [[0 for _ in range(team_num)] for _ in range(team_num)]
        adj_record()
        get_point()

    print(score)
