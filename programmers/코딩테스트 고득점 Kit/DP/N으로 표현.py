def solution(N, number):
    
    total = [set() for i in range(9)]
    
    for i in range(1, 9) :
        total[i].add(int(str(N) * i))
        if i > 1 :
            for j in range(1, i) :
                for s in total[j] :
                    for k in total[i - j] :
                        total[i].add(s + k)
                        total[i].add(s - k)
                        total[i].add(s * k)
                        if k != 0 :
                            total[i].add(s // k)
        if number in total[i] :
            return i
    return -1
