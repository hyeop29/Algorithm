import sys
sys.stdin = open("input.txt", "r")

def check() :
    return max(flour) - min(flour) <= k

def add() :
    temp = [0]
    min = flour[0]
    for i in range(1, n) :
        if min > flour[i] :
            min = flour[i]
            temp = []
            temp.append(i)
        elif min == flour[i] :
            temp.append(i)

    for i in temp :
        flour[i] += 1

def _roll(a, b, c) :
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n - a, n) :
        for j in range(b) :
            ox, oy = i - (n - 1), j
            temp[oy + (n - 1) - 1][b - 1 - ox] = arr[i][j]
            arr[i][j] = 0
    for i in range(b + 1, c) :
            temp[n - 1][i - b] = arr[n - 1][i]
            arr[n - 1][i] = 0
    
    for i in range(n - (b + 1), n) :
        for j in range(c - b) :
            arr[i][j] = temp[i][j]
            temp[i][j] = 0
    
    _a = a
    a = b + 1
    b = _a
    c = c - b
    
    
def roll() :
    for i in range(n):
        arr[n - 1][i] = flour[i]
    a, b, c = 1, 1, n
    while a <= c :
        _roll(a, b, c)

T = int(input())
for tc in range(1, T + 1) :
    # n : 배열의 크기, k : 최댓값과 최솟값의 차이
    n, k = map(int, input().split())
    arr = [[0 for _ in range(n)] for _ in range(n)]
    flour = list(map(int, input().split()))

    # 각 위치의 밀가루 양의 최댓값과 최솟값의 차이가 K 이하가 될 때까지 반복
    cnt = 0
    while not check() :
        cnt += 1
        # 1. 밀가루 양이 가장 작은 위치에 밀가루 1만큼 더 넣어준다. (가장 작은 위치가 여러 개라면 모두 넣기)
        add()
        print("flour : ", flour)
        # 2. 도우를 말아준다.
        roll()
        print("arr : ")
        for i in range(n):
            print(arr[i])
        print()
        break
        # 3. 도우를 꾹 눌러준다.
        # 4. 도우를 두 번 반으로 접어준다.
        # 5. 3의 과정 반복

    # 출력 : 최소 연산 횟수
    print(cnt)
