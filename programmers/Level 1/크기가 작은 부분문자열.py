def solution(t, p):
    len_t = len(t)
    len_p = len(p)
    i, answer = 0, 0
    while( i + len_p <= len_t) :
        if t[i: i + len_p] <= p :
            answer += 1
        i += 1

    return answer
