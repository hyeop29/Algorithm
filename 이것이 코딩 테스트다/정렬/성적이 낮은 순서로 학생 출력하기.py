N = int(input())
Student = []
for i in range(N) :
  Student.append(list(input().split()))

Student = sorted(Student, key = lambda x : x[1])

for i in Student :
  print(i[0], end = " ")
