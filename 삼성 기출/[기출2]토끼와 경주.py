import sys
sys.stdin = open("input.txt", "r")

import heapq

def setting(_n, _m, _p, rabbit) :
    global n, m, p, dis, score, race_pri
    n, m , p = _n, _m, _p
    for i in range(0, 2 * p, 2) :
        pid = rabbit[i]
        dis[pid] = rabbit[i + 1]
        score[pid] = 0
        # 점프 횟수, 행 + 열, 행, 열, pid
        heapq.heappush(race_pri, [0, 0, 0, 0, pid])

def up(r, c, udis) :
    udis = udis % (2 * (n - 1))
    if r - udis >= 0 :
        return r - udis, c
    else :
        return down(0, c, udis - r)

def down(r, c, ddis) :
    ddis = ddis % (2 * (n - 1))
    if r + ddis <= n - 1 :
        return r + ddis, c
    else :
        return up(n - 1, c, ddis - (n - 1 - r))
def right(r, c, rdis) :
    rdis = rdis % (2 * (m - 1))
    if c + rdis <= m - 1 :
        return r, c + rdis
    else :
        return left(r, m - 1, rdis - (m - 1 - c))
def left(r, c, ldis) :
    ldis = ldis % (2 * (m - 1))
    if c - ldis >= 0 :
        return r, c - ldis
    else :
        return right(r, 0, ldis - c)

def race(k, s) :
    global total_score

    get_s = {}
    for _ in range(k) :
        jump, r_c, r, c, pid = heapq.heappop(race_pri)

        temp_rc = []
        # 상, 하, 좌, 우로 점프 시킨다.
        pid_dis = dis[pid]
        ur, uc = up(r, c, pid_dis)
        heapq.heappush(temp_rc, [-(ur + uc), -ur, -uc])
        dr, dc = down(r, c, pid_dis)
        heapq.heappush(temp_rc, [-(dr + dc), -dr, -dc])
        rr, rc = right(r, c, pid_dis)
        heapq.heappush(temp_rc, [-(rr + rc), -rr, -rc])
        lr, lc = left(r, c, pid_dis)
        heapq.heappush(temp_rc, [-(lr + lc), -lr, -lc])

        nrc, nr, nc = heapq.heappop(temp_rc)
        heapq.heappush(race_pri, [jump + 1, -nrc, -nr, -nc, pid])
        get_s[pid] = [nrc, nr, nc, pid]

        # r + c 점수를 본인 제외하고 획득
        print("pid : ", pid)
        print("r + c, r, c : ", -nrc, -nr, -nc)
        score[pid] -= (-nrc + 2)
        total_score += (-nrc + 2)


    # s 점수를 얻을 토끼를 찾는다.
    get_s_value = list(get_s.values())
    heapq.heapify(get_s_value)
    _, _, _, pid = heapq.heappop(get_s_value)
    score[pid] += s



def change(pid_t, L) :
    global dis
    dis[pid_t] *= L

T = int(input())
for tc in range(1, T + 1) :
    n, m, p = -1, -1, -1
    dis = {} # key : pid , value : di
    score = {} # 토끼들의 점수 관리
    race_pri = [] # 점프를 진행한 우선순위를 담기위한 heapq
    total_score = 0

    # q : 명령어의 수
    q = int(input())
    for _ in range(q) :
        com = list(map(int, input().split()))
        if com[0] == 100 :
            # 1. 경기 시작 준비
            setting(com[1], com[2], com[3], com[4:])
            print("dis : ", dis)
            print("score : ", score)
            print("race_pri : ", race_pri)
            print()
        elif com[0] == 200 :
            # 2. 경주 진행
            race(com[1], com[2])
            print("After race : ")
            print("dis : ", dis)
            print("score : ", score)
            print("race_pri : ", race_pri)
            print("total_score : ", total_score)
            print()
        elif com[0] == 300 :
            # 3. 이동 거리 변경
            change(com[1], com[2])
        else :
            print(max(score.values()) + total_score)
