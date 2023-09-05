headline = input()

for i in headline :
    if 97 <= ord(i) <= 122 :
        i = chr(ord(i) - 32)

    print(i, end = "")
