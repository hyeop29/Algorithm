# import sys
# sys.stdin = open("input.txt", "r")

# 격자의 크기 n, 팀의 개수 m, 라운드 수 k
n, m, k =  map(int, input().split())

gido = []
for _ in range(n) :
    gido.append(list(map(int, input().split())))

# 팀 마다 길이를 기록해둘 배열, 0번은 안쓰겠습니다.
line = [0 for _ in range(m + 1)]
visited = [[False for _ in range(n)] for _ in range(n)]
team = [[] for _ in range(m + 1)]
info = [[0 for _ in range(n)] for _ in range(n)]
# print("초기 상태 확인")
# print("n : {}, m : {}, k : {}".format(n, m, k))
# print("gido : {}".format(gido))
# print("line : {}".format(line))
# print("visited : {}".format(visited))
# print("team : {}".format(team))
# print("info : {}".format(info))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
# 격자 안에 있는지 확인하는 함수
def in_range(x, y) :
    return 0 <= x and x < n  and 0 <= y and y < n

# 팀 별로 길이 확인, 팀 정보 기입, 팀 위치 기입
def start() :
    team_num = 1
    for x in range(n) :
        for y in range(n) :
            if gido[x][y] == 1 :
                find(team_num, x, y)
                team_num += 1
def find(num, x, y) :
    info[x][y] = num
    team[num].append((x, y))
    visited[x][y] = True
    if gido[x][y] == 3:
        line[num] = len(team[num])
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny) and len(team[num]) == 1:
            if gido[nx][ny] == 2 :
                find(num, nx, ny)
        elif in_range(nx, ny) and gido[nx][ny] > 1 and gido[nx][ny] <= 4 and not visited[nx][ny] :
            find(num, nx, ny)

# 공 던져지기 점수를 얻는 사람과 팀을 반환 하자
def throw(round) :
    # print("round 1 :", round)
    round = round % (4*n)
    # print("round 2 :", round)
    if 0 < round <= n :
        for i in range(n) :
            if 1 <= gido[round - 1][i] <= 3 :
                return (round -1, i), info[round - 1][i]
    elif n < round <= 2*n :
        round = round % n
        if round == 0 :
            for i in range(n - 1, -1, -1) :
                if 1 <= gido[i][n - 1] <= 3:
                    return (i, n - 1), info[i][n-1]
        else :
            for i in range(n - 1, -1, -1) :
                if 1 <= gido[i][round - 1] <= 3 :
                    return (i, round - 1), info[i][round - 1]
    elif 2*n < round <= 3*n :
        round = round % n
        if round == 0 :
            for i in range(n - 1, -1, -1) :
                if 1 <= gido[round][i] <= 3:
                    return (round, i), info[round][i]
        else :
            for i in range(n - 1, -1, -1) :
                if 1 <= gido[n - round][i] <= 3 :
                    return (n - round, i), info[n - round][i]
    else :
        round = round % n
        if round == 0 :
            for i in range(n):
                if 1 <= gido[i][round] <= 3:
                    return (i, round), info[i][round]
        else :
            for i in range(n) :
                if 1 <= gido[i][n - round] <= 3 :
                    return (i, n - round), info[i][n - round]

    return (-1, -1), 0

 # 점수 획득 함수
def get_point(pos, num) :
    global result
    temp = team[num].index(pos)
    temp += 1
    result += (temp * temp)

# 머리 바꾸기
def change(num) :
    temp = line[num]
    for i in range(temp // 2) :
        team[num][i], team[num][temp - 1 - i] = team[num][temp - 1 - i], team[num][i]

    temp = len(team[num]) - line[num]
    ex = temp // 2
    seq = -1
    for j in range(line[num], line[num] + ex) :
        team[num][j], team[num][seq] = team[num][seq], team[num][j]
        seq -= 1
# 본격적인 시작
def simulation(round) :
    # STEP 1 이동
    for i in range(1, m + 1) :
        for j in range(len(team[i]) - 1, 0, -1) :
            if j == len(team[i]) - 1 :
                temp = team[i][j]
            team[i][j] = team[i][j - 1]
        team[i][0] = temp

    # 지도에 정보 변경
    for i in range(1, m + 1) :
        for j in range(len(team[i])) :
            tx, ty = team[i][j]
            if j < line[i] :
                if j == 0 :
                    gido[tx][ty] = 1
                elif j == (line[i] - 1) :
                    gido[tx][ty] = 3
                else :
                    gido[tx][ty] = 2
            else :
                gido[tx][ty] = 4
    # STEP 2
    # 점수를 획득한 사람의 위치와 팀 번호를 획득
    pos, num = throw(round)
    # 점수를 획득한 사람이 있을 경우에만 점수를 얻는 함수 실행 => 팀방향 전환
    if num > 0 :
        get_point(pos, num)
        change(num)
        # 지도에 정보 변경
        for j in range(len(team[num])):
            tx, ty = team[num][j]
            if j < line[num]:
                if j == 0:
                    gido[tx][ty] = 1
                elif j == (line[num] - 1):
                    gido[tx][ty] = 3
                else:
                    gido[tx][ty] = 2
            else:
                gido[tx][ty] = 4


start()
# print("초기화 완료")
# print("gido : {}".format(gido))
# print("line : {}".format(line))
# print("visited : {}".format(visited))
# print("team : {}".format(team))
# print("info : {}".format(info))
for i in range(1, k + 1) :
    simulation(i)
    # print("==========================================================================================================================================")
    # print("gido : {}".format(gido))
    # print("line : {}".format(line))
    # print("visited : {}".format(visited))
    # print("team : {}".format(team))
    # print("info : {}".format(info))
    # print("score : {}".format(result))
print(result)
