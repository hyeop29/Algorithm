def solution(s):
    s = list((s.upper()))
    p_count = 0
    y_count = 0
    for i in s :
        if i == 'P':
            p_count += 1
        elif i == 'Y':
            y_count += 1
    
    if (p_count == y_count) :
        return True
    else :
        return False

print(solution("pPoooyY"))
print(solution("Pyy"))