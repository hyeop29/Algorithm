from collections import deque

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상, 우, 하, 좌 (시계방향)

def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

def change_under(d) :
    global under, ufs

    if d == 0 : # 주사위를 위로 굴린다.
        under = 7 - ufs[1]  # under는 기존 주사위의 front 반대 방향값
        # 위 : 기존 값 front, 앞 : 기존 up 반대 값, side 유지
        ufs = [ufs[1], 7 - ufs[0], ufs[2]]
    elif d == 1 : # 주사위를 오른쪽으로 굴린다.
        under = ufs[2] # under는 기존 주사위의 side(오른쪽 옆)값
        # 위 : 기존 주사위의 side값 반대편, 앞 : 유지, side 기존 위의 값
        ufs = [7 - ufs[2], ufs[1], ufs[0]]
    elif d == 2 : # 주사위를 아래로 굴린다.
        under = ufs[1] # under은 기존 주사위의 front 값
        # 위 : 기존 주사위의 front 값 반대편, 앞 : 기존 위의 값, side : 유지
        ufs = [7 - ufs[1], ufs[0], ufs[2]]
    else : # 주사위를 왼쪽으로 굴린다.
        under = 7 - ufs[2] # under은 기존 주사위의 오른쪽 반대편 값
        # 위 : 기존 주사위의 오른쪽, 앞 : 유지, side : 기존 위의 값 반대편
        ufs = [ufs[2], ufs[1], 7 - ufs[0]]

def roll() :
    global pos, d
    # pos, under, d(방향) 변경
    # pos 변경
    px, py = pos
    dx, dy = dxy[d]
    nx, ny = px + dx, py + dy

    if in_range(nx, ny) :
        pos = (nx, ny)
    else :
        d = (d + 2) % 4
        dx, dy = dxy[d]
        pos = (px + dx, py + dy)

    # under 변경
    change_under(d)

    # d 변경
    px, py = pos
    if under > arr[px][py] :
        d = (d + 1) % 4
    elif under < arr[px][py] :
        d = (d - 1) % 4

def get_score() : # 점수 구하기 bfs로 구현하자
    global answer
    visited = [[False for _ in range(n)] for _ in range(n)]
    px, py = pos
    origin = arr[px][py]
    q = deque()

    visited[px][py] = True
    answer += origin
    q.append((px, py))

    while q :
        cx, cy = q.popleft()
        for dx, dy in dxy :
            nx, ny = cx + dx, cy + dy
            if in_range(nx, ny) and not visited[nx][ny] and arr[nx][ny] == origin :
                visited[nx][ny] = True
                answer += origin
                q.append((nx, ny))


# T = int(input())
T = 1
for tc in range(1, T + 1) :
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ufs = [1, 2, 3]
    pos = (0, 0) # 주사위 위치
    under = 6 # 초기 주사위 아래 값
    d = 1 # 초기 방향은 오른쪽

    answer = 0 # 점수의 합
    for _ in range(m) :
        # 주사위 굴리기
        roll()
        # 점수 획득
        get_score()

    print(answer)
