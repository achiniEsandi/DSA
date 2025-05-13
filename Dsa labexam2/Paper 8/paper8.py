def s(n):
    if (n == 1):
        return 1
    else:
        return s(n-1) + n


while(True):
    num = int(input("Enter number: "))
    if(num == -1):
        break
    elif(num < -1):
        print("Negative number cannot be entered other than -1")
        continue
    print("The output is ",s(num))

    
    
