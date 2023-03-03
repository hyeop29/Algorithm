s = input()

temp = ""
check = False
for i in s :
  if i == "<" :
    print("".join(reversed(temp)), end = "")
    temp = ""
    check = True
    
  elif check and i == ">" :
    temp += i
    print(temp, end = "")
    temp = ""
    check = False
    continue
    
  elif check == False and i == " " :
    print("".join(reversed(temp)), end = " ")
    temp = ""
    continue
    
  temp += i

if(len(temp) > 0) :
  print("".join(reversed(temp)))
