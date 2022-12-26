def solution(phone_number) :
    for i in range(0, len(phone_number) - 4) :
        phone_number = phone_number[:i] + "*" + phone_number[i+1:]
    return phone_number

print(solution("01031106701"))