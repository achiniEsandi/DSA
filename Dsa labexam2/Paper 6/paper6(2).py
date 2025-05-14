def sumcube(n):
    if(n == 1):
        return n
    else:
        return (sumcube(n - 1) + n * n * n)




while(True):
    num = int(input("Enter number (-1 to exit): "))

    if(num == -1):
        print("Program ended")
        break

    elif(num <-1):
        print("Enter a positive number")

    else:
        print("Output: ",sumcube(num))

    
