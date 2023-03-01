N = map(int,input())
Data = list(input().split())

result = [1,1]

for i in Data :
    if i == "R" :
      if result[1] == N :
        continue
      else :
        result[1] += 1
    elif i == "L" :
      if result[1] == 1 :
        continue
      else :
        result[1] -= 1
    elif i == "U" :
      if result[0] == 1 :
        continue
      else :
        result[0] -= 1
    else :
      if result[0] == N :
        continue
      else :
        result[0] += 1

# 리스트의 내용을 대괄호 없이 출력, * : 리스트 압축 해제
print(*result)




# 상하좌우
N = int(input())
plan = list((input().split()))

result = [1, 1]
move = {"L" : [0, -1], "R" : [0, 1], "U" : [-1, 0], "D" : [1, 0]}

for i in plan :
  
  if(result[0] + move[i][0] < 1 or result[0] + move[i][0] > N or result[1] + move[i][1] < 1 or result[1] + move[i][1] > N) :
    continue
  else :
    result[0] += move[i][0]
    result[1] += move[i][1]

print(result[0], result[1])
