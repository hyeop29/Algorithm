from collections import deque

def find_attacker() -> tuple : # 공격자 찾기
    ax, ay = -1, -1
    min_a = float('inf') # 초기값은 최대로 설정
    for sum in range(n + m - 2, -1, -1) :
        for j in range(m - 1, -1, -1) :
            i = sum - j
            # 만약 행 값이 n 값보다 클 경우 continue / 이미 부서진 포탑일 경우도 continue
            if i < 0 or i >= n or daepo[i][j] == 0 :
                continue
            # 공격력이 낮은 포탑을 만났다면, 값들을 갱신 해준다.
            if min_a > daepo[i][j] :
                ax, ay = i, j
                min_a = daepo[i][j]
            # 공격력이 같을 경우 공격한 지 얼마나 오래 됐는지 비교
            elif min_a == daepo[i][j] and last_attack[ax][ay] < last_attack[i][j] :
                ax, ay = i, j
                min_a = daepo[i][j]

    return ax, ay

def find_victim() -> tuple : # 공격 당할 대상 찾기
    vx, vy = -1, -1
    max_a = float('-inf') # 초기값은 최소로 설정
    for sum in range(n + m - 1) :
        for i in range(n - 1, -1, -1) :
            j = sum - i
            # 만약 열 값이 m 값보다 클 경우 continue / 이미 부서진 포탑일 경우도 continue
            if j < 0 or j >= m or daepo[i][j] == 0 :
                continue
            # 공격력이 높은 포탑을 만났다면, 값들을 갱신 해준다.
            if max_a < daepo[i][j] :
                vx, vy = i, j
                max_a = daepo[i][j]
            # 공격력이 같을 경우 공격한 지 얼마나 오래 됐는지 비교
            elif max_a == daepo[i][j] and last_attack[vx][vy] > last_attack[i][j] :
                vx, vy = i, j
                max_a = daepo[i][j]

    return vx, vy

def attack(x, y, power) : # 좌표와 power가 주어지면 해당 좌표값에 있는 곳에 power 만큼 공격
    attack_check[x][y] = True
    daepo[x][y] = max(0, daepo[x][y] - power)


def tryLaser() : # 레이저 공격 가능 여부 반환 bfs 사용
    visited = [[False for _ in range(m)] for _ in range(n)]
    # 역추적에 사용 할 리스트
    back = [[None for _ in range(m)] for _ in range(n)]
    # 우/하/좌/상
    dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))
    q = deque()
    q.append(attacker)
    visited[attacker[0]][attacker[1]] = True

    while q :
        x, y = q.popleft()
        for dx, dy in dxy :
            nx , ny = (x + dx + n) % n, (y + dy + m) % m
            if visited[nx][ny] or daepo[nx][ny] == 0 :
                continue
            q.append((nx, ny))
            visited[nx][ny] = True
            back[nx][ny] = (x, y)

    if not visited[victim[0]][victim[1]] :
        return False

    attack(victim[0], victim[1], daepo[attacker[0]][attacker[1]])
    attack_x, attack_y = back[victim[0]][victim[1]]
    while (attack_x != attacker[0] or attack_y != attacker[1]) :
        attack(attack_x, attack_y, daepo[attacker[0]][attacker[1]] // 2)
        attack_x, attack_y = back[attack_x][attack_y]

    return True

def bomb() : # 포탄 공격
    for i in (-1, 0, 1) :
        for j in (-1, 0, 1) :
            nx, ny = (victim[0] + i - n) % n, (victim[1] + j - m) % m
            # 공격자인 경우 continue
            if nx == attacker[0] and ny == attacker[1] :
                continue
            attack_power = daepo[attacker[0]][attacker[1]] // 2
            if i == 0 and j == 0 :
                attack_power = daepo[attacker[0]][attacker[1]]
            attack(nx, ny, attack_power)

def only_one() : # 포탑이 한 개 남았는 지 확인하는 함수
    count = 0
    for i in range(n) :
        for j in range(m) :
            if daepo[i][j] > 0 :
                count += 1

    return count == 1

def repair() : # 포탑 정비하기
    for i in range(n) :
        for j in range(m) :
            if not attack_check[i][j] and daepo[i][j] != 0 :
                daepo[i][j] += 1

# testcase 개수 입력
# T = int(input())
T = 1


for testcase in range(1, T + 1) :
    # n : 가로 크기, m : 세로 크기, k : 턴 횟수
    n, m, k = map(int, input().split())
    # 대포의 기존 공격력 입력
    daepo = [list(map(int, input().split())) for _ in range(n)]
    # 공격자의 개입 여부
    attack_check = [[False for _ in range(m)] for _ in range(n)]
    # 대포의 최근 공격 확인
    last_attack = [[0 for _ in range(m)] for _ in range(n)]

    # k 번의 turn 만큼 반복
    for turn in range(1, k + 1) :
        # 1. 공격자 선정
        attacker = find_attacker()
        last_attack[attacker[0]][attacker[1]] = turn
        attack_check[attacker[0]][attacker[1]] = True
        # 2 - 1. 공격대상 선택
        victim = find_victim()
        # 공격자 핸디캡
        daepo[attacker[0]][attacker[1]] += n + m
        # 2 - 2. 레이저 공격 여부 확인 / 반환값 : 가능하면 True , 불가하면 False
        # 2 - 3. 레이저 공격 불가 시 포탄 공격 진행
        if not tryLaser() :
            bomb()
        if only_one() : # 대포가 1개가 된다면 그 즉시 중지
            break
        # 3. 포탑 정비
        repair()
        # 공격자의 개입 여부 초기화
        attack_check = [[False for _ in range(m)] for _ in range(n)]

    victim = find_victim()
    print(daepo[victim[0]][victim[1]])
