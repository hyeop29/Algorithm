# import sys
# sys.stdin = open("input.txt", "r")

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우, 하, 좌, 상
line_dxy = [(0, -1), (1, 0), (0, 1), (-1, 0)] # 좌, 하, 우, 상

def attack(d, p) :
    global answer

    tx, ty = n // 2, n // 2
    dx, dy = dxy[d]

    for i in range(1, p + 1) :
        monster = gido[tx + dx * i][ty + dy * i]
        answer += monster
        gido[tx + dx * i][ty + dy * i] = 0

def mov() :
    # line 으로 옮기자
    tx, ty = n // 2, n // 2
    check = 0 # dis 1, 1, 2, 2, 3, 3 두번 반복 후 증가하는 점을 이용
    cnt, dis = 0, 1 # dis칸 만큼 이동하면 방향 변경
    mov_d = 0
    index = 0

    while ty != -1 : # o(n * n)
        # print("tx, ty : ", tx, ty)
        # print("mov_d : ", mov_d)
        line[index] = gido[tx][ty]
        gido[tx][ty] = 0
        dx, dy = line_dxy[mov_d]
        tx, ty = tx + dx, ty + dy

        cnt += 1
        index += 1

        if cnt == dis :
            mov_d = (mov_d + 1) % 4
            check += 1
            cnt = 0
            if check == 2 :
                dis += 1
                check = 0

    # 빈칸으로 당겨주면 된다.
    index = 0
    # print("mov before real_line : ", real_line)
    for i in range(n * n) :
        if line[i] != 0 :
            real_line[index] = line[i]
            index += 1
        line[i] = 0

def check_four() :
    cnt, num = 0, -1
    for i in range(1, n * n) :
        if real_line[i] == 0 :
            break

        if num != real_line[i] :
            num = real_line[i]
            cnt = 1
        else :
            cnt += 1

        if cnt >= 4 :
            # print("four over (num, cnt, i): ", num, cnt, i)
            return True

    return False
def under_four() :
    global answer
    # 일단 중복된 4번을 제거해준다.
    cnt, num = 0, -1
    temp = [1]
    for i in range(1, n * n) :
        if num != real_line[i] :
            if cnt >= 4 :
                answer += num * cnt
                for t in temp :
                    real_line[t] = 0
            num = real_line[i]
            cnt = 1
            temp = [i]
        else :
            temp.append(i)
            cnt += 1

        # 가장 마지막 경우를 고려하자
        if i == n * n - 1 and cnt >= 4:
            answer += num * cnt
            for t in temp:
                real_line[t] = 0


        if real_line[i] == 0:
            break

    # 다시 앞으로 당겨준다.
    index = 0
    for i in range(n * n) :
        if real_line[i] != 0 :
            line[index] = real_line[i]
            index += 1
        real_line[i] = 0

    # 다시 realline으로 돌려준다.
    for i in range(n * n) :
        if line[i] == 0 :
            break
        real_line[i] = line[i]
        line[i] = 0

def new_line() :
    global real_line
    line[0] = -1
    index = 1
    cnt, num = 1, real_line[1]
    for i in range(2, n * n) :
        if num != real_line[i] :
            line[index] = cnt
            index += 1
            if index == n * n :
                break
            line[index] = num
            index += 1
            if index == n * n :
                break

            num = real_line[i]
            cnt = 1
        else :
            cnt += 1

        if i == n * n - 1 :
            line[index] = cnt
            index += 1
            if index == n * n:
                break
            line[index] = num

        if real_line[i] == 0 :
            break

    real_line = [0 for _ in range(n * n)]

    # gido 으로 옮기자
    tx, ty = n // 2, n // 2
    check = 0  # dis 1, 1, 2, 2, 3, 3 두번 반복 후 증가하는 점을 이용
    cnt, dis = 0, 1  # dis칸 만큼 이동하면 방향 변경
    mov_d = 0
    index = 0

    while ty != -1:  # o(n * n)
        if line[index] == 0 :
            break
        gido[tx][ty] = line[index]
        line[index] = 0
        dx, dy = line_dxy[mov_d]
        tx, ty = tx + dx, ty + dy

        cnt += 1
        index += 1

        if cnt == dis:
            mov_d = (mov_d + 1) % 4
            check += 1
            cnt = 0
            if check == 2:
                dis += 1
                check = 0

# T = int(input())
T = 1
for tc in range(1, T + 1) :
    # n : 격자 크기, m : 라운드 수
    n, m = map(int, input().split())
    gido = [list(map(int, input().split())) for _ in range(n)]
    gido[n // 2][n // 2] = -1 # 타워 표시
    info_round = [list(map(int, input().split())) for _ in range(m)]

    line = [0 for _ in range(n * n)]
    real_line = [0 for _ in range(n * n)]
    answer = 0

    for i in range(m) :
        d, p = info_round[i]
        # 1. 몬스터 공격
        attack(d, p)
        # print("After attack answer : ", answer)
        # print("After attack : ")
        # print("gido : ")
        # for j in range(n) :
        #     print(gido[j])
        # print()
        # 2. 비어있는 공간으로 몬스터 이동
        mov()
        # print("line : ", line)
        # print("real_line : ", real_line)
        # print()
        # 3. 4번 이상 나오면 몬스터 삭제 -> 비어있는 칸 이동 (4번 이상 몬스터 없을 때 까지 반복)
        # print("real_line [:117]", real_line[:118])
        # print("real_line : ", real_line)
        while check_four() :
            # print("!!!!!!!!!!!!!!!!")
            under_four()
        # print("After under_four answer : ", answer)
        # print("After under_four : ")
        # print("line : ", line)
        # print("real_line : ", real_line)
        # print()
        # 4. 삭제가 끝난 후 몬스터 나열, (개수, 숫자 크기) 새로운 배열 생성
        # print("gido : ")
        # for j in range(n) :
        #     print(gido[j])
        # print()
        new_line()
        # print("line : ", line)
        # print("i , answer : ", i, answer)
        # print("gido : ")
        # for j in range(n) :
        #     print(gido[j])
        # print()
        # print("--")
        # print("line : ", line)
        # print("real_line : ", real_line)
        # print("--")
        # print("i , answer : ", i, answer)

    print(answer)
