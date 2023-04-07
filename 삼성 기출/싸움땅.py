# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque
# 기본 정보 입력 받기
# n : 격자 size, m : 플레이어 수, k : round
n, m, k = map(int, input().split())

gido = [[deque() for _ in range(n)] for _ in range(n)]
# print(gido)
# print(len(gido[0][0]))
# 격자 입력 받기
for i in range(n):
     temp = list(map(int, input().split()))
     for j in range(n) :
         gido[i][j].append(temp[j])
# print(gido)
# print(len(gido[0][0]))
# print(gido[0][0][-1])
# 플레이어 정보 입력 받기
# (x, y) : 플레이어의 위치, d : 방향, s : 초기 능력치
pos = []
p_d = []
p_s = []
for _ in range(m):
    x, y, d, s = map(int, input().split())
    pos.append([x - 1, y - 1])
    p_d.append(d)
    p_s.append(s)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

gun = [0] * m
point = [0] * m

# print("gun : {}".format(gun))
#
# print("n : {}, m : {}, k : {}".format(n, m, k))
# print("gido : {}".format(gido))
# print("pos : {}".format(pos))
# print("p_d : {}".format(p_d))
# print("p_s : {}".format(p_s))


# 격자 범위 안에 있는지 확인 하는 함수
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 같은 칸에 본인 제외 누가 있는지 확인하는 함수
# 0이면 아무도 없음, i 면 해당 사람 번호 반환
def check(player):
    for i in range(m):
        # 같은 위치에 있는 사람 확인할 때 본인은 패스
        if i != player and pos[i] == pos[player]:
            return i
    return -1

# 누가 있는지 확인하는 함수
def who(x, y) :
    for i in range(m) :
        if pos[i] == [x, y] :
            return False
    return True

# p1과 p2가 싸움, point 적립하고 진사람 반환
def fight(p1, p2):
    attack1 = p_s[p1] + gun[p1]
    attack2 = p_s[p2] + gun[p2]
    if attack1 > attack2:
        point[p1] += (attack1 - attack2)
        return p1, p2
    elif attack2 > attack1:
        point[p2] += (attack2 - attack1)
        return p2 ,p1
    # 같은 경우는 초기 능력치가 더 높은 사람이 이김
    else:
        if p_s[p1] > p_s[p2] :
            return p1, p2
        else :
            return p2, p1

# 큐를 정렬해주는 함수
def sort_q(x, y) :
    temp = list(gido[x][y])
    gido[x][y].clear()
    temp.sort()
    for i in range(len(temp)) :
        gido[x][y].append(temp[i])

def round():
    for i in range(m):
        # STEP 1 => 한 칸 이동
        x, y = pos[i]
        id = p_d[i]
        nx, ny = x + dx[id], y + dy[id]
        if in_range(nx, ny):
            pos[i] = [nx, ny]
        # 격자 안에 없다면 반대 방향으로 한칸
        else:
            p_d[i] = (p_d[i] + 2) % 4
            id = p_d[i]
            pos[i] = [x + dx[id], y + dy[id]]

        # STEP 2 - 1 =>  이동한 방향에 플레이어가 없다면 해당 칸에 총이 있는지 확인합니다.
        # 총이 있는 경우, 해당 플레이어는 총을 획득
        now = check(i)
        x, y = pos[i]
        if now == -1 :
            if gido[x][y] :
                mg = int(gido[x][y][-1])
                if mg > gun[i]:
                    temp = gun[i]
                    gun[i] = mg
                    gido[x][y].pop()
                    gido[x][y].append(temp)
                    sort_q(x, y)
        else:
            # STEP 2 - 2 - 1 => 플레이어를 만났다!! 싸우자 !! 이긴 사람은 포인트를 차이만큼 가져간다.
            winner, looser = fight(i, now)
            # STEP 2 - 2 - 2 => 진 플레이어는 본인이 가지고 있는 총을 해당 격자에 내려놓는다.
            # 해당 플레이어가 원래 가지고 있던 방향대로 한칸 이동
            # 범위 밖이면 오른쪽 90도 회전 한다. => 이동
            # 해당 칸에 총이 있으면 플레이어는 총을 획득 , 조건은 아까와 같음

            id = p_d[looser]
            # 패배자는 가지고 있는 총을 버림
            if gun[looser] > 0 :
                gido[x][y].append(gun[looser])
                sort_q(x, y)
                gun[looser] = 0
            # 패배자 이동
            nx, ny = x + dx[id], y + dy[id]
            if in_range(nx, ny) and who(nx, ny) :
                pos[looser] = [nx, ny]
            # 격자 안에 없다면 오른쪽 90도로 전환 후 공간이 있으면 이동
            else:
                for _ in range(3):
                    id = (id + 1) % 4
                    nx, ny = x + dx[id], y + dy[id]
                    if in_range(nx, ny) and who(nx, ny):
                        p_d[looser] = id
                        pos[looser] = [nx, ny]
                        break

            nx, ny = pos[looser]
            # 이동을 마친 후 해당 자리에 총이 있다면 줍자
            if gido[nx][ny] :
                mg = int(gido[nx][ny][-1])
                gun[looser] = mg
                gido[nx][ny].pop()
                # if gido[nx][ny] > gun[looser] :
                #     gun[looser], gido[nx][ny] = gido[nx][ny], gun[looser]

            # 승리자는 총을 비교해서 챙기자
            # 승리자 위치 반환
            x, y = pos[winner]
            if gido[x][y] :
                mg = int(gido[x][y][-1])
                if mg > gun[winner]:
                    temp = gun[winner]
                    gun[winner] = mg
                    gido[x][y].pop()
                    gido[x][y].append(temp)
                    sort_q(x, y)

                # if gido[x][y] > gun[winner] :
                #     gun[winner], gido[x][y] = gido[x][y], gun[winner]

for _ in range(k) :
    round()
    # print("=================")
    # print("count : ", count)
    # print("p_d : ",p_d)
    # print("pos :",pos)
    # print("gun : ", gun)
    # print("gido : ")
    # for i in range(n) :
    #     print(gido[i])

print(*point)



