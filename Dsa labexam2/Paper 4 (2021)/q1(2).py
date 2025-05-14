def seq(n):
    if(n == 1):
        return n
    else:
        return (n-1) + seq(n-1)




while(True):
    num = int(input("Enter number: "))

    if(num == -1):
        print("Output: Finished")
        break

    elif(num < -1):
        print("Enter a positive number\n")
        continue

    print("Output: ",seq(num))
