import sys

message = input()
key = input()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
key55 = [['' for _ in range(5)] for _ in range(5)]
row, col = 0, 0

check = True

for i in key :
    for temp in key55 :
        if i in temp :
            check = False
            break
    if check :
        key55[row][col] = i
        col += 1
        if col == 5 :
            col = 0
            row += 1
            if row == 5 :
                check = False
                break
    check = True

if check :
    for i in alphabet :
        for temp in key55 :
            if i in temp :
                check = False
                break
        if check :
            key55[row][col] = i
            col += 1
            if col == 5 :
                col = 0
                row += 1
                if row == 5 :
                    break
        check = True

# 메세지를 두 글자씩 나누는 일
check = True
message2 = ''
message2 += message[0]
for i in range(1, len(message)) :
    if check and message[i] == message2[-1] :
        if message[i] == 'X' :
            message2 += 'Q'
        else :
            message2 += 'X'

    message2 += message[i]
    if len(message2) % 2 == 0 :
        check = False
    else : check = True

if len(message2) % 2 != 0 :
    message2 += 'X'

# 암호화 시작
for i in range(0, len(message2), 2) :
    for j in range(5) :
        for k in range(5) :
                if message2[i] == key55[j][k] :
                    row1 = j
                    col1 = k
                if message2[i + 1] == key55[j][k] :
                    row2 = j
                    col2 = k
    if row1 == row2 :
        print(key55[row1][(col1 + 1) % 5], end = '')
        print(key55[row2][(col2 + 1) % 5], end = '')
    elif col1 == col2 :
        print(key55[(row1 + 1) % 5][col1], end = '')
        print(key55[(row2 + 1) % 5][col2], end = '')
    else :
        print(key55[row1][col2], end = '')
        print(key55[row2][col1], end = '')
