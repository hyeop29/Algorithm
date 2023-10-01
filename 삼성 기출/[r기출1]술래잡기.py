# 파일 입출력을 위한 sys // 제출 시 삭제할 것
# import sys
# sys.stdin = open("input.txt", "r")

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상, 우, 좌, 하

def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

def do_mov() :
    for i in range(m) :
        if (-1, -1) == do[i] :
            continue

        x, y = do[i]
        sx, sy = sul
        if abs(sx - x) + abs(sy - y) > 3 :
            continue

        d = do_d[i]
        dx, dy = dxy[d]
        nx, ny = x + dx, y + dy
        if in_range(nx, ny):
            # 이동하려는 칸이 술래의 칸 이면 이동 x
            if (nx, ny) != sul:
                do[i] = (nx, ny)
        else:
            do_d[i] = (d + 2) % 4
            d = do_d[i]
            dx, dy = dxy[d]

            nx, ny = x + dx, y + dy
            if(nx, ny) != sul :
                do[i] = (nx, ny)

def get_point(sul, sul_d, turn) :
    global score
    cnt = 0 # 몇 명의 도망자를 잡는지 확인하는 변수
    x, y = sul
    d = sul_d
    dx, dy = dxy[d]
    for i in range(3) :
        nx, ny = x + (i * dx), y + (i * dy)
        # print("nx, ny : ", nx, ny)
        # print("tree : ", tree)
        if in_range(nx, ny) :
            if (nx, ny) in tree :
                continue
            for j in range(m) :
                if (-1, -1) != do[j] and (nx, ny) == do[j] :
                    do[j] = (-1, -1)
                    cnt += 1

    score += (turn * cnt)

def sul_mov(turn) :
    global check, limit, now, two, sul, sul_d
    # check = True    # check가 True면 안에서 밖 // False면 밖에서 안
    # limit, now = 1, 0 # 술래는 같은 방향으로 움직인 횟수(now)가 limit이되면 방향을 바꾼다.
    # two = 0 # limit은 두번 지속된다. 그것을 관리하는 변수
    x, y = sul
    dx, dy = dxy[sul_d]
    nx, ny = x + dx, y + dy
    sul = (nx, ny)
    # print("==================================")
    # print("trun : ", turn)
    # print("limit, now, two : ", limit, now, two)
    # print("==================================")
    if check :
        now += 1
        if limit == now :
            sul_d = (sul_d + 1) % 4
            now = 0
            two += 1
            if two == 2:
                limit += 1
                now, two = 0, 0

        if sul == (0, 0) :
            check = False
            now, two = 0, -1
            limit -= 1
            sul_d = 2

    else :
        now += 1
        if limit == now :
            sul_d = (sul_d - 1) % 4
            now = 0
            two += 1
            if two == 2:
                limit -= 1
                now, two = 0, 0

        if sul == (n//2, n//2) :
            check = True
            now, two = 0, 0
            limit = 1
            sul_d = 0
    # 바뀐 술래의 좌표와 방향을 이용해 도망자를 잡아낸다.
    get_point(sul, sul_d, turn)

# T = int(input())
T = 1
for tc in range(1, T + 1) :
    # n : 격자 크기, m : 도망자 수, h : 나무 수, k : 턴 횟수
    n, m, h, k = map(int, input().split())
    # 점수를 기록할 변수
    score = 0
    # 술래의 위치와 방향
    sul = (n//2, n//2)
    sul_d = 0   # 최초 방향은 상
    # 도망자의 위치와 방향
    do = []
    do_d = []   # 1 => 우 2 => 하
    for _ in range(m) :
        x, y, d = map(int, input().split())
        do.append((x - 1, y - 1))
        do_d.append(d)
    # 나무의 위치와 방향
    tree = set()
    for _ in range(h) :
        x, y = map(int, input().split())
        tree.add((x - 1, y - 1))

    # print("sul, sul_d : ", sul, sul_d)
    # print("do, do_d : ", do, do_d)
    # print("tree : ", tree)
    # print()

    check = True    # check가 True면 안에서 밖 // False면 밖에서 안
    limit, now = 1, 0 # 술래는 같은 방향으로 움직인 횟수(now)가 limit이되면 방향을 바꾼다.
    two = 0 # limit은 두번 지속된다. 그것을 관리하는 변수
    for turn in range(1, k + 1) :
        # 도망자 이동
        do_mov()
        # print("do, do_d : ", do, do_d)
        # 술래 이동 + 점수 획득
        sul_mov(turn)
        # print("sul, sul_d : ", sul, sul_d)
        # print("score : ", score)
        # print()

    print(score)
