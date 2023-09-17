# 파일 입출력 // 제출 시 삭제해야함.
# import sys
# sys.stdin = open("input.txt", "r")

import heapq
from collections import defaultdict

INF = float("inf")

machineList = []   # 사용 가능한 채점기 번호들을 가지고 있는 Min Heap
machineStatus = [] # Tuple(채점 시작 시각, 채점 domain) 을 가지고 있다.
n = 0 # 채점기 개수
sizeQ = 0 # 채점 대기 큐 안에 있는 task 수 // 출력값
setQ = set() # 현재 대기큐에 있는 url
waitQ = defaultdict(list) # 채점 대기 큐 => (우선순위, 시간)
stringLock = defaultdict(int) # 도메인이 채점이 불가한 시간 기록

def getDomain(url) :
    return url.split('/', 1)

def setting(_n, url) :
    global n, machineList, machineStatus
    n = _n
    machineList = [i for i in range(1, n + 1)]
    machineStatus = [None for _ in range(n + 1)]

    pushQ(0, 1, url)

def pushQ(t, p, url) :
    global sizeQ
    # 채점 대기큐에 있는 task 중 동일한 url이 있을 경우는 return
    if url in setQ :
        return

    setQ.add(url)
    # waitQ에 추가하기
    domain, id = getDomain(url)
    heapq.heappush(waitQ[domain], (p, t, id))

    sizeQ += 1

def popQ(domain) :
    global sizeQ
    # 채점 대기 큐에서 삭제 ( 채점 대기 큐 => 채점 큐 이동이라고 생각하면 됨)
    _, _, id = heapq.heappop(waitQ[domain])
    # 채점 대기 큐에 있는 url 정보에서도 삭제
    setQ.remove(domain + '/' + id)
    # 채점 대기 큐에 있는 url 수 삭제
    sizeQ -= 1


def judge(t) :
    if not machineList : # 쉬고 있는 채점기가 없다면, 채점 실패
        return

    # 조건에 맞는 채점 대상 찾기
    bestPrior, bestTime, bestDomain = INF, 0, ""

    for domain, que in waitQ.items() :
        if not que :  # 해당 Domain으로 시작하는 채점 대기 URL이 없는 경우, 무시하기
            continue
        if stringLock[domain] > t :
            continue
        candPrior, candTime, _ = que[0]
        if candPrior < bestPrior or (candPrior == bestPrior and candTime < bestTime) :
            bestPrior, bestTime, bestDomain = candPrior, candTime, domain

    if bestPrior == INF : # 채점 가능한 것이 없다면 채점 실패
        return

    # 채점기 골라주기
    machineIdx = heapq.heappop(machineList)
    machineStatus[machineIdx] = (t, bestDomain)
    popQ(bestDomain) # 선택된 도메인에서 채점할 url 가져오기
    stringLock[bestDomain] = INF

def finish(t, p) :
    if machineStatus[p] == None :
        return

    start, domain = machineStatus[p]
    machineStatus[p] = None
    # 다시 사용 가능한 채점기 목록에 넣어준다.
    heapq.heappush(machineList, p)
    gap = t - start

    stringLock[domain] = start + 3 * gap



# T = int(input()) # 테스트케이스 개수 입력
T = 1
for tc in range(1, T + 1) :
    # 명령의 수 q
    q = int(input())
    for _ in range(q) :
        com = input().split()
        # 코드트리 채점기 준비
        if com[0] == "100" :
           setting(int(com[1]), com[2])
        # 채점 요청
        elif com[0] == "200" :
            pushQ(int(com[1]), int(com[2]), com[3])
        # 채점 시도
        elif com[0] == "300" :
            judge(int(com[1]))
        # 채점 종료
        elif com[0] == "400" :
            finish(int(com[1]), int(com[2]))
        else :
            print(sizeQ)
