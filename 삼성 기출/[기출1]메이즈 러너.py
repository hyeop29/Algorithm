# input.txt 파일에 입력값 읽기
# import sys
# sys.stdin = open("input.txt", "r")

# 필요한 함수 구현
# 참가자 이동
def move() :
    global answer

    for i in range(1, m + 1) :
        if traveler[i] == exits :
            continue

        tx, ty = traveler[i]
        ex, ey = exits

        # 상하로 움직이는 것을 선호
        if tx != ex :
            nx, ny = tx, ty

            if ex > nx :
                nx += 1
            else :
                nx -= 1

            # 벽의 내구성이 0일 경우 참가자 이동
            if not board[nx][ny] :
                traveler[i] = (nx, ny)
                answer += 1
                continue

        if ty != ey :
            nx, ny = tx, ty

            if ey > ny :
                ny += 1
            else :
                ny -= 1

            if not board[nx][ny] :
                traveler[i] = (nx, ny)
                answer += 1
                continue

# 모든 참가자 탈출 여부 확인
def check_escape() :
    for i in range(1, m + 1) :
        if traveler[i] != exits :
            return False
    return True

# 가장 작은 사각형 찾기 => 가장 작은 사각형부터 늘려가며 참가자와 출구 모두 들어온 경우 찾기
def find_min_square() :
    ex, ey = exits

    # 사각형 사이즈 2부터 시작한다.
    for sz in range(2, n + 1) :

        for sx1 in range(1, n + 2 - sz) :
            for sy1 in range(1, n + 2 - sz) :
                sx2, sy2 = sx1 + sz - 1, sy1 + sz - 1

                # 출구가 없으면 볼 필요 X
                if not (sx1 <= ex <= sx2 and sy1 <= ey <= sy2) :
                    continue

                # print("sz : {}, sx1 : {} sx2: {}, sy1 : {}, sy2 : {}".format(sz, sx1, sx2, sy1, sy2))
                # 참가자 있는지 확인
                for i in range(1, m + 1) :
                    tx, ty = traveler[i]
                    # print("tx : {}, ty : {}".format(tx, ty))
                    if sx1 <= tx <= sx2 and sy1 <= ty <= sy2 and (tx != ex or ty != ey) :
                        # 참가자가 한명이라도 있다면 작은 사각형의 왼쪽 상단 좌표와 크기를 반환
                        return sx1, sy1, sz

    # 혹시 모를 예외 처리
    return -1, -1, -1

# 사각형 회전
def rotate_square() :
    # 가장 작은 사각형의 좌표와 크기를 먼저 확인한다.
    lx, ly, square_size = find_min_square()
    # print("사각형 정보 : ", lx, ly, square_size)
    if square_size == -1 :
        print("사각형을 찾지 못했습니다.")
        exit()

    # 정사각형을 회전
    for x in range(lx, lx + square_size) :
        for y in range(ly, ly + square_size) :
            # 회전 어려우니 (0, 0) 으로 놓고 생각한 후 다시 돌리자.
            ox, oy = x - lx, y - ly
            rx, ry = oy, square_size - ox - 1

            # 내구성 감소
            if board[x][y] > 0 :
                board[x][y] -= 1
            next_board[rx + lx][ry + ly] = board[x][y]

    # 회전했던 값을 진짜 board에 넣어준다.
    for x in range(lx, lx + square_size) :
        for y in range(ly, ly + square_size) :
            board[x][y] = next_board[x][y]

    # 참가자와 출구도 회전
    rotate_traveler_exits(lx, ly, square_size)

def rotate_traveler_exits(sx1, sy1, sz) :
    global exits
    # 참가자 회전
    for i in range(1, m + 1) :
        tx, ty = traveler[i]
        if sx1 <= tx < sx1 + sz and sy1 <= ty < sy1 + sz :
            ox, oy = tx - sx1, ty - sy1
            rx, ry = oy, sz - ox - 1

            traveler[i] = (rx + sx1, ry + sy1)
    # 출구 회전
    ex, ey = exits
    ox, oy = ex - sx1, ey - sy1
    rx, ry = oy, sz - ox - 1

    exits = (rx + sx1, ry + sy1)


# testcase 개수 입력 받기 (main)
# T = int(input())
T = 1
for testcase in range(1, T + 1) :
    # n : 미로 크기, m : 참가자 수, k : 게임 시간
    n, m, k = map(int, input().split())

    board = [
        [0] * (n + 1)
        for _ in range(n + 1)
    ]

    # board 입력 받기
    for i in range(1, n + 1) :
        board[i] = [0] + list(map(int, input().split()))

    # 회전을 위한 board
    next_board = [
        [0] * (n + 1)
        for _ in range(n + 1)
    ]

    # 참여자 입력 받기
    traveler = [(-1, -1)]
    for _ in range(m) :
        traveler.append(tuple(map(int, input().split())))

    # 출구 입력 받기
    exits = tuple(map(int, input().split()))

    # 정답
    answer = 0

    # print(board)

    # k초 동안 이동 및 회전 실행
    for time in range(k) :
        move()
        # print("참가 이동 후 :", traveler)
        # 참가자들이 모두 탈출 했는 지 확인
        if check_escape() :
            break

        # 미로 회전
        rotate_square()
        # print(str(time + 1) + "초: ", board)
        # print("참가자 : ", traveler)
        # print("출구 : ", exits)

    print(answer)
    print(*exits)
