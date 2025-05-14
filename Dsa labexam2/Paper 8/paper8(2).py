def calSum(n):
    if(n == 1):
        return 1
    else:
        return (calSum(n-1) + n)



while(True):
    num = int(input("Enter a number: "))

    if(num == -1):
        print("Program ended")
        break

    elif(num < -1):
        print("Enter a positive number")

    else:
        print("Output: ", calSum(num))

