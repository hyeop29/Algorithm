N = int(input())
result = 0

for i in range((N + 1) * 60 * 60) :
  h = i // 3600
  m = (i - h * 3600) // 60
  s = (i - h * 3600 - m * 60) % 60
  time = str(h) + str(m) + str(s)
  if "3" in time :
    result += 1

print(result)
