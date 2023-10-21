answer = 0
n = -1

queen = []

def backtracking(num) :
    global answer
    
    if num == n :
        answer += 1
        return
    
    for i in range(n) :
        check = True
        for j in range(num) :
            if i == queen[j] :
                check = False
                break
            
            elif abs(queen[j] - i) == num - j :
                check = False
                break
        
        if check :
            queen[num] = i
            backtracking(num + 1)
    
def solution(_n):
    global n, queen
    n = _n
    queen = [-1 for _ in range(n)]
    
    backtracking(0)
    return answer
