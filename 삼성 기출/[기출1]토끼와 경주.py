# 파일 입출력을 위한 부분, 제출 시 삭제해야함.
import sys
sys.stdin = open("input.txt", "r")

import heapq

pri = [] # 토끼의 우선 순위 보관.
score = dict() # 토끼의 점수
dis = dict() # 각 토끼별로 이동 거리
n, m = 0, 0
total_score = 0

def init(all) :
    global n, m, pri, score, dis

    pri = []  # 토끼의 우선 순위 보관.
    score = dict()  # 토끼의 점수
    dis = dict()  # 각 토끼별로 이동 거리

    n, m, p = int(all[0]), int(all[1]), int(all[2])
    for i in range(3, 2 * p + 3, 2) :
        p_id, d_id = int(all[i]), int(all[i + 1])
        score[p_id] = 0
        dis[p_id] = d_id
        heapq.heappush(pri, (0, 0, 0, 0, p_id))  # 총 점프 횟수, 행 + 열, 행, 열, 고유번호

def up(r, c, pid, dis) :
    n_dis = dis % (2 * (n - 1))
    if r - n_dis >= 0 :
        return r - n_dis, c
    else :
        n_dis -= r
        return down(0, c, pid, n_dis)

def down(r, c, pid, dis) :
    n_dis = dis % (2 * (n - 1))
    if r + n_dis < n :
        return r + n_dis, c
    else :
        n_dis -= (n - 1 - r)
        return up(n - 1, c, pid, n_dis)

def left(r, c, pid, dis) :
    n_dis = dis % (2 * (m - 1))
    if c - n_dis >= 0 :
        return r, c - n_dis
    else :
        n_dis -= c
        return right(r, 0, pid, n_dis)

def right(r, c, pid, dis) :
    n_dis = dis % (2 * (m - 1))
    if c + n_dis < m :
        return r, c + n_dis
    else :
        n_dis -= (m - 1 - c)
        return left(r, m - 1, pid, n_dis)
def race(k, s) :
    # print("k : ", k)
    global total_score

    score_pri = {} # 행 + 열, 행, 열, 고유번호가 큰 토끼

    for temp_k in range(k) : # k 최대값 100
        race_pri = [] # 초기화
        j, r_c, r, c, pid = heapq.heappop(pri) # 우선순위가 가장 높은 토끼를 결정
        # print("######################")
        # print("pid : ", pid)
        # 벽을 만나면 반대 방향을 가도록 구성하는 부분이 까다롭다,,, 그것도 거리의 범위는 1억..
        # 상하좌우를 따로 만들기
        distance = dis[pid]
        ur, uc = up(r, c, pid, distance)
        # print("ur, uc : ", ur, uc)
        dr, dc = down(r, c, pid, distance)
        # print("dr, dc : ", dr, dc)
        lr, lc = left(r, c, pid, distance)
        # print("lr, lc : ", lr, lc)
        rr, rc = right(r, c, pid, distance)
        # print("rc, rr : ", rr, rc)

        heapq.heappush(race_pri, (-(ur + uc), -ur, -uc))
        heapq.heappush(race_pri, (-(dr + dc), -dr, -dc))
        heapq.heappush(race_pri, (-(lr + lc), -lr, -lc))
        heapq.heappush(race_pri, (-(rr + rc), -rr, -rc))

        # 가장 우선순위가 높은 칸을 골라 그 위치로 해당 토끼 이동
        new_rc, new_r, new_c = heapq.heappop(race_pri)
        # print("new_r, new_c : ", new_r, new_c)
        # print()
        heapq.heappush(pri, (j + 1, -new_rc, -new_r, -new_c, pid))
        score_pri[pid] = (new_rc, new_r, new_c, -pid)

        score[pid] -= (-new_rc + 2)
        total_score += (-new_rc + 2)

    score_pri_V = list(score_pri.values())
    heapq.heapify(score_pri_V)
    # k번의 턴이 모두 진행된 직후에는 우선순위가 높은 토끼에게 점수 S를 더해준다.
    _, _, _, pid = heapq.heappop(score_pri_V)
    score[-pid] += s

def change_dist(pid, L) :
    dis[pid] = dis[pid] * L


# TestCase 수 입력
T = int(input())
for tc in range(1, T + 1) :
    q = int(input())
    for _ in range(q) :
        # print("score : ", score)
        com = input().split()
        # 경주 시작 준비
        if com[0] == "100" :
            init(com[1:])
        # 경주 진행
        if com[0] == "200" :
            race(int(com[1]), int(com[2]))
        # 이동거리 변경
        if com[0] == "300" :
            change_dist(int(com[1]), int(com[2]))
        if com[0] == "400" :
            print(max(score.values()) + total_score)
