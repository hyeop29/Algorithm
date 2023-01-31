S = input()
answer = 0

for i in S :
  i = int(i)
  if i <= 1 or answer <= 1 :
    answer += i
  else :
    answer *= i

print(answer)
