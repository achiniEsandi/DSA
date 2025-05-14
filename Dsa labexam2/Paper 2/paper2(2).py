

def Fibonacci(n):
    if(n <= 1):
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


while(True):
    num = int(input("Enter a number (-1 to exit): "))
    if(num == -1):
        print("Program ended")
        break
    elif(num <-1):
        print("Enter a positive number")
        #continue
    else:
        print("Output: ",Fibonacci(num))

