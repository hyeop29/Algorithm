def solution(dartResult) :
    digit = [0 for i in range(3)]
    print(digit)
    count, i = 0, -1
    while count < len(dartResult) :
        if dartResult[count].isdigit() :
            i += 1
            if dartResult[count + 1].isdigit() :
                digit[i] = int(dartResult[count] + dartResult[count + 1])
                count += 1
            else :
                digit[i] = int(dartResult[count])
        
        elif dartResult[count] == "D" :
            digit[i] = pow(digit[i], 2)
        elif dartResult[count] == "T" :
            digit[i] = pow(digit[i], 3)
        elif dartResult[count] == "*" :
            for j in range(i - 1, i + 1):
                digit[j] = 2*digit[j]
        elif dartResult[count] == "#" :
            digit[i] = -1*digit[i]

        count += 1

    return sum(digit)
