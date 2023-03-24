# 병사 배치하기
# N 입력받기
N = int(input())
# 병사에 대한 정보 입력받기
soilder = list(map(int,input().split()))
# 오름차순으로 정렬
soilder.reverse()

d = [1] * N

for i in range(N) :
  for j in range(i) :
    if soilder[j] < soilder[i] :
      d[i] = max(d[j] + 1, d[i])

print(N - max(d))
