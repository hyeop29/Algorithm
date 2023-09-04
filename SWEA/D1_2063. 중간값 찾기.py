T = int(input())
mid_index = T//2

temp_list = list(map(int, input().split()))
temp_list.sort()

answer = temp_list[mid_index]

print(answer)
