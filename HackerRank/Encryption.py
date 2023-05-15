#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    s_len = len(s)
    temp = s_len**(1/2)
    row, col = math.floor(temp), math.ceil(temp)
    if row * col < s_len :
        row += 1
        
    encry = []
    count = 0
    for i in range(row) :
        a = []
        for j in range(col) :
            if count == s_len :
                a.append("")
            else :
                a.append(s[count])
                count += 1
        encry.append(a)  
        
    result = ""
    for j in range(col) :
        for i in range(row) :
            result += encry[i][j]
        result += " "
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
