def solution(s):
    number = {"zero" : "0" ,"one" : "1", "two" : "2", "three" : "3", "four" : "4"
    , "five" : "5","six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}
    
    temp, answer ="", ""
    for i in s :
        if i in number.values() :
            answer += i
        else :
            temp += i
            if temp in number :
                answer += number[temp]
                temp = ""

    return int(answer)
