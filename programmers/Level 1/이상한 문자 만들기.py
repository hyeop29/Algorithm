def solution(s) :
    s = s.split(' ')
    answer = ''
    for i in range(0,len(s)) :
        for j in range(0, len(s[i])) :
            if j % 2 == 0 :
                answer += s[i][j].upper()
            else :
                answer += s[i][j].lower()
        if i != len(s) - 1 :
            answer += " "
    return answer
print(solution("try hello world"))