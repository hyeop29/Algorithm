import sys
import math

N, B = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
result = 0

max_a = int(a[N - 1] + pow(B,0.5))

def cal_fee(mid, a_list) :
    fee = 0
    for i in a_list :
        if mid > i :
            fee += pow(mid - i, 2)
    return fee

def binarysearch(start, end, a_list, temp) :
    if start > end :
        return temp
    mid = (start + end) // 2
    # print("mid : {}, start : {}, end : {}, cal : {}".format(mid, start, end, cal_fee(mid, a_list)))
    if(cal_fee(mid, a_list) <= B) :
        temp = mid
        return binarysearch(mid + 1, end, a_list, temp)
    else :
        return binarysearch(start, mid - 1, a_list, temp)

result = binarysearch(a[0], max_a, a, 0)

print(result)
