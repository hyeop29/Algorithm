import sys
sys.stdin = open("input.txt", "r")

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
INF = float("inf")

def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

def mov() :
    global answer
    for i in range(m) :
        check = False
        x, y = do[i]
        if (x, y) == (-1, -1) :
            continue
        ox, oy = out
        dis = abs(x - ox) + abs(y - oy)
        best_x, best_y = x, y

        for dx, dy in dxy :
            nx, ny = x + dx, y + dy
            ndis = abs(nx - ox) + abs(ny - oy)
            if in_range(nx, ny) and miro[nx][ny] == 0 and dis > ndis :
                check = True
                dis = ndis
                best_x, best_y = nx, ny

        # 도착할 경우 -1, -1 로 변경해준다.
        if (best_x, best_y) == out :
            do[i] = (-1, -1)
        else :
            do[i] = (best_x, best_y)

        if check :
            answer += 1

def finish() :
    for x, y in do :
        if (x, y) != (-1, -1) :
            return False
    return True
def find_square() :
    # 가장 작은 정사각형의 크기를 찾자
    dis = INF
    ox, oy = out
    for x, y in do :
        if (x, y) == (-1, -1) :
            continue
        temp_dis = max(abs(x - ox), abs(y - oy))
        if dis > temp_dis :
            dis = temp_dis

    # 그럼 0, 0 부터 시작하며 조건에 만족하는 정사각형의 왼쪽 위 좌표를 구한다.
    for start_x in range(n - dis) :
        for start_y in range(n - dis) :
            end_x, end_y = start_x + dis, start_y + dis
            if start_x <= ox <= end_x and start_y <= oy <= end_y :
                # 참가자가 있는지 확인
                for x, y in do :
                    if (x, y) == (-1, -1) :
                        continue
                    if start_x <= x <= end_x and start_y <= y <= end_y :
                        return start_x, start_y, dis

def rotate() :
    global out
    # 정사각형의 왼쪽 위 좌표 (x, y) , 정사각형의 크기 : dis
    x, y, dis = find_square()

    # 해당 정보를 이용해서 회전한다. 회전할 땐, 0,0 으로 가져와 회전하면 된다.
    # 회전하며 내구도 1 감소
    for i in range(x, x + dis + 1) :
        for j in range(y, y + dis + 1) :
            x0, y0 = i - x, j - y
            temp_miro[y0 + x][dis - x0 + y] = miro[i][j]

    for i in range(x, x + dis + 1):
        for j in range(y, y + dis + 1):
            if temp_miro[i][j] > 0 :
                temp_miro[i][j] -= 1
            miro[i][j] = temp_miro[i][j]

    for i in range(m) :
        dx, dy = do[i]
        if (dx, dy) == (-1, -1) :
            continue
        if x <= dx <= x + dis and y <= dy <= y + dis:
            x0, y0 = dx - x, dy - y
            do[i] = (y0 + x, dis - x0 + y)

    ox, oy = out
    x0, y0 = ox - x, oy - y
    out = (y0 + x, dis - x0 + y)

T = int(input())
for tc in range(1, T + 1) :
    # n : 미로 크기, m : 참가자 수, k : 게임 시간
    n, m, k = map(int,input().split())
    # 미로 입력 받기
    miro = [list(map(int, input().split())) for _ in range(n)]
    # 참가자 입력, 도망자라고 칭하겠음.
    do = []
    for _ in range(m) :
        r, c = map(int, input().split())
        do.append((r - 1, c - 1))
    # 출구 입력
    r, c = map(int, input().split())
    out = (r - 1, c - 1)

    # 회전 시 사용할 임시 miro
    temp_miro = [[0 for _ in range(n)] for _ in range(n)]
    answer = 0 # 참가자들의 이동거리
    # k번 반복
    for _ in range(k) :
        # 1. 참가자 이동
        mov()
        # 모두 탈출했는 지 확인
        if finish() :
            break
        # 2. 회전
        rotate()

    print(answer)
    ox, oy = out
    print(ox + 1, oy + 1)
