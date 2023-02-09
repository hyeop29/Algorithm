"""
Project : 정수형 난수 리스트의 정렬 및 경과시간 측정
(1) 중복되지 않는 정수형 (int) 난수를 지정된 개수 (예: 10,000 ~ 1,000,000) 만큼 생성하는 함수
genBigRandList(L,n)을 구현하라. 이 함수에는 리스트 L과 리스트에 포함될 중복되지 않는 난수의 개수 n이 전달된다.
(2) 주어진 리스트의 첫 부분 2줄 (한 줄에 10개씩)과 마지막 2줄을 출력하는 함수 printListSample(L, per_line, sample_lines)
를 구현하라.
(3) 주어진 리스트의 원소들을 오름차순으로 병합정렬 구조로 정렬하는 함수 mergeSort(L) 함수를 구현하라.
(4) 표준입력장치로 부터 100,000 이상 크기의 정수형 난수 개수를 입력 받은 후, genBigRandList() 함수를 사용하여 중복되지 않는
정수형 난수 리스트를 생성하고, 이를 printListSample() 함수를 사용하여 출력하라. 이 정수형 난수 리스트를 mergeSort() 함수를
사용하여 정렬하고, 정렬된 상태를 printListSample() 함수를 사용하여 출력하라.
(5) 정렬에서 걸린 시간을 time 모듈의 time() 메소드를 사용하여 측정하고, 출력하라.
Author: Chang‐Hyeop LEE
Date of last update: December. 29, 2022
"""
import random
import time

def genBigRandList(L, n) :
    L = (random.sample(range(0, n),n))
    return L

def printListSample(L, per_line, sample_lines) :
    count = 1
    if per_line * sample_lines > len(L) :
        for i in range(len(L)) :
            print("{:6d}".format(L[i]), end=' ')
            count += 1
            if count > per_line :
                count = 1
                print("")
    else :
        for i in range(per_line * sample_lines) :
            print("{:6d}".format(L[i]), end=' ')
            count += 1
            if count > per_line :
                count = 1
                print("")

        count = 1
        k = len(L) - per_line * sample_lines
        print(". . . . . .")
        for i in range(k, len(L)) :
            print("{:6d}".format(L[i]), end=' ')
            count += 1
            if count > per_line :
                count = 1
                print("")

def merge(L1, L2):
    temp = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2) :
        if L1[i] < L2[j] :
            temp.append(L1[i])
            i += 1
        else :
            temp.append(L2[j])
            j += 1
    if i < len(L1) :
        temp.extend(L1[i:])
    else :
        temp.extend(L2[j:])    
    return temp

def mergeSort(L) :
    if len(L) > 1 :
        mid = len(L) // 2
        L1 = mergeSort(L[:mid])
        L2 = mergeSort(L[mid:])
        return merge(L1, L2)
    else :
        return L

n = int(input("Input size of random list L(-1 to quit) = "))
if n == -1 :
    exit()
else :
    L = []
    L = genBigRandList(L, n)
    print("Before mergeSort of L : ")
    printListSample(L, 10, 2)
    start_t = time.time()
    L = mergeSort(L)
    end_t = time.time()
    print("After mergeSort of L : ")
    printListSample(L, 10, 2)
    print("mergeSort() for list L (size = {}) took {} sec" .format(n, end_t - start_t))
