import sys
sys.stdin = open("input.txt", "r")

from collections import defaultdict

def build(n, m, gift_info) :
    global belt_broken, head, tail

    belt_broken = [False for _ in range(m + 1)]
    head = [-1 for _ in range(m + 1)]
    tail = [-1 for _ in range(m + 1)]

    temp = [[] for _ in range(m + 1)]   # 초기 벨트와 선물의 정보를 담을 임시 2중 리스트
    for i in range(1, m + 1) :
        for j in range((n // m) * (i - 1), (n // m) * i) :
            temp[i].append(gift_info[j])
            weight[gift_info[j]] = gift_info[j + n]
            belt_info[gift_info[j]] = i

    for i in range(1, m + 1):
        for j in range(n // m - 1):
            prv[temp[i][j + 1]] = temp[i][j]
            nxt[temp[i][j]] = temp[i][j + 1]
        prv[temp[i][0]] = -1
        nxt[temp[i][-1]] = -1

        head[i] = temp[i][0]
        tail[i] = temp[i][-1]



def out() :
    pass

def remove() :
    pass

def check() :
    pass

def error() :
    pass

T = int(input())
for tc in range(1, T + 1) :
    belt_broken = [] # 벨트의 고장 정보, 고장이 났으면 True
    head, tail = [], [] # 각 벨트의 가장 앞과 뒤를 관리
    prv, nxt = dict(), dict() # 각 선물의 앞과 뒤를 관리
    weight = dict() # 선물 id 별 weight
    # 선물 id 별 벨트의 정보 / 만약 사라진 선물이면 -1 => 만약 존재하지 않는 key에 대해 호출 할 수 있으니,
    # defaultdict 사용
    belt_info = defaultdict(lambda : -1)

    # q : 명령 수
    q = int(input())
    for _ in range(q) :
        query = list(map(int, input().split()))
        if query[0] == 100 :
            build(query[1], query[2], query[3:])
            print("After build : ")
            print("belt_broken : ", belt_broken)
            print("head : ", head)
            print("tail : ", tail)
            print()
            print("prv : ", prv)
            print("nxt : ", nxt)
            print("weight : ", weight)
            print("belt_info : ", belt_info)
            print()
            break
        elif query[0] == 200 :
            out()
        elif query[0] == 300 :
            remove()
        elif query[0] == 400 :
            check()
        else : # 500번
            error()
