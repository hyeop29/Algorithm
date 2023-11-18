import sys
sys.stdin = open("input.txt")

from collections import defaultdict

T = int(input())

for tc in range(1, T + 1) :
    temp = int(input())
    score = list(map(int, input().split()))

    count_score = defaultdict(int)
    for i in score :
        count_score[i] += 1

    max_key = max(count_score, key = count_score.get)
    print("#" + str(tc), max_key)
