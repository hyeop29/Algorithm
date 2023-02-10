N, x = map(int,input().split())
data = list(map(int,input().split()))

count = 0

def binarysearch(start, end, array) :
  global count
  if start > end :
    return

  mid = (start + end) // 2
  if data[mid] == x :
    count += 1
    binarysearch(start, mid - 1, array)
    binarysearch(mid + 1, end, array)
    
  elif data[mid] > x :
    binarysearch(start, mid - 1, array)
  else :
    binarysearch(mid + 1, end, array)

binarysearch(0, N, data)

if count > 0 :
  print(count)
else :
  print(-1)
