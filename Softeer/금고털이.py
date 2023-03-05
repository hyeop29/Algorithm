"""
문제 : 루팡은 배낭을 하나 메고 은행금고에 들어왔다. 금고 안에는 값비싼 금, 은, 백금 등의 귀금속 덩어리가 잔뜩 들어있다. 배낭은 W ㎏까지 담을 수 있다.
각 금속의 무게와 무게당 가격이 주어졌을 때 배낭을 채울 수 있는 가장 값비싼 가격은 얼마인가?
루팡은 전동톱을 가지고 있으며 귀금속은 톱으로 자르면 잘려진 부분의 무게만큼 가치를 가진다.
입력형식 : 첫 번째 줄에 배낭의 무게 W와 귀금속의 종류 N이 주어진다. i + 1 (1 ≤ i ≤ N)번째 줄에는 i번째 금속의 무게 Mi와 무게당 가격 Pi가 주어진다.
"""
import sys

MP = list()
price = 0
w, n = map(int,input().split())
for i in range(n) :
    mp = list(map(int, input().split()))
    MP.append(mp)

MP.sort(key = lambda x : x[1], reverse = True)
for m, p in MP :
    if w >= m :
        price += m * p
        w -= m
    else :
        price += w * p
        break

print(price)
