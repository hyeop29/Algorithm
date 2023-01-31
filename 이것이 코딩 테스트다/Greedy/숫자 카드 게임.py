N, M = map(int, input().split())
for i in range(N) :
  data = list(map(int, input().split()))
  if i == 0 : # 가장 첫 행의 경우 비교대상이 없으므로
    result = min(data)
  else :
    if result < min(data) :
      result = min(data)

print(result)
