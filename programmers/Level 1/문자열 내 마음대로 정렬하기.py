def solution(strings, n) :
    strings.sort()
    print(strings)
    answer = []
    answer = sorted(strings, key = lambda x:x[n])
    return answer
