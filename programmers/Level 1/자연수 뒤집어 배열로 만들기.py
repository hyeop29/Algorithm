def solution(n):
    answer = [int(i) for i in str(n)]
    answer.reverse()
    return answer

print(solution(12345))