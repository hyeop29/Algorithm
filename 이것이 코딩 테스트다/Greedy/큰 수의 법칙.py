N, M, K = map(int, input().split())
Data = list(map(int, input().split()))

Data = sorted(Data, reverse = True)
count = 0 # 연산 횟수 측정
index = 0 # 배열의 인덱스
result = 0 # 연산 결과
check = 0 # 연속 K번 더하기를 확인하기 위해

while count < M :
  if check == K :
    index += 1
    result += Data[index]
    index -= 1
    check = 0
  else : 
    result += Data[index]
    check += 1
  count += 1

print(result)
