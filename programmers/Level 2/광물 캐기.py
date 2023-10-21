answer, n = 500 * 25, 0

def piro(picks, minerals, real_answer) :
    global answer
    
    # print("picks, minerals, temp_answer : ", picks, minerals, temp_answer)
    
    check1, check2 = True, True
    for i in picks : # O(3)
        if i != 0 :
            check1 = False
            break
        
    for i in minerals : # O(50)
        if i != -1 :
            check2 = False
            break
    
    if check1 or check2 :
        if answer > real_answer :
            answer = real_answer
        return
    
    else :
        for i in range(3) :
            if picks[i] > 0 :
                picks[i] -= 1
                
                temp = [mineral for mineral in minerals]
                temp_mineral = [0, 0, 0]
                temp_answer, cnt = 0, 0
                
                for j in range(n) :
                    if temp[j] != -1 and cnt < 5 :
                        if temp[j] == "diamond" :
                            temp_mineral[0] += 1
                        elif temp[j] == "iron" :
                            temp_mineral[1] += 1
                        else :
                            temp_mineral[2] += 1
                        
                        cnt += 1
                        temp[j] = -1
                    if cnt == 5 :
                        break
                
                for m in range(3) :
                    if i == 0 :
                        temp_answer += temp_mineral[m]
                    elif i == 1 :
                        if m == 0 :
                            temp_answer += temp_mineral[m] * 5
                        else :
                            temp_answer += temp_mineral[m]
                    else :
                        if m == 0 :
                            temp_answer += temp_mineral[m] * 25
                        elif m == 1 :
                            temp_answer += temp_mineral[m] * 5
                        else :
                            temp_answer += temp_mineral[m]
                        
                
                piro(picks, temp, real_answer + temp_answer)
                picks[i] += 1


def solution(picks, minerals):
    global n
    
    n = len(minerals)
    piro(picks, minerals, 0)
    
    return answer





