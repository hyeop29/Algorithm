month = {1 : 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31
, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
Days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

def solution(a, b) :
    answer = 4 + b
    for i in range(1, a) :
        answer += month[i]
    answer = answer % 7
    return Days[answer]
