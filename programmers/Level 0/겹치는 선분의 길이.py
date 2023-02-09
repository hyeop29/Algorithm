def solution(lines):
    answer = 0
    check = False
    data= [0 for i in range(201)]
    for i in lines :
        for j in range(i[0], i[1]) :
            data[j + 100] += 1
            
    for i in data :
        if i > 1 :
            answer += 1
        
    return answer
