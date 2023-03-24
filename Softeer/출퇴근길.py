import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

road = [[] for _ in range(n + 1)]
roadR = [[] for _ in range(n + 1)]

for _ in range (m) :
    x, y = map(int, input().split())
    road[x].append(y)
    roadR[y].append(x)

s, t = map(int, input().split())

def dfs(start, road, visit) :
    if visit[start] :
        return
    visit[start] = True
    for i in road[start] :
        dfs(i, road, visit)
    return

fromS = [False] * (n + 1)
fromS[t] = True
dfs(s, road, fromS)

toS = [False] * (n + 1)
dfs(t, roadR, toS)

fromT = [False] * (n + 1)
fromT[s] = True
dfs(t, road, fromT)

toT = [False] * (n + 1)
dfs(s, roadR, toT)

# print("fromS : {}, toS : {}".format(fromS, toS))
# print("fromT : {}, toT : {}".format(fromT, toT))

result = 0
for i in range(1, n + 1) :
    if fromS[i] and fromT[i] and toS[i] and toT[i] :
        result += 1

print(result - 2)
