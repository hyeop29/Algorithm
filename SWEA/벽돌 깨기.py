import sys
sys.stdin = open("input.txt", "r")

from collections import deque

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]    # 상, 하, 좌, 우

def in_range(x, y) :
    return 0 <= x < h and 0 <= y < w

def down_block(down_arr) :
    temp = [temp_arr[:] for temp_arr in down_arr]
    for j in range(w) :
        index = h - 1
        for i in range(h - 1, -1, -1) :
            if temp[i][j] > 0 :
                temp[index][j] = temp[i][j]
                index -= 1
        for i in range(index, -1, -1) :
            temp[i][j] = 0

    return temp

def remove(cnt, remove_arr, broken) :
    global broken_block
    if broken >= total_block :
        broken_block = total_block
        return
    if broken_block == total_block :  # 이미 답은 정해졌다.
        return
    if cnt == n :   # 모든 횟수를 다 던졌다.
        if broken > broken_block :
            broken_block = broken
        return

    q = deque()
    # 부수는 작업
    for j in range(w) :
        temp = [temp_arr[:] for temp_arr in remove_arr]
        visited = [[False for _ in range(w)] for _ in range(h)]
        temp_broken = 0
        for i in range(h) :
            if temp[i][j] > 0 :
                for dx, dy in dxy :
                    for k in range(1, temp[i][j]) :
                        nx, ny = i + dx * k, j + dy * k
                        visited[i][j] = True
                        if in_range(nx, ny) and temp[nx][ny] > 0 and not visited[nx][ny] :
                            visited[nx][ny] = True
                            q.append((nx, ny))
                temp[i][j] = 0
                temp_broken += 1
                break

        while q :
            cx, cy = q.popleft()
            for dx, dy in dxy:
                for k in range(1, temp[cx][cy]):
                    nx, ny = cx + dx * k, cy + dy * k
                    if in_range(nx, ny) and temp[nx][ny] > 0 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))

            temp[cx][cy] = 0
            temp_broken += 1

        # print("broken : ", broken)
        # print("j , cnt : ", j, cnt)
        # print("temp_broken : ", temp_broken)
        # print("temp : ")
        # for row in range(h) :
        #     print(temp[row])
        # print()
        temp = down_block(temp)
        new_broken = broken + temp_broken
        remove(cnt + 1, temp, new_broken)

T = int(input())
for tc in range(1, T + 1) :
    # n : 구슬을 던지는 횟수, w : 가로 길이, h : 세로 길이
    n, w, h = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(h)]
    # 최초의 벽돌의 개수를 측정하자
    total_block = 0
    for i in range(h) :
        for j in range(w) :
            if arr[i][j] > 0 :
                total_block += 1

    broken_block = 0 # 부순 벽돌 개수
    remove(0, arr, 0)

    print("#" + str(tc), total_block - broken_block)
