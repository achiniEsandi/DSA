def seq(n):
    if(n == 1):
        return 2
    else:
        return seq(n-1) / 2




while(True):
    num = int(input("Enter number: "))
    if(num == -1):
        print("Output: Finished")
        break
    elif(num < -1):
        print("Enter a positive value")
    else:
        print("Output: ",seq(num))
