N,  M  = map(int,input().split())
ricecake = list(map(int, input().split()))
result = 0

def cut (start, end, result) :
  if start >= end :
    print(result)
    return
  temp = []
  mid = (end + start) // 2

  for i in range(len(ricecake)) :
    if ricecake[i] - mid > 0:
      temp.append(ricecake[i] - mid)
      
  if sum(temp) > M :
    cut(mid + 1, end, result)
  else :
    result = mid
    cut(start, mid - 1, result)

cut(0, max(ricecake), result)
