import sys
import math
from collections import deque

H, K, R = map(int,input().split())

result = 0
tree = [dict({"left" : deque([]), "right" : deque([])}) for _ in range(pow(2,H))]

for _ in range(pow(2,H)) :
    tree.append(deque(list(map(int,input().split()))))


for i in range(1, R + 1) :
    if i % 2 == 0 :
        if(len(tree[1]['right']) > 0) :
            result += tree[1]['right'].popleft()

        for j in range(2, pow(2,H)) :
            if(len(tree[j]['right']) < 1) :
                continue
            else :
                if(j % 2 == 0) :
                    tree[j//2]['left'].append(tree[j]['right'].popleft())
                else :
                    tree[j//2]['right'].append(tree[j]['right'].popleft())
    
    else :
        if(len(tree[1]['left']) > 0) :
            result += tree[1]['left'].popleft()

        for j in range(2, pow(2,H)) :
            if(len(tree[j]['left']) < 1) :
                continue
            else :
                if(j % 2 == 0) :
                    tree[j//2]['left'].append(tree[j]['left'].popleft())
                else :
                    tree[j//2]['right'].append(tree[j]['left'].popleft())

    if i <= K :
        for k in range(pow(2, H), len(tree)) :
            if k % 2 == 0 :
                tree[k//2]['left'].append(tree[k].popleft())
            else :
                tree[k//2]['right'].append(tree[k].popleft())


print(result)
