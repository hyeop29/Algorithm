def solution(s):
    answer = []
    answer_str = []
    s = list(s)
    for i in s :
        if i not in answer_str:
            answer.append(-1)
        else :
            index, count = 0, 0
            for j in answer_str :
                if i == j :
                    index = count
                count += 1
            answer.append(len(answer_str) - index)
        
        answer_str.append(i)

    return answer
