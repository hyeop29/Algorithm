import sys
sys.stdin = open("input.txt")


dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

def snail() :
    d_index = 0
    count = 1
    cx, cy = 0, 0

    check = 1
    cnt_dis, dis = 0, n

    while(count <= n * n) :
        temp[cx][cy] = count

        cnt_dis += 1
        if cnt_dis == dis :
            check -= 1
            cnt_dis = 0
            d_index = (d_index + 1) % 4
            if check == 0 :
                check = 2
                dis -= 1


        dx, dy = dxy[d_index]
        cx, cy = cx + dx, cy + dy

        count += 1


T = int(input())

for tc in range(1, T + 1) :
    n = int(input())
    temp = [[0 for _ in range(n)] for _ in range(n)]

    snail()

    print("#" + str(tc))
    for row in temp :
        print(*row)
