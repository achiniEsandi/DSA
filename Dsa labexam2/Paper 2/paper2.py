def Fibonacci(n):
    if(n <= 1):
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)




while(True):
    num = int(input("Enter number: "))
    if(num == -1):
        break
    print("Output: ",Fibonacci(num))
