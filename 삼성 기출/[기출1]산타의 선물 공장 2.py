def build(n, m, gift) :
    global head, tail, cnt, pre, nxt
    head = [0 for _ in range(n)]
    tail = [0 for _ in range(n)]
    cnt = [0 for _ in range(n)]
    pre = [0 for _ in range(m + 1)]
    nxt = [0 for _ in range(m + 1)]

    temp = [[] for _ in range(n)]
    for i in range(1, m + 1) :
        temp[gift[i - 1] - 1].append(i)

    for i in range(n) :
        cnt[i] = len(temp[i])

        if cnt[i] == 0 :
            head[i] = -1
            tail[i] = -1
            continue

        head[i] = temp[i][0]
        tail[i] = temp[i][-1]

        for j in range(cnt[i] - 1) :
            nxt[temp[i][j]] = temp[i][j + 1]
            pre[temp[i][j + 1]] = temp[i][j]

        pre[head[i]] = -1
        nxt[tail[i]] = -1

def mov(m_src, m_dst) :

    if cnt[m_src - 1] > 0 :
        if cnt[m_dst - 1] == 0 :
            tail[m_dst - 1] = tail[m_src - 1]
            head[m_dst - 1] = head[m_src - 1]
        else :
            pre[head[m_dst - 1]] = tail[m_src - 1]
            nxt[tail[m_src - 1]] = head[m_dst - 1]

            head[m_dst - 1] = head[m_src - 1]

        head[m_src - 1], tail[m_src - 1] = -1, -1
        cnt[m_dst - 1] += cnt[m_src - 1]
        cnt[m_src - 1] = 0

    print(cnt[m_dst - 1])

def change_head(m_src, m_dst) :
    if cnt[m_src - 1] + cnt[m_dst - 1] == 0 : # 두 벨트 모두 선물개수 0개
        pass
    elif cnt[m_src - 1] != 0 and cnt[m_dst - 1] != 0 : # 두 벨트 모두 선물 0개 이상

        if cnt[m_src - 1] == 1 and  cnt[m_dst - 1] == 1 :
            head[m_src - 1], head[m_dst - 1] = head[m_dst - 1], head[m_src - 1]
            tail[m_src - 1], tail[m_dst - 1] = tail[m_dst - 1], tail[m_src - 1]
        elif cnt[m_src - 1] == 1 :
            nxt[head[m_src - 1]], nxt[head[m_dst - 1]] = nxt[head[m_dst - 1]], nxt[head[m_src - 1]]
            head[m_src - 1], head[m_dst - 1] = head[m_dst - 1], head[m_src - 1]
            pre[nxt[head[m_dst - 1]]] = head[m_dst - 1]

            tail[m_src - 1] = head[m_src - 1]
        elif cnt[m_dst - 1] == 1 :
            nxt[head[m_src - 1]], nxt[head[m_dst - 1]] = nxt[head[m_dst - 1]], nxt[head[m_src - 1]]
            head[m_src - 1], head[m_dst - 1] = head[m_dst - 1], head[m_src - 1]
            pre[nxt[head[m_src - 1]]] = head[m_src - 1]

            tail[m_dst - 1] = head[m_dst - 1]
        else :
            nxt[head[m_src - 1]], nxt[head[m_dst - 1]] = nxt[head[m_dst - 1]], nxt[head[m_src - 1]]
            head[m_src - 1], head[m_dst - 1] = head[m_dst - 1], head[m_src - 1]
            pre[nxt[head[m_src - 1]]], pre[nxt[head[m_dst - 1]]] = head[m_src - 1], head[m_dst - 1]

    elif cnt[m_src - 1] == 0 :
        if cnt[m_dst - 1] == 1 :
            head[m_src - 1] = head[m_dst - 1]
            tail[m_src - 1] = head[m_src - 1]

            head[m_dst - 1], tail[m_dst - 1] = -1, -1
        else :
            head[m_src - 1] = head[m_dst - 1]
            tail[m_src - 1] = head[m_src - 1]
            head[m_dst - 1] = nxt[head[m_src - 1]]

            pre[head[m_dst - 1]] = -1
            nxt[head[m_src - 1]] = -1

        cnt[m_src - 1] += 1
        cnt[m_dst - 1] -= 1

    elif cnt[m_dst - 1] == 0 :
        if cnt[m_src - 1] == 1 :
            head[m_dst - 1] = head[m_src - 1]
            tail[m_dst - 1] = head[m_dst - 1]

            head[m_src - 1], tail[m_src - 1] = -1, -1
        else :
            head[m_dst - 1] = head[m_src - 1]
            tail[m_dst - 1] = head[m_dst - 1]
            head[m_src - 1] = nxt[head[m_dst - 1]]

            pre[head[m_src - 1]] = -1
            nxt[head[m_dst - 1]] = -1

        cnt[m_dst - 1] += 1
        cnt[m_src - 1] -= 1

    print(cnt[m_dst - 1])

def divide(m_src, m_dst) :
    if cnt[m_src - 1] // 2 == 0 :
        pass
    else :
        temp = cnt[m_src - 1] // 2

        mid = head[m_src - 1]
        for _ in range(temp - 1) :
            mid = nxt[mid]

        if cnt[m_dst - 1] == 0 :
            head[m_dst - 1] = head[m_src - 1]
            tail[m_dst - 1] = mid
            head[m_src - 1] = nxt[mid]
            nxt[mid] = -1
            pre[head[m_src - 1]] = -1

        else :
            ori_src_head = head[m_dst - 1]
            pre[head[m_dst - 1]] = mid
            head[m_dst - 1] = head[m_src - 1]
            head[m_src - 1] = nxt[mid]
            pre[head[m_src - 1]] = -1

            nxt[mid] = ori_src_head

        cnt[m_dst - 1] += temp
        cnt[m_src - 1] -= temp

    print(cnt[m_dst - 1])

def gift_info(p_num) :
    a = pre[p_num]
    b = nxt[p_num]

    print(a + 2 * b)

def belt_info(b_num) :
    a = head[b_num - 1]
    b = tail[b_num - 1]
    c = cnt[b_num - 1]

    print(a + 2 * b + 3 * c)

T = 1
for tc in range(1, T + 1) :
    head, tail, cnt, pre, nxt = [], [], [], [], []

    # q : 명령어 수
    q = int(input())
    for _ in range(q) :
        query = list(map(int, input().split()))
        if query[0] == 100 :
            build(query[1], query[2], query[3:])
        elif query[0] == 200 :
            mov(query[1], query[2])
        elif query[0] == 300 :
            change_head(query[1], query[2])
        elif query[0] == 400 :
            divide(query[1], query[2])
        elif query[0] == 500 :
            gift_info(query[1])
        else :
            belt_info(query[1])
