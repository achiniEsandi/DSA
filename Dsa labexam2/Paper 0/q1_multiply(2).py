def Multiply(M,n):
    if(n == 1):
        return M
    else:
        return (M + Multiply(M, n-1))



while(True):
    M = int(input("Enter number M: "))
    if(M == -1):
        print("Program ended")
        break
    
    n = int(input("Enter number n: "))
    if(n == 0):
        print("Output: ",0)
        continue

    print("Output: ",Multiply(M,n))
