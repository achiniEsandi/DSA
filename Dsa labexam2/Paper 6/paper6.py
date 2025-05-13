def sumcube(n):
    if (n == 1):
        return 1
    else:
        return (sumcube(n-1)+n*n*n)



while(True):
    num = int(input("Enter number: "))
    if( num == -1):
        break
    else:
        print("Output: ",sumcube(num))
