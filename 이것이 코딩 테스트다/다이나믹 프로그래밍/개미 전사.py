N = int(input())
data = list(map(int, input().split()))

d = [0] * N

for i in range(N) :
  if i == 0 :
    d[i] = data[i]
  elif i == 1 :
    d[i] = max(d[i - 1], data[i])
  else :
    d[i] = max(d[i -1], d[i - 2] + data[i])

print(d[N - 1])
