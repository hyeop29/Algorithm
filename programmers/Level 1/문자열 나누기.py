def solution(s):
    count1 = 0
    count2 = 0
    answer = 0
    k = 0
    for i in range(len(s)) :
         if s[i] == s[k] :
            count1 += 1
         else:
            count2 += 1
         
         if count1 == count2 :
            count1 = 0
            count2 = 0
            k = i + 1
            answer += 1
    if count1 != count2:
        answer +=1

    return answer

s = "abracadabra"
print(solution(s))
