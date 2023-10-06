# import sys
# sys.stdin = open("input.txt", "r")

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우

def check():
    return max(flour) - min(flour) <= k

def add():
    temp = [0]
    min = flour[0]
    for i in range(1, n):
        if min > flour[i]:
            min = flour[i]
            temp = []
            temp.append(i)
        elif min == flour[i]:
            temp.append(i)

    for i in temp:
        flour[i] += 1

def roll(a, b, c):
    # print("n - a : ", n - a)
    for i in range(n - a, n):
        for j in range(b):
            ox, oy = i - (n - a), j
            temp[oy + (n - b) - 1][a - 1 - ox] = arr[i][j]
            arr[i][j] = 0
    for i in range(b, c):
        temp[n - 1][i - b] = arr[n - 1][i]
        arr[n - 1][i] = 0

    # print("temp : ")
    # for i in range(n):
    #     print(temp[i])
    # print()

    for i in range(n - (b + 1), n):
        for j in range(c - b):
            arr[i][j] = temp[i][j]
            temp[i][j] = 0

def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

def press(a, c) :
    # print("c, a : ", c, a)
    for i in range(n - a, n) :
        for j in range(c + 1) :
            if arr[i][j] == 0 :
                continue
            for dx, dy in dxy :
                nx, ny = i + dx, j + dy
                if in_range(nx, ny) and arr[i][j] < arr[nx][ny] :
                    d = (arr[nx][ny] - arr[i][j]) // 5
                    temp[i][j] += d
                    temp[nx][ny] -= d
    # print("temp : ")
    # for i in range(n):
    #     print(temp[i])
    # print()
    for i in range(n - a, n) :
        for j in range(c + 1) :
            if temp[i][j] == 0 :
                continue
            arr[i][j] += temp[i][j]
            temp[i][j] = 0

    # print("arr : ")
    # for i in range(n):
    #     print(arr[i])
    # print()

    # 다시 flour 형태로 바꿔줘야함
    # 열이 작은 것부터 나열하고, 열이 같다면 행이 큰 것부터 순서대로 좌측에 배치
    cnt = 0
    for j in range(c + 1):
        for i in range(n - 1, n - a - 1, -1) :
            if arr[i][j] == 0 :
                continue
            flour[cnt] = arr[i][j]
            arr[i][j] = 0
            cnt += 1

def fold() :
    for i in range(n):
        arr[n - 1][i] = flour[i]

    # n/2 만큼 180도 뒤집은 다음 위로 올려주고, 나머지는 왼쪽으로 가져온다.
    for i in range(n // 2) :
        arr[n - 1 - 1][n // 2 - 1 - i] = arr[n - 1][i]
    for i in range(n // 2, n) :
        arr[n - 1][i - n // 2] = arr[n - 1][i]
        arr[n - 1][i] = 0

    # 그 상태에서 /2 만큼 접고 180도 접고, 나머지는 왼쪽으로 가져온다.
    for i in range(n // 4) :
        arr[n - 1 - 3][n // 4 - 1 - i] = arr[n - 1][i]
        arr[n - 2 - 1][n // 4 - 1 - i] = arr[n - 2][i]
    for i in range(n // 4, n) :
        arr[n - 1][i - n // 4] = arr[n - 1][i]
        arr[n - 2][i - n // 4] = arr[n - 2][i]
        arr[n - 1][i], arr[n - 2][i] = 0, 0

    # print("arr : ")
    # for i in range(n):
    #     print(arr[i])
    # print()

# T = int(input())
T = 1
for tc in range(1, T + 1):
    # n : 배열의 크기, k : 최댓값과 최솟값의 차이
    n, k = map(int, input().split())
    temp = [[0 for _ in range(n)] for _ in range(n)] # roll에 사용할 임시 list
    arr = [[0 for _ in range(n)] for _ in range(n)]
    flour = list(map(int, input().split()))

    # 각 위치의 밀가루 양의 최댓값과 최솟값의 차이가 K 이하가 될 때까지 반복
    cnt = 0
    while not check():
        # 1. 밀가루 양이 가장 작은 위치에 밀가루 1만큼 더 넣어준다. (가장 작은 위치가 여러 개라면 모두 넣기)
        add()
        # print("flour : ", flour)
        # 2. 도우를 말아준다.
        for i in range(n):
            arr[n - 1][i] = flour[i]
        a, b, c = 1, 1, n
        while a <= c - b:
            # print("a, b, c :", a, b, c)
            roll(a, b, c)
            _a = a
            a = b + 1
            c = c - b
            b = _a
        #     print("After roll a, b, c :", a, b, c)
        #     print()
        # print("arr : ")
        # for i in range(n):
        #     print(arr[i])
        # print()
        # 3. 도우를 꾹 눌러준다.
        # print("After press : ")
        press(a, c)
        # print("flour : ", flour)
        # 4. 도우를 두 번 반으로 접어준다.
        # print("After fold : ")
        fold()
        # 5. 3의 과정 반복
        press(4, n // 4)
        # print("After second press : ")
        # print("flour : ", flour)
        cnt += 1

    # 출력 : 최소 연산 횟수
    print(cnt)
