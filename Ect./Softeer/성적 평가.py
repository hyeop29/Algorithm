import sys
import copy

N = int(input())
data = []
result = []
copyarr = []

for _ in range(3) :
    data.append(list(map(int,input().split())))

for i in range(N) :
    result.append(data[0][i] + data[1][i] + data[2][i])
data.append(result)

def rank(arr) :
    copyarr = copy.deepcopy(arr)
    arr.sort(reverse = True)    
    for i in copyarr :
        binarySearch(0, N - 1, arr, i)


def binarySearch(start, end , arr, i) :
    mid =  (start + end) // 2
    if arr[mid] == i :
        if arr[mid - 1] == i :
            count = check(arr, i, mid, 0)
            print(mid - count + 1, end = " ")
        else :
            print(mid + 1, end = " ")
    elif arr[mid] < i :
        binarySearch(0, mid - 1, arr, i)

    else :
        binarySearch(mid + 1, end, arr, i)

def check(arr, i, mid, count) :
    while(arr[mid - 1] == i) :
        mid -= 1
        if mid < 0 :
            break
        count += 1
    return count
        
for i in range(4) :

    rank(data[i])
    if i != 3 :
        print()
