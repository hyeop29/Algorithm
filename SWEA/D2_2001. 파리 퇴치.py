import sys
sys.stdin = open("input.txt")

INF = float("inf")

def count_die(r, c) :
    cnt = 0
    for i in range(m) :
        for j in range(m) :
            cnt += pari[r + i][c + j]
    return cnt

def kill() :
    max_kill = -INF

    for i in range(n - m + 1) :
        for j in range(n - m + 1) :
            temp = count_die(i, j)

            if max_kill < temp :
                max_kill = temp

    return max_kill

T = int(input())

for tc in range(1, T + 1) :
    n, m = map(int, input().split())
    pari = [list(map(int, input().split())) for _ in range(n)]
    answer = kill()

    print("#" + str(tc), answer)
