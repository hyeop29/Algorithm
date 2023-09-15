# 파일 입출력 / 제출 전에 주석 or 삭제 해야함.
import sys
sys.stdin = open("input.txt", "r")

from collections import deque

# bfs 에서 사용할 dxy / 우, 하, 좌, 상
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def find_atk() -> tuple :
    min_A = float("inf")
    ax, ay = -1, -1
    for sum in range(n + m - 2, -1, -1) :
        for j in range(m - 1, -1, -1) :
            i = sum - j
            if 0 > i or i >= n or potop[i][j] == 0 :
                continue

            if min_A > potop[i][j] :
                min_A = potop[i][j]
                ax, ay = i, j
            elif min_A == potop[i][j] and when_potop[ax][ay] < when_potop[i][j] :
                min_A = potop[i][j]
                ax, ay = i, j
    return ax, ay

def find_victim() -> tuple :
    max_V = float("-inf")
    vx, vy = -1, -1
    for sum in range(0, n + m - 1) :
        for i in range(n - 1, -1, -1) :
            j = sum - i
            if 0 > j or j >= m or potop[i][j] == 0 :
                continue

            if max_V < potop[i][j] :
                max_V = potop[i][j]
                vx, vy = i, j
            elif max_V == potop[i][j] and when_potop[vx][vy] > when_potop[i][j] :
                max_V = potop[i][j]
                vx, vy = i, j
    return vx, vy

def attack(x, y, power) :
    potop[x][y] = max(0, potop[x][y] - power)
    check_potop[x][y] = True

def Layzer() -> bool : # bfs
    # visited 배열
    visited = [[False for _ in range(m)] for _ in range(n)]
    # back_tracking
    back = [[None for _ in range(m)] for _ in range(n)]

    q = deque()
    q.append(atk)
    visited[atk[0]][atk[1]] = True

    while q :
        x, y = q.popleft()
        for dx, dy in dxy :
            nx, ny = (x + dx + n) % n, (y + dy + m) % m
            if not visited[nx][ny] and potop[nx][ny] > 0 :
                visited[nx][ny] = True
                q.append((nx, ny))
                back[nx][ny] = (x, y)

    # 공격 대상 지점까지 이동 못했다면 Layzer 공격 불가
    if not visited[victim[0]][victim[1]] :
        return False

    # 레이저 공격 진행
    attack(victim[0], victim[1], potop[atk[0]][atk[1]])

    power = potop[atk[0]][atk[1]] // 2
    lx, ly = back[victim[0]][victim[1]]
    while lx != atk[0] or ly != atk[1] :
        attack(lx, ly, power)
        lx, ly = back[lx][ly]

    return True

def boom() :
    vx, vy = victim
    for dx in (-1, 0, 1) :
        for dy in (-1, 0, 1) :
            nx, ny = (vx + dx + n) % n, (vy + dy + m) % m
            # 부서진 포탑이거나 공격자면 continue
            if potop[nx][ny] == 0 or (nx, ny) == atk :
                continue
            power = potop[atk[0]][atk[1]] // 2
            if dx == 0 and dy == 0 :
                power = potop[atk[0]][atk[1]]
            attack(nx, ny, power)

def finish() :
    cnt = 0
    for i in range(n) :
        for j in range(m) :
           if potop[i][j] > 0 :
               cnt += 1
    return cnt == 1

def repair() :
    for i in range(n) :
        for j in range(m) :
            if not check_potop[i][j] and potop[i][j] > 0 :
                potop[i][j] += 1

# Testcase 개수 입력
T = int(input())
for tc in range(1, T + 1) :
    # n : 행, m : 열, k : turn 횟수
    n, m, k = map(int, input().split())
    # n x m 담을 배열
    potop = [list(map(int, input().split())) for _ in range(n)]
    # n x m 공격 언제 했는 지 확인하는 배열
    when_potop = [[0 for _ in range(m)] for _ in range(n)]
    # 공격 개입을 확인하는 배열
    check_potop = [[False for _ in range(m)] for _ in range(n)]

    # 본격적인 구현
    for turn in range(1, k + 1) :
        # 1. 공격자 선정
        atk = find_atk()
        # 공격 turn 기록 / 공격 개입 True
        when_potop[atk[0]][atk[1]] = turn
        check_potop[atk[0]][atk[1]] = True
        # 2-1. 공격대상자 선정
        victim = find_victim()
        # 공격자 핸디캡
        potop[atk[0]][atk[1]] += n + m
        # 2-2-1. 레이저 공격 여부 확인
        if not Layzer() :
            # 2-2-2. 레이저 공격 불가 => 포탄 공격
            boom()
        # 3. 포탑 부서짐 (남아 있는 포탑 개수 확인, 1개면 즉시 종료)
        if finish() :
            break
        # 4. 포탑 재정비
        repair()
        check_potop = [[False for _ in range(m)] for _ in range(n)]
        # print(potop)

    answer = find_victim()
    print(potop[answer[0]][answer[1]])
