def solution(x):
    a = list(str(x))
    sum = 0
    for i in a :
        sum += int(i)
    
    if (x % sum) == 0 :
        return True
    else :
        return False

print(solution(10))
print(solution(11))
print(solution(12))
print(solution(13))