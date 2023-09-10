def benefit(day, price_list) :
    answer = 0
    max_price = price_list[day - 1]
    for i in range (day - 1, -1, -1) :
       if max_price < price_list[i] :
           max_price = price_list[i]
       else :
           answer += max_price - price_list[i]

    return answer

T = int(input()) # 테스트 케이스의 수

for i in range(1, T + 1) :
    n = int(input()) # n일 동안의 물건의 매매가 예측
    price = list(map(int, input().split()))
    answer = benefit(n, price)
    print("#" + str(i), answer)
