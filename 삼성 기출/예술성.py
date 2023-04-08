# import sys
# sys.stdin = open("input.txt", "r")

# 첫 번째 줄에 n이 주어집니다. n은 반드시 홀수
n = int(input())
gido = []
for _ in range(n) :
    gido.append(list(map(int, input().split())))

# 입력 확인
# print("< 입력 확인 >")
# print("n : ", n)
# print("gido : ", gido)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False for _ in range(n)] for _ in range(n)]
info = [[0 for _ in range(n)] for _ in range(n)]
group = [0]
group_point = [0]
temp = 0
# 전체 예술 점수
point = 0

# 격자 안 확인하는 함수
def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n
# dfs
def dfs(x, y, num) :
    global temp
    temp += 1
    visited[x][y] = True
    info[x][y] = num
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny) and gido[nx][ny] == gido[x][y] and not visited[nx][ny] :
            dfs(nx, ny, num)

def find(x, y, check) :
    temp = info[x][y]
    visited[x][y] = True
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny) :
            if info[nx][ny] != info[x][y] :
                check[temp][info[nx][ny]] += 1
            elif info[nx][ny] == info[x][y] and not visited[nx][ny] :
                find(nx, ny, check)


# 맞닿아 있는 변의 수 count
def touch(check) :
    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] :
                find(i, j, check)

# 초기 정보 획득
def start() :
    global temp
    global point
    count = 1
    for x in range(n) :
        for y in range(n) :
            if not visited[x][y] :
                temp = 0
                dfs(x, y, count)
                group.append(temp)
                group_point.append(gido[x][y])
                count += 1
    # print("group_point : ",group_point)
    # print("group : ", group)
    num = len(group) - 1
    check = [[0 for _ in range(num + 1)] for _ in range(num + 1)]
    # print("before touch check : ", check)
    for i in range(n) :
        for j in range(n) :
            visited[i][j] = False
    touch(check)
    # print("after touch check : ", check)
    # 계산
    for i in range(1, num + 1) :
        for j in range(1, num + 1) :
            if check[i][j] > 0 :
                point += (group[i] + group[j]) * group_point[i] * group_point[j] * check[i][j]
                # print("내부 점수 :", point)
                check[j][i] = 0
# 회전
def simulation() :
    # 십자 모양의 경우 통째로 반시계 방향으로 90도 회전
    room = [[0 for _ in range(n)] for _ in range(n)]
    ten = n // 2
    for i in range(n) :
        room[ten][i] = gido[i][ten]
    count = 0
    for i in range(n - 1, -1, -1) :
        room[count][ten] = gido[ten][i]
        count += 1
    # print("room 1 : ", room)
    # 나머지 정사각형은 시계 방향으로 90도 회전
    for i in range(ten) :
        for j in range(ten) :
            room[j][ten - i - 1] = gido[i][j]

    for i in range(ten) :
        for j in range(ten + 1, n) :
            tj = j - (ten + 1)
            room[tj][ten - i - 1 + ten + 1] = gido[i][j]

    for i in range(ten + 1, n) :
        for j in range(ten + 1, n) :
            ti = i - (ten + 1)
            room[j][ten - ti - 1 + ten + 1] = gido[i][j]

    for i in range(ten + 1, n) :
        for j in range(ten) :
            ti = i - (ten + 1)
            room[j + (ten + 1)][ten - ti - 1] = gido[i][j]

    # print("room 2 : ", room)
    for i in range(n) :
        for j in range(n) :
            gido[i][j] = room[i][j]

# print("< after start >")
start()
# print("info : ", info)
# print("group : ", group)
# print("point : ", point)
# print("gido : ", gido)
for i in range(3) :
    # print("< after simulation >")
    simulation()
    group_point = [0]
    group = [0]
    info = [[0 for _ in range(n)] for _ in range(n)]
    # print("info :", info)
    # print("group : ", group)
    # print("point :", point)
    # print("gido :", gido)
    for i in range(n) :
        for j in range(n) :
            visited[i][j] = False
    # print("< after start >")
    start()
    # print("info : ", info)
    # print("group : ", group)
    # print("point : ", point)
    # print("gido : ", gido)
print(point)
