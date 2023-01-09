def solution(lottos, win_nums) :
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    temp = 0
    answer = []
    for i in win_nums :
        if i in lottos :
            temp += 1
    answer.append(rank[temp + lottos.count(0)])
    answer.append(rank[temp])
    
    return answer
