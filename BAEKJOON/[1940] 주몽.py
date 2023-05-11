n = int(input())
m = int(input())
material = list(map(int, input().split()))

start = 0
end = n - 1
answer = 0

material.sort()

while(start < end) :
  sum = material[start] + material[end]
  if sum == m :
    answer += 1
    start += 1
    end -= 1
  elif sum > m :
    end -= 1
  else :
    start += 1

print(answer)
