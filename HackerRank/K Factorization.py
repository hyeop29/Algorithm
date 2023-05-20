#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kFactorization' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY A
#

def kFactorization(n, A, k):
    answer = [n]
    A.sort(reverse = True)
    index = 0
    while index < k :

        if n % A[index] == 0 :
            answer.append(n//A[index])
            n = n // A[index]
            if n == 1 :
                break
            
        else :
            index += 1
            
    answer.reverse()
    if answer[0] != 1 :
        return [-1]
    else :
        return answer
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = kFactorization(n, A, k)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
