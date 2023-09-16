# 파일 입출력 시 필요, 제출 시 제거 해야함.
import sys
sys.stdin = open("input.txt", "r")

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_range(x, y) -> bool : # maze를 벗어나는 지 확인
    return 0 <= x < n and 0 <= y < n

def move() :
    global answer
    for i in range(m) :
        # 이미 탈출한 참가자는 이동하지 않는다.
        if people[i] == (-1, -1) :
            continue

        person = people[i]
        mx, my = -1, -1
        # 기존 출구와의 거리 확인
        min_Dis = abs(person[0] - exy[0]) + abs(person[1] - exy[1])

        for dx, dy in dxy :
            nx, ny = person[0] + dx, person[1] + dy
            temp_Dis = abs(nx - exy[0]) + abs(ny - exy[1])
            # 조건에 맞으면 이동
            if in_range(nx, ny) and min_Dis > temp_Dis and maze[nx][ny] == 0 :
                min_Dis = temp_Dis
                mx, my = nx, ny

        if mx != -1 and my != -1 :
            people[i] = (mx, my)
            # 이동 거리(answer) + 1
            answer += 1
            # 탈출 여부 확인
            if people[i] == exy :
                people[i] = (-1, -1)

def finish() :
    for i in range(m) :
        if not people[i] == (-1, -1) :
            return False
    return True

def find_Square() :
    min_Len = float('inf')
    ex, ey = exy
    for i in range(m) :
        if people[i] == (-1, -1) :
            continue
        person = people[i]
        min_Len = min(min_Len, max(abs(ex - person[0]), abs(ey - person[1])))

    for i in range(n - min_Len) :
        for j in range(n - min_Len) :
            in_Person = False
            in_Exit = False
            for x in range(i, i + min_Len + 1) :
                for y in range(j, j + min_Len + 1) :
                    if (x, y) in people :
                        in_Person = True
                    if (x, y) == exy :
                        in_Exit = True
                    if in_Person and in_Exit :
                        return i, j, min_Len


def rotate() :
    global exy
    # 3-1. 사각형 찾기
    best_x, best_y, min_Len = find_Square()
    # 3-2. 진짜 회전
    # 회전을 위한 배열이 필요함.
    for i in range(best_x, best_x + min_Len + 1) :
        for j in range(best_y, best_y + min_Len + 1) :
            tx, ty = i - best_x, j - best_y
            nx, ny = ty, min_Len - tx
            if maze[i][j] > 0 :
                maze[i][j] -= 1
            temp_Maze[nx + best_x][ny + best_y] = maze[i][j]

            # 참가자 이동
            for p in range(m) :
                if (i, j) == people[p] and not rotate_P[p] :
                    rotate_P[p] = True
                    tx, ty = i - best_x, j - best_y
                    nx, ny = ty, min_Len - tx
                    people[p] = (nx + best_x, ny + best_y)
    # 출구 이동
    ex, ey = exy
    tx, ty = ex - best_x, ey - best_y
    nx, ny = ty, min_Len - tx
    exy = (nx + best_x, ny + best_y)

    # 회전을 위해 사용했던 임시 배열에서 진짜 배열로 이동
    for i in range(best_x, best_x + min_Len + 1) :
        for j in range(best_y, best_y + min_Len + 1) :
            maze[i][j] = temp_Maze[i][j]

    for p in range(m) :
        rotate_P[p] = False


# testcase 개수 입력 받기
T = int(input())
for tc in range(1, T + 1) :
    # 1. 입력
    # n : 지도 크기, m : 참가자 수, k : 시간
    answer = 0
    n, m, k = map(int, input().split())
    # 미로 구성
    maze = [list(map(int, input().split())) for _ in range(n)]
    # 회전을 위한 미로 생성
    temp_Maze = [[0 for _ in range(n)] for _ in range(n)]
    # 참가자들 좌표
    people = [None for _ in range(m)]
    # 참가자들 회전을 위한 bool 값
    rotate_P = [False for _ in range(m)]
    for i in range(m) :
        tx, ty = map(int, input().split())
        people[i] = (tx - 1, ty - 1)
    # 출구 좌표
    tx, ty = map(int, input().split())
    exy = (tx - 1, ty - 1)

    # k초 동안 진행
    for i in range(k) :
        # 2. 이동
        move()
        # 2-1. 모든 참가자 탈출 여부 확인
        if finish() :
            break
        # 3. 회전
        rotate()

    # 4. 출력
    print(answer)
    ex, ey = exy
    print(ex + 1, ey + 1)
