#모험가 길드
N = int(input())
data = list(map(int,input().split()))

data.sort()
result, temp, count = 0, 0, 0 

for i in data :
  if i == 1 :
    result += 1
    continue
    
  else :
    count += 1
    if temp < i :
      temp = i
  
  if count == temp :
    count, temp = 0, 0
    result += 1

print(result)
