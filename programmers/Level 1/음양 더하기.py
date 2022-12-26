def solution(absolutes, signs) :
    for i in range(0,len(absolutes)) :
        if not signs[i] :
                absolutes[i] = -absolutes[i]
    return sum(absolutes)

print(solution([4,7,12],[True,False,True]))