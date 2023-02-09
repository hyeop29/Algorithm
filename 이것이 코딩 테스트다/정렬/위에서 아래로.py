N = int(input())

data = []
for _ in range(N) :
  data.append(int(input()))

data.sort(reverse = True)
print(*data)
