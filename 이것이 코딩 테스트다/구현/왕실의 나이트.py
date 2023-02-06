y, x = input()
result = 0
col = [0, "a", "b", "c", "d", "e", "f", "g", "h"]
y = col.index(y)

dx1 = [2, -2]
dy1 = [1, -1]

x = int(x)

for i in range(len(dx1)):
  for j in range(len(dy1)):
    ex = x + dx1[i]
    ey = y + dy1[j]
    if ex > 0 and ex < 9 and ey > 0 and ey < 9:
      result += 1

dx1 = [1, -1]
dy1 = [2, -2]
for i in range(len(dx1)):
  for j in range(len(dy1)):
    ex = x + dx1[i]
    ey = y + dy1[j]
    if ex > 0 and ex < 9 and ey > 0 and ey < 9:
      result += 1

print(result)
