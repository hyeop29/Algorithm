from collections import deque
tc = int(input())

for _ in range(tc) :
  n, m = map(int, input().split())
  temp = list(map(int, input().split()))
  q = deque([])
  for i in range(n) :
    q.append([temp[i], i])
  
  count = 0
  while q :
    priority = q.popleft()
    if q and priority[0] < max(q)[0] :
      q.append(priority)
    else :
      count += 1
      if priority[1] == m :
        print(count)
