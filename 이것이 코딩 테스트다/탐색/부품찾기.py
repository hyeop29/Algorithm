N = int(input())
data = list(map(int,input().split()))
data.sort()
M  = int(input())
request = list(map(int, input().split()))

def binary_search(start, end, data, x) :
  if start > end :
    return False

  mid = (start + end) // 2
  if data[mid] == x :
    return True
  elif data[mid] > x :
    return binary_search(start, mid - 1, data, x)
  else :
    return binary_search(mid + 1, end, data, x)

for i in request :
  if binary_search(0, N - 1, data, i) :
    print("yes", end = '')
  else :
    print("no", end = '')
