# import sys
# sys.stdin = open("input.txt", "r")

# 입력 받기
# 격자의 크기 n, 박멸이 진행되는 년 수 m, 제초제의 확산 범위 k, 제초제가 남아있는 년 수 c
n, m, k, c = map(int, input().split())

gido = []
for _ in range(n) :
    gido.append(list(map(int, input().split())))

# print("n : {}, m : {}, k : {}, c : {}".format(n, m, k, c))
# print("gido : ", gido)

# 상, 하, 좌, 우 확인 하기 위한 dx dy
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

baby_temp = [[0 for _ in range(n)] for _ in range(n)]

# kill 함수에 사용될 변수 선언
result = [[0 for _ in range(n)] for _ in range(n)]
tree_kill = [[0 for _ in range(n)] for _ in range(n)]
kx = [-1, -1, 1, 1]
ky = [-1, 1, -1, 1]

# 박멸한 나무 수
die = 0

# 격자 안에 있는지 확인 하는 함수
def in_range(x, y) :
    return 0 <= x and x < n and 0 <= y and y < n
# 나무 성장 시키는 함수
def grow(x, y) :
    count = 0
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny) and gido[nx][ny] > 0 :
            count += 1
    gido[x][y] += count

# 번식 하는 함수
def baby(x, y) :
    temp = gido[x][y]
    count = 0
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny) and gido[nx][ny] == 0 and tree_kill[nx][ny] == 0 :
            count += 1

    if count > 0 :
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny) and gido[nx][ny] == 0 and tree_kill[nx][ny] == 0:
                baby_temp[nx][ny] += (temp // count)

# 가장 많이 나무를 죽일 수 있는 제초제 뿌릴 위치 파악 후 제초제 분산
def kill() :
    max_value = 0
    max_x, max_y = -1, -1
    for x in range(n) :
        for y in range(n) :
            if gido[x][y] <= 0:
                continue

            count = gido[x][y]
            check = [True for _ in range(4)]
            for j in range(1, k + 1):
                for i in range(4) :
                    if not check[i] :
                        continue
                    nx, ny = x + (j * kx[i]), y + (j * ky[i])
                    if in_range(nx, ny) :
                        if gido[nx][ny] <= 0 :
                            check[i] = False
                        elif gido[nx][ny] > 0 :
                            count += gido[nx][ny]

            # 가장 많이 죽일 수 있는 위치 기록
            if max_value < count :
                max_value = count
                max_x, max_y = x, y

    # 제초제 수명 수정
    for i in range(n) :
        for j in range(n) :
            if tree_kill[i][j] > 0 :
                tree_kill[i][j] -= 1

    global die

    if max_value > 0 :
        die += max_value
        # 제초제 뿌림
        check = [True for _ in range(4)]
        gido[max_x][max_y] = 0
        tree_kill[max_x][max_y] = c
        for j in range(1, k + 1):
            for i in range(4):
                if not check[i] :
                    continue
                nx, ny = max_x + (j * kx[i]), max_y + (j * ky[i])
                if in_range(nx, ny) :
                    if gido[nx][ny] == -1 :
                        check[i] = False
                    elif gido[nx][ny] == 0 :
                        tree_kill[nx][ny] = c
                        check[i] = False
                    elif gido[nx][ny] > 0:
                        gido[nx][ny] = 0
                        tree_kill[nx][ny] = c

def simulation() :
    # STEP 1 인접한 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장, 성장은 모든 나무에게 동시에 일어남
    for i in range(n) :
        for j in range(n) :
            if gido[i][j] <= 0 :
                continue
            grow(i, j)
    # print("gido 1 : ", gido)
    # STEP 2 인접한 4개의 칸 중, 다른 나무, 제조체, 벽 없는 곳에 번식 진행 => 나무 그루 수 / 현재 번식 가능 칸 으로 번식, 나머지는 버림
    for i in range(n) :
        for j in range(n) :
            baby_temp[i][j] = 0

    for i in range(n):
        for j in range(n):
            if gido[i][j] <= 0:
                continue
            baby(i, j)
    # print("baby_temp 2 - 1: ", baby_temp)
    for i in range(n) :
        for j in range(n) :
            if baby_temp[i][j] > 0 :
                gido[i][j] += baby_temp[i][j]
    # print("gido 2 - 2: ", gido)
    # STEP 3
    # 각 칸 중 제초제를 뿌렸을 때 나무가 가장 많이 박멸되는 칸에 제초제를 뿌립니다.
    # 나무가 없는 칸에 제초제를 뿌리면 박멸되는 나무가 전혀 없는 상태로 끝이 나지만, 나무가 있는 칸에 제초제를 뿌리게 되면 4개의 대각선 방향으로 k칸만큼 전파되게 됩니다.
    # 단 전파되는 도중 벽이 있거나 나무가 아얘 없는 칸이 있는 경우, 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다.
    # 제초제가 뿌려진 칸에는 c년만큼 제초제가 남아있다가 c+1년째가 될 때 사라지게 됩니다.
    # 제초제가 뿌려진 곳에 다시 제초제가 뿌려지는 경우에는 새로 뿌려진 해로부터 다시 c년동안 제초제가 유지됩니다.
    kill()

# print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

for _ in range(m) :
    simulation()
    # print("gido : ", gido)
    # print("tree_kill : ", tree_kill)
    # print("result : ", result)
    # print("answer : ", die)
    # print("=====================")

print(die)
