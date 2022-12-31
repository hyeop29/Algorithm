def solution(array, commands) :
    answer = []
    for i in commands :
        command = list(map(lambda x: x-1, i))
        new = array[command[0]:command[1] + 1]
        new.sort()
        answer.append(new[command[2]])

    return answer
