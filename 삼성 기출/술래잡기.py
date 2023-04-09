# import sys
# sys.stdin = open("input.txt", "r")
# n : 격자 크기, m : 도망자 수, h : 나무 수, k : turn 횟수
n, m, h, k = map(int,input().split())

gido = [[0 for _ in range(n)] for _ in range(n)]
sul_gido = [[0 for _ in range(n)] for _ in range(n)]
tree = [[0 for _ in range(n)] for _ in range(n)]
domang = [[] for _ in range(m + 1)]
dd = [0 for _ in range(m + 1)]
sul = [n//2, n//2]
sul_d = [3]
sul_check = 0
record = 0
line = 1
switch = [True]

point = 0

count = 1
sul_gido[n // 2][n //2] = 1
for _ in range(m) :
    x, y, d = map(int, input().split())
    gido[x - 1][y - 1] = 1
    domang[count] = [x - 1, y - 1]
    dd[count] = d - 1
    count += 1
for _ in range(h) :
    tx, ty = map(int, input().split())
    tree[tx - 1][ty - 1] = 1

# print("n : {}, m : {}, h : {}, k: {}".format(n, m, h, k))
# print("gido : ", gido)
# print("tree : ", tree)
# print("domang : ", domang)
# print("dd : ", dd)
# print("sul : ", sul)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 격자 안에 있는지 확인
def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

def distance(t1, t2) :
    x1, y1 = t1
    x2, y2 = t2
    dis = abs(x1 - x2) + abs(y1 - y2)
    if dis <= 3 :
        return True
    return False

def move_sul() :
    global sul_check
    global record
    global line
    # 방향을 바꿔야 함
    d = sul_d[0]
    x, y = sul
    nx, ny = x + dx[d], y + dy[d]
    if in_range(nx, ny) :
        # gido[nx][ny] = -1
        sul_gido[x][y] = 0
        sul_gido[nx][ny] = 1
        sul[0], sul[1] = nx, ny
        record += 1
        if sul == [0, 0] :
            switch[0] = False
            sul_d[0] = 1
            line = record
            sul_check = -1
            record = 0
        elif record == line :
            sul_d[0] = (sul_d[0] + 1) % 4
            sul_check += 1
            record = 0
            if sul_check == 2 :
                sul_check = 0
                line += 1

def move_return() :
    global sul_check
    global record
    global line
    # 방향을 바꿔야 함
    d = sul_d[0]
    x, y = sul
    nx, ny = x + dx[d], y + dy[d]
    if in_range(nx, ny) :
        # gido[nx][ny] = -1
        sul_gido[x][y] = 0
        sul_gido[nx][ny] = 1
        sul[0], sul[1] = nx, ny
        record += 1
        if sul == [n//2, n//2] :
            switch[0] = True
            sul_d[0] = 3
            line = 1
            sul_check = 0
            record = 0
        elif record == line :
            sul_d[0] = (sul_d[0] - 1) % 4
            sul_check += 1
            record = 0
            if sul_check == 2 :
                sul_check = 0
                line -= 1

def catch(turn) :
    global point
    d = sul_d[0]
    x, y = sul
    count = 0
    if tree[x][y] == 0 and gido[x][y] > 0 :
        count += gido[x][y]
        gido[x][y] = 0

    for i in range(1, 3) :
        nx, ny = x + (i * dx[d]), y + (i * dy[d])
        if in_range(nx, ny) :
            if tree[nx][ny] == 0 and gido[nx][ny] > 0 :
                count += gido[nx][ny]
                gido[nx][ny] = 0
    point += turn * count

def move_domang() :
    for i in range(1, m + 1) :
        if domang[i] != [-1, -1] and distance(sul, domang[i]) :
            d = dd[i]
            x, y = domang[i][0], domang[i][1]
            # 잡혔다
            if gido[x][y] == 0 :
                domang[i] = [-1, -1]
                continue
            nx, ny = x + dx[d], y + dy[d]
            if [nx, ny] == sul :
                continue
            if in_range(nx, ny) :
                domang[i] = [nx, ny]
                gido[x][y] -= 1
                gido[nx][ny] += 1
            else :
                dd[i] = (d + 2) % 4
                d = dd[i]
                x, y = domang[i][0], domang[i][1]
                nx, ny = x + dx[d], y + dy[d]
                if [nx, ny] == sul:
                    continue
                if in_range(nx, ny):
                    domang[i] = [nx, ny]
                    gido[x][y] -= 1
                    gido[nx][ny] += 1
    # print("after domang")
    # print("gido : ", gido)
    # print("tree : ", tree)
    # print("domang : ", domang)
    # print("dd : ", dd)
    # print("sul : ", sul)

for i in range(1, k + 1) :
    # print("turn : ", i)
    move_domang()
    # 술래 이동
    if switch[0]:
        move_sul()
    else:
        move_return()
    # print("after sul")
    # print("gido : ", gido)
    # print("tree : ", tree)
    # print("domang : ", domang)
    # print("dd : ", dd)
    # print("sul : ", sul)
    # print("sul_d : ", sul_d[0])
    # print("line : ", line)
    # print("record : ", record)
    # print("sul_check : ", sul_check)
    # print("point : ", point)
    # print("=========================================")
    catch(i)
    # print("gido : ", gido)
    # print("=========================================")

print(point)
