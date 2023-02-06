S = list(input())

S.sort()
str_S = []
temp = 0

for i in S :
  if "A" <= i and i <= "Z" :
    str_S.append(i)
  else :
    temp += int(i)

result = "".join(str_S)
print(result + "" + str(temp))
