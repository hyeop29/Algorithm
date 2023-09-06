T = int(input())

for i in range(1, T + 1) :
    check = True
    for j in str(i) :
        if j in ['3','6','9'] :
            check = False
            print('-', end = "")
    if check :
        print(i, end = "")

    print(" ", end ="")
