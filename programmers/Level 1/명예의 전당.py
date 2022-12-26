# 리스트의 0번째 항목부터 새로운 리스트에 추가
# 새로운 리스트는 오름차순 정렬 k 번째에 해당하는 값 answer 배열에 추가

def solution(k, score):
    temp = []
    answer = []
    k -= 1
    for i in range(len(score)) :
        temp.append(score[i])
        temp.sort(reverse=True)
        if i  < k :
            answer.append(temp[i])
        else :
            answer.append(temp[k])
    return answer


k = 3
score = [10,100,20,150,1,100,200]
print(solution(k, score))