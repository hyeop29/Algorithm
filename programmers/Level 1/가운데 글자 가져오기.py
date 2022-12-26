def solution(s) :
    answer = ''
    s_len = len(s)
    s_mid = s_len // 2
    
    if (s_len % 2) == 0 :
        answer = s[s_mid - 1 : s_mid + 1]
    else :
        answer = s[s_mid]
    
    return answer

print(solution("abcde"))