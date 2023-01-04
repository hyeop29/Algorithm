# 에라토스테네스의 체 방식 사용

import math 

def solution (n) :
    answer = 0
    prime = list(range(n + 1))
    for i in range(2, int(math.sqrt(n + 1)) + 1) :
        if prime[i] == 0 :
            continue
        else :
            j = 2
            while i * j <= n :
                prime[i * j] = 0
                j += 1
    for i in range(2, n + 1) :
        if prime[i] > 0 :
            answer += 1
    return answer
