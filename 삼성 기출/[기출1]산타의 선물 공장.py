# 파일 입출력을 하기 위한 sys / 제출 시 주석 처리할 것
# import sys
# sys.stdin = open("input.txt", "r")

from collections import defaultdict

# 상자 id 별 belt 정보, 다음 상자, 이전 상자, 무게 보관
belt_info = defaultdict(lambda : -1)
prv, nxt = defaultdict(lambda : 0), defaultdict(lambda : 0)
weight = {}

# belt 별 head, tail, 부모 belt, 고장 여부 보관
head, tail = [0 for _ in range(10)], [0 for _ in range(10)]
parent_belt = [i for i in range(10)]
broken = [False for _ in range(10)]

n, m = -1, -1

def build_fac(_n, _m, etc) :
    global belt_info, prv, nxt, weight, head, tail, parent_belt, broken, n, m
    # 상자 id 별 belt 정보, 다음 상자, 이전 상자, 무게 보관
    belt_info = defaultdict(lambda: -1)
    prv, nxt = defaultdict(lambda: 0), defaultdict(lambda: 0)
    weight = {}

    # belt 별 head, tail, 부모 belt, 고장 여부 보관
    head, tail = [0 for _ in range(10)], [0 for _ in range(10)]
    parent_belt = [i for i in range(10)]
    broken = [False for _ in range(10)]

    # n : 상자 개수, m : 벨트 개수
    n, m = _n, _m
    temp_id, temp_w = etc[:n], etc[n:]

    # id마다 무게 관리
    for i in range(n) :
        weight[temp_id[i]] = temp_w[i]

    # 벨트 별로 상자를 넣어 준다.
    size = n//m
    for i in range(m) :
        # 각 벨트의 head, tail 정보 기입
        head[i] = temp_id[i * size]
        tail[i] = temp_id[(i + 1) * size - 1]

        for j in range(i * size, (i + 1) * size) :
            # 상자 id가 어떤 벨트에 있는 지 기입
            # print("temp_id[j] : ", temp_id[j])
            belt_info[temp_id[j]] = i

            # 상자 id별 nxt, prv 기입
            if j < (i + 1) * size - 1 :
                nxt[temp_id[j]] = temp_id[j + 1]
                prv[temp_id[j + 1]] = temp_id[j]

def remove_id(_id, remove_belt) :
    b = belt_info[_id]
    b_num = parent_belt[b]

    if remove_belt :
        belt_info[_id] = -1

    # 원소가 하나인 경우
    if head[b_num] == tail[b_num] :
        head[b_num] = tail[b_num] = 0
    # 원소가 head인 경우
    elif head[b_num] == _id :
        n_id = nxt[_id]

        head[b_num] = n_id
        prv[n_id] = 0
    # 원소가 taild인 경우
    elif tail[b_num] == _id :
        p_id = prv[_id]

        tail[b_num] = p_id
        nxt[p_id] = 0
    # 그외의 경우
    else :
        n_id = nxt[_id]
        p_id = prv[_id]

        nxt[p_id] = n_id
        prv[n_id] = p_id

    # 삭제 된 값에 대한 처리
    prv[_id] = nxt[_id] = 0

def hacha(w_max) :
    total = 0
    for i in range(m) :
        if broken[i] or head[i] == 0 :
            continue

        h_id = head[i]
        w = weight[h_id]

        # 물건 하차 가능하다면 하차 시킨다.
        if w <= w_max :
            total += w

            # 하차 진행
            remove_id(h_id, True)
        # 물건이 하차 불가하다면, 가장 뒤로 보내준다.
        elif nxt[h_id] != 0 :
            remove_id(h_id, False)

            tail_id = tail[i]

            prv[h_id] = tail_id
            nxt[tail_id] = h_id

            tail[i] = h_id
    print(total)

def remove(r_id) :
    # print("weight :", weight)
    # print("belt_info : ", belt_info)
    # print("belt_info[r_id] : ", belt_info[r_id])
    # print()
    if belt_info[r_id] == -1 :
        print(-1)
        return

    remove_id(r_id, True)
    print(r_id)

def check(f_id) :
    # print("400400400400 : ", belt_info)
    if belt_info[f_id] == -1 :
        print(-1)
        return

    b = belt_info[f_id]
    b_num = parent_belt[b]
    # 해당 상자가 head가 아니라면 당겨준다.
    if head[b_num] != f_id :
        ori_tail = tail[b_num]
        ori_head = head[b_num]

        # tail 갱신
        now_tail = prv[f_id]
        tail[b_num] = now_tail
        nxt[now_tail] = 0

        # 기존 tail의 nxt를 head로,
        # head의 prv를 기존 tail로 변경
        nxt[ori_tail] = ori_head
        prv[ori_head] = ori_tail

        # 새로 head를 지정한다.
        head[b_num] = f_id

    print(b_num + 1)

def error(b_num) :
    b_num -= 1
    # 이미 망가져있는 경우 -1을 출력한다
    if broken[b_num] :
        print(-1)
        return

    broken[b_num] = True

    # 빈 벨트의 경우
    if head[b_num] == 0 :
        print(b_num + 1)
        return

    # 오른쪽으로 이동하며 옮겨준다
    nxt_num = b_num
    while True :
        nxt_num = (nxt_num + 1) % m
        if not broken[nxt_num] :
            # 벨트가 비어 있다면 그대로 옮겨준다.
            if tail[nxt_num] == 0 :
                head[nxt_num] = head[b_num]
                tail[nxt_num] = tail[b_num]

            else :
                b_head = head[b_num]
                nxt_tail = tail[nxt_num]

                nxt[nxt_tail] = b_head
                prv[b_head] = nxt_tail

                tail[nxt_num] = tail[b_num]
            break

    for i in range(m) :
        if parent_belt[i] == b_num :
            parent_belt[i] = nxt_num

    print(b_num + 1)


# testcase 수 입력 받기
# T = int(input())
T = 1
# testcase 수 만큼 반복
for tc in range(1, T + 1) :
    # q : 명령 수
    q = int(input())
    for _ in range(q) :
        com = list(map(int, input().split()))
        if com[0] == 100 :
            build_fac(com[1], com[2], com[3:])
        elif com[0] == 200 :
            hacha(com[1])
        elif com[0] == 300 :
            remove(com[1])
        elif com[0] == 400 :
            check(com[1])
        else :
            error(com[1])
        # print()
        # print(com)
        # print("prv : ", prv)
        # print("nxt : ", nxt)
        # print("weight : ", weight)
        # print("belt_info : ", belt_info)

        # print("head : ", head)
        # print("tail : ", tail)

        # print("parent_belt : ", parent_belt)
        # print("broken : ", broken)
        # print()
