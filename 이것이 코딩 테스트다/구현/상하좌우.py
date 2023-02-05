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
