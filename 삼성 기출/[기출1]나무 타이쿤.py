# import sys
# sys.stdin = open("input.txt", "r")

dxy = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]

def mov() :
    for i in range(n) :
        for j in range(n) :
            if vitamin[i][j] == 0 :
                continue
            vitamin[i][j] = 0
            dx, dy = dxy[d]
            nx, ny = i + dx * p, j + dy * p
            temp_vitamin[nx % n][ny % n] = 1

    for i in range(n) :
        for j in range(n) :
            if temp_vitamin[i][j] == 1 :
                vitamin[i][j] = temp_vitamin[i][j]
                temp_vitamin[i][j] = 0

def vitamin_in() :
    for i in range(n) :
        for j in range(n) :
            if vitamin[i][j] == 1 :
                gido[i][j] += 1

def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

def check(x, y) :
    cnt = 0
    for i in range(1,8, + 2) :
        dx, dy = dxy[i]
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and gido[nx][ny] > 0 :
            cnt += 1

    return cnt

def grow() :
    for i in range(n) :
        for j in range(n) :
            if vitamin[i][j] == 1 :
                cnt = check(i, j)
                gido[i][j] += cnt

def buy() :
    for i in range(n) :
        for j in range(n) :
            if gido[i][j] >= 2 and vitamin[i][j] == 0:
                vitamin[i][j] = 1
                gido[i][j] -= 2
            elif vitamin[i][j] == 1 :
                vitamin[i][j] = 0


# T = int(input())
T = 1
for tc in range(1, T + 1) :
    # n : 격자의 크기, m : 총년 수
    n, m = map(int, input().split())
    gido = [list(map(int, input().split())) for _ in range(n)]
    vitamin = [[0 for _ in range(n)] for _ in range(n)] # 영양제 위치 관리
    temp_vitamin = [[0 for _ in range(n)] for _ in range(n)]  # 영양제 이동 시 사용

    for i in range(n - 2, n) :  # 초기 비타민 설정
        for j in range(2) :
            vitamin[i][j] = 1

    for _ in range(m) :
        _d, p = map(int, input().split()) # 각 년도의 이동 규칙
        d = _d - 1

        # 1. 특수영양제 이동
        mov()
        # print("After mov : ")
        # print("vitamin : ", vitamin)
        # print()
        # 2. 특수영양제 투입
        vitamin_in()
        # print("After vitamin_in : ")
        # print("gido : ", gido)
        # print()
        # 3. 대각선 나무 수 확인 후, 성장
        grow()
        # print("After grow : ")
        # print("gido : ", gido)
        # print()
        # 4. 특수 영양제 구입
        buy()
        # print("After buy : ")
        # print("vitamin : ", vitamin)
        # print()

    answer = 0
    for i in range(n) :
        answer += sum(gido[i])
    print(answer)
