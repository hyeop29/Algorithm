N, M = map(int,input().split())
d = [10001] * (M + 1)

coin = []
for _ in range(N) :
  coin.append(int(input()))
  
d[0] = 0

for i in coin :
  for j in range(i, M + 1) :
    if (j - i) < 10001 : 
      d[j] = min(d[j], d[j - i] + 1)

if d[M] == 10001 :
  print(-1)
else :
  print(d[M])
