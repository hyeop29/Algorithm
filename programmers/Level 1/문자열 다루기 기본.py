def solution(s) :
    number_list = []

    for i in range(10) :
        i = str(i)
        number_list.append(i)
    
    if len(s) == 4 or len(s) == 6 :
        for i in s :
            if i not in number_list :
                return False
        return True
    else :
        return False
    

print(solution("1aaa"))