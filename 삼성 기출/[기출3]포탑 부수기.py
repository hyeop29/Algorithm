import sys
sys.stdin = open("input.txt", "r")

INF = float("inf")

def find_attacker() :
    global attacker
    ax, ay = -1, -1
    power = INF

    for sum in range(n + m - 2, -1, -1) :
        for j in range(m - 1, -1, -1) :
            i = sum - j
            if i >= n or i < 0 or gido[i][j] == 0:
                continue
            if gido[i][j] < power :
                power = gido[i][j]
                ax, ay = i, j
            elif gido[i][j] == power and time[i][j] > time[ax][ay] :
                power = gido[i][j]
                ax, ay = i, j

    attacker = (ax, ay)

def find_victim() :
    pass

def Laser() :
    return False

def bomb() :
    pass

def repair() :
    pass

T = int(input())
for tc in range(1, T + 1) :
    # n : 행, m : 열, k : 턴 횟수
    n, m, k = map(int, input().split())
    gido = [list(map(int, input().split())) for _ in range(n)]
    time = [[0 for _ in range(n)] for _ in range(n)]
    no = [[False for _ in range(n)] for _ in range(n)]
    attacker = (-1, -1) # 공격자의 좌표
    victim = (-1, -1) # 피해자의 좌표

    for t in range(1, k + 1) :
        # 1. 공격자 선정
        find_attacker()
        print("After find_attacker : ")
        print("attacker : ", attacker)
        break
        # 2 - 1. 공격 대상 선정, 이후 공격자의 핸디캡 적용
        find_victim()
        # 2 - 2. 공격 (레이저가 가능하다면, 레이저 그렇지 않으면 포탄 공격)
        if not Laser() :
            bomb()
        # 3. 포탑 부서짐 => 이미 2번에서 적용
        # 4. 포탑 정비
        repair()
