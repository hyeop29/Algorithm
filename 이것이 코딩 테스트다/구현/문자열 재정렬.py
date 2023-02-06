S = list(input())

S.sort()
str_S = []
temp = 0
check = False

for i in S :
  if "A" <= i and i <= "Z" :
    str_S.append(i)
  else :
    check = True
    temp += int(i)

if check :
  str_S.append(str(temp))
  
result = "".join(str_S)
print(result)
