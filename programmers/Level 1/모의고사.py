def solution(answers) :
    answer_list = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    answer = [0, 0, 0]
    person = []
    for i in range(len(answers)) :
        for j in range(len(answer_list)) :
            if answers[i] == answer_list[j][i % len(answer_list[j])] :
                answer[j] += 1

    for i in range(len(answer)) :
        if answer[i] == max(answer) :
            person.append(i + 1)
    return person
