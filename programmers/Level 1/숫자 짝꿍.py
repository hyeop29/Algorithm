def solution(X, Y):
    X_count = []
    Y_count = []
    answer = ""
    for i in range(10) :
         X_count.append(X.count(str(i)))
         Y_count.append(Y.count(str(i)))
    
    for i in range(9, -1, -1) :
        if X_count[i] >= Y_count[i] :
            if Y_count[i] == 0 :
                continue
            else :
                answer += str(Y_count[i] * str(i))
        else :
            if X_count[i] == 0:
                continue
            else :
                answer += str(X_count[i] * str(i))
        
    if answer == "":
        answer = "-1"
    elif answer[0] == "0":
        answer = "0"
    return answer
