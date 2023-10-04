# import sys
# sys.stdin = open("input.txt", "r")

import copy

INF = float("inf")
dxy = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
pack_dxy = [(-1, 0), (0, -1), (1, 0), (0, 1)]    # 상 - 좌 - 하 - 우

def copy() :
    global egg_monster

    for i in range(4) :
        for j in range(4) :
            for d in range(8) :
                if monster[i][j][d] == 0 :
                    continue
                egg_monster[i][j][d] += monster[i][j][d]

def in_range(x, y) :
    return 0 <= x < 4 and 0 <=y < 4

def mon_mov() :
    global monster, gido

    temp_monster = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]

    for i in range(4) :
        for j in range(4) :
            for d in range(8) :
                if monster[i][j][d] == 0 :
                    continue
                for k in range(8) :
                    new_d = (d + k) % 8
                    dx, dy = dxy[new_d]
                    nx, ny = i + dx, j + dy
                    if in_range(nx, ny) and die_monster[nx][ny] == 0 and (nx, ny) != packman :
                        temp_monster[nx][ny][new_d] += monster[i][j][d]

                        gido[nx][ny] += monster[i][j][d]
                        gido[i][j] -= monster[i][j][d]

                        monster[i][j][d] = 0
                        break

    for i in range(4) :
        for j in range(4) :
            for d in range(8) :
                if temp_monster[i][j][d] > 0 :
                    monster[i][j][d] += temp_monster[i][j][d]

def dfs(x, y, t, route, eat_gido) :   # x, y, t : 먹는 몬스터 개수, route : 경로
    global best_eat, best_route




    if len(route) == 3 :
        # print("@@@@@@@@@@@@@@@@@@@@@@@")
        # print("rotue : ", route)
        if best_eat < t :
            # print("@@@@@@@@@@@@@@@@@@@@@@@")
            # print("rotue : ", route)
            # print("t : ", t)
            for i in range(3) :
                best_route[i] = route[i]
            best_eat = t
        return

    else :
        # if len(route) > 0 and route[0] == 3 :
            # print()
            # print()
            # print("dfs 진입 후 정보 :")
            # print("x, y, t, route, eat_gido : ", x, y, t, route)
            # print(eat_gido)
        for i in range(4) :
            dx, dy = pack_dxy[i]
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) :
                route.append(i)
                mon = eat_gido[nx][ny]
                eat_gido[nx][ny] = 0
                dfs(nx, ny, t + mon, route, eat_gido)
                eat_gido[nx][ny] = mon
                route.pop()



def packman_mov() :
    global best_eat, best_route, packman, monster, gido, die_monster
    best_eat, best_route = -INF, [-1, -1, -1]

    eat_gido = [temp[:] for temp in gido]
    # print("eat_gido : ", eat_gido)
    # print("origin packman : ", packman)
    r, c = packman
    dfs(r, c, 0, [], eat_gido)
    # print("best_eat : ", best_eat)
    # print("best_route : ", best_route)

    for i in best_route :
        dx, dy = pack_dxy[i]
        r, c = r + dx, c + dy

        if gido[r][c] > 0 :
            monster[r][c] = [0 for _ in range(8)]
            die_monster[r][c] = 3
            gido[r][c] = 0

    packman = (r, c)

def delete_die() :
    global die_monster
    for i in range(4) :
        for j in range(4) :
            if die_monster[i][j] > 0 :
                die_monster[i][j] -= 1

def wakeup_egg() :
    global egg_monster, monster
    for i in range(4) :
        for j in range(4) :
            for d in range(8) :
                if egg_monster[i][j][d] > 0 :
                    monster[i][j][d] += egg_monster[i][j][d]
                    gido[i][j] += egg_monster[i][j][d]
                    egg_monster[i][j][d] = 0

# T = int(input())
T = 1
for tc in range(1, T + 1) :
    # m : 몬스터 수, t : 턴 횟수
    m, t = map(int, input().split())
    # 초기 팩맨 위치
    r, c = map(int, input().split())
    packman = (r - 1, c - 1)

    gido = [[0 for _ in range(4)] for _ in range(4)]
    monster = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]
    egg_monster = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]
    die_monster = [[0 for _ in range(4)] for _ in range(4)]
    temp = []

    best_eat = -INF
    best_route = []

    for _ in range(m) :
        r, c, d = map(int, input().split())
        gido[r - 1][c - 1] += 1
        monster[r - 1][c - 1][d - 1] += 1


    # print("monster : ")
    # for i in range(4):
    #     for j in range(4):
    #         print(monster[i][j], end=" ")
    #     print()
    # print("******************************************")
    # print("******************************************")
    # print("******************************************")

    for _ in range(t) :
        # 1. 몬스터 복제 시도
        copy()
        # print("gido : ", gido)
        # print("egg_monster : ")
        # for i in range(4):
        #     for j in range(4):
        #         print(egg_monster[i][j], end=" ")
        #     print()
        # print("monster : ")
        # for i in range(4):
        #     for j in range(4):
        #         print(monster[i][j], end=" ")
        #     print()
        # # 2. 몬스터 이동
        # print("===========================================")
        # print("===========================================")
        # print("===========================================")
        mon_mov()
        # print("gido : ", gido)
        # print("egg_monster : ")
        # for i in range(4):
        #     for j in range(4):
        #         print(egg_monster[i][j], end=" ")
        #     print()
        # print("monster : ")
        # for i in range(4):
        #     for j in range(4):
        #         print(monster[i][j], end=" ")
        #     print()
        # 3. 팩맨 이동
        packman_mov()
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        # print("monster : ")
        # for i in range(4):
        #     for j in range(4):
        #         print(monster[i][j], end=" ")
        #     print()
        # print("die_monster : ")
        # for i in range(4):
        #     for j in range(4):
        #         print(die_monster[i][j], end=" ")
        #     print()
        # print("packman : ", packman)
        # print("gido : ", gido)
        # 4. 몬스터 시체 소멸
        delete_die()
        # 5. 몬스터 복제 완성
        wakeup_egg()

    answer = 0
    for i in range(4) :
        answer += sum(gido[i])

    print(answer)
