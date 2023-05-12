def solution(distance, rocks, n):
    answer = 0
    left, right = 0, distance    
    rocks.sort()
    rocks.append(distance)

    while (left <= right) :
        temp, count = 0, 0
        mid = (left + right) // 2
        for rock in rocks :
            if mid > rock - temp :
                count += 1
            elif mid <= rock - temp :
                temp = rock
                
            if count > n : # 제거한 돌이 n 보다 크면 종료
                break
                
        if count > n : # 제거한 돌이 n 보다 크면 지정한 돌 사이의 간격이 크다 => 줄이자
            right = mid - 1
        else : # 같을 경우 answer에 현재 mid 값을 주고, 더 늘어날 수 있으니 줄여본다
            answer = mid
            left = mid + 1

    return answer
