import math

def solution(n):
    n_sqrt = math.sqrt(n)
    k = int(n_sqrt)
    if (pow(k, 2) == n) :
        return pow( k+1, 2)
    else :
        return -1

print(solution(121))
print(solution(3))
