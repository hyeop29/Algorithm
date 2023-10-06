def solution(m, n, puddles):
    record = [[0 for _ in range(m)] for _ in range(n)]
    if len(puddles) > 0 :
        for water in puddles :
            wy, wx = water
            record[wx - 1][wy - 1] = -1
    
    for i in range(n) :
        for j in range(m) :
            if record[i][j] == -1 :
                record[i][j] = 0
            elif i == 0 and j == 0 :
                record[i][j] = 1
            elif i != 0 and j == 0 :
                record[i][j] = record[i - 1][j]
            elif i == 0 and j != 0 :
                record[i][j] = record[i][j - 1]
            elif i != 0 and j != 0 :
                record[i][j] = record[i - 1][j] + record[i][j - 1] 
                
    return record[n - 1][m - 1] % 1000000007
