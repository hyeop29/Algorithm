def solution(price, money, count) :
    sum_price = 0
    for i in range(1, count + 1) :
        sum_price += i*price
    if sum_price > money :
        answer = sum_price - money
    else :
        answer = 0 
    return answer