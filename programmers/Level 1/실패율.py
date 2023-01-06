def solution(N, stages) :
    answer = dict()
    stages_len = len(stages)
    for i in range(1, N+1) :
        stages_len -= stages.count(i-1)
        if stages_len == 0 :
            answer[i] = 0
        else :
            answer[i] = stages.count(i) / stages_len
    return (sorted(answer, key=lambda x: answer[x], reverse=True))

# 시간 복잡도 줄인 풀이
def solution(N, stages) :
    answer = dict()
    stages_len = len(stages)
    sc = [0 for i in range(0, N + 2)]
    for i in stages :
        sc[i] += 1

    for i in range(1, N+1) :
        if stages_len == 0:
            answer[i] = 0
        else :
            answer[i] = sc[i] / stages_len
        stages_len -= sc[i]
    return (sorted(answer, key=lambda x : answer[x] , reverse=True))
