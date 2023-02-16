T = int(input())
result = []
for _ in range(T) :
  n, m = map(int,  input().split())
  data = list(map(int, input().split()))
  gold = [[0 for _ in range(m)] for _  in range(n)]
  count = 0
  
  for i in range(n) :
    for j in range(m) :
      gold[i][j] = data[count]
      count += 1

  for i in range(1, m) :
    for j in range(n) :
      if j == 0 :
        left_top = 0
      else :
        left_top = gold[j - 1][i - 1]

      mid = gold[j][i - 1]

      if j == n - 1 :
        left_down = 0
      else :
        left_down = gold[j + 1][i - 1]

      gold[j][i] = max(left_top, mid, left_down) + gold[j][i]

  max_gold = 0
  for i in range(n) :
    if max_gold < gold[i][m - 1] :
      max_gold = gold[i][m - 1]
  result.append(max_gold)
  
for i in result :
  print(i)
