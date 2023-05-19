t = int(input())
k = int(input())

coins = []
for _ in range(k) :
  coins.append(list(map(int, input().split())))

dp = [0 for _ in range(t + 1)]
dp[0] = 1
for c, num in coins :
  for i in range(t, 0, -1) :
    for j in range(1, num + 1) :
      if i - c * j < 0 :
        continue
      dp[i] += dp[i - (c * j)]

print(dp[t])
